# ~/movie-service/app/api/db.py
import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, ARRAY

from databases import Database

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL is None:
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("plot", String(250)),
    Column("genres", ARRAY(String)),
    Column("casts_id", ARRAY(Integer)),
)

database = Database(DATABASE_URL)
