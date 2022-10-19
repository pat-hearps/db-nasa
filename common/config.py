from dotenv import load_dotenv
load_dotenv()

from datetime import datetime
import os

DBPASS = os.getenv("POSTGRES_PASSWORD", default="")
DBNAME = os.getenv("POSTGRES_DB", default="nasa")
DBUSER = os.getenv("POSTGRES_USER", default="pat")
DBHOST = os.getenv("DB_HOST", default="localhost")
DBPORT = os.getenv("DB_PORT", default="5432")

DB_URL = f"postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}:{DBPORT}/{DBNAME}"

HTTPS = "https://"
HOST_EPIC = "epic.gsfc.nasa.gov"
API = "api"
ARCHIVE = "archive"
NATURAL = "natural"
ENHANCED = "enhanced"
PNG = "png"
JPG = "jpg"
BASE_ADDR = f"{HTTPS}{HOST_EPIC}"

INIT_DATE = datetime(2021, 1, 1)

