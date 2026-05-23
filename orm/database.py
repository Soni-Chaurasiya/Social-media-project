from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL =f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine = create_engine(SQLALCHEMY_DATABASE_URL) 

sessionLocal = sessionmaker(autoflush=False, autocommit = False, bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()   



while True:
    try:
        conn = psycopg2.connect(host = settings.database_hostname,database = settings.database_name, user=settings.database_username, password = settings.database_password, port=settings.database_port,cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        # print("connected successfully...")
        break

    except Exception as error:
        print("failed to connect db...")
        print("Error ------",error)  


