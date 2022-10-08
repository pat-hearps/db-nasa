from dotenv import load_dotenv
load_dotenv()

import os

from sqlalchemy import create_engine

DBPASS = os.getenv("POSTGRES_PASSWORD", default="")
DBNAME = os.getenv("POSTGRES_DB", default="nasa")
DBUSER = os.getenv("POSTGRES_USER", default="pat")
DBHOST = os.getenv("DB_HOST", default="localhost")
DBPORT = os.getenv("DB_PORT", default="5432")

DB_URL = f"postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}:{DBPORT}/{DBNAME}"


def get_engine():
    return create_engine(url=DB_URL)
