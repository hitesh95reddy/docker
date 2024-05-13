from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URI='postgresql://postgres:postgres@localhost:5432/postgres'
engine=create_engine(DB_URI)
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
