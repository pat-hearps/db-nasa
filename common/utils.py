import requests

from common.log_config import get_logger

logger = get_logger(__file__)


def get_request(url: str) -> requests.Response:
    """Helper for requesting URLs with status and error handling"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            logger.warning(f"Couldn't retrieve {url}\nstatus={response.status_code}\nbody={response.content}")
    except Exception:
        logger.error(f"Error requesting {url}: ", exc_info=True)
