import json
from datetime import datetime
import time

from sqlalchemy.orm import Session

from common.config import BASE_ADDR, API, ENHANCED, INIT_DATE
from common.directory import DIR
from common.log_config import get_logger
from common.utils import get_request
from backend.models import EpicMeta
from migrations.utils import get_engine

logger = get_logger(__file__, level="DEBUG")

fp_avail = DIR.DATA.TEMP / 'available.json'


def get_available():
    logger.info("Fetching available image dates")
    address = f"{BASE_ADDR}/{API}/{ENHANCED}/available"
    resp = get_request(address)
    if resp:
        dates = resp.json()
        dates = [d for d in dates if datetime.fromisoformat(d) >= INIT_DATE]
        fp_avail.write_text(json.dumps(dates, indent=2))
        logger.info(f"{len(dates)} dates saved to {fp_avail}")


def main():

    if not fp_avail.exists():
        get_available()

    available_dates = json.loads(fp_avail.read_text())

    engine = get_engine()

    for dt_str in available_dates:
        address = f"{BASE_ADDR}/{API}/{ENHANCED}/date/{dt_str}"
        resp = get_request(address)
        if not resp:
            logger.info(f"No metadata response from {address}")
            continue
        try:
            rj = resp.json()

            with Session(engine) as session:
                epics, names = [], []
                for meta in rj:
                    name = meta['image']
                    coords = meta['centroid_coordinates']
                    obj_meta = EpicMeta(identifier=meta['identifier'],
                                        taken_datetime=datetime.fromisoformat(meta['date']),
                                        version=meta['version'],
                                        image_name=name,
                                        centroid_lat=coords['lat'],
                                        centroid_long=coords['lon']
                                        )
                    epics.append(obj_meta)
                    names.append(name)
                logger.info(f"Found {len(names)} rows of metadata for {dt_str}, adding to DB")
                logger.debug(f"Image names: {names}")

                session.add_all(epics)
                session.commit()
                logger.info("Committed")

        except Exception:
            logger.error("problem: ", exc_info=True)

            time.sleep(0.5)


if __name__ == '__main__':
    main()
