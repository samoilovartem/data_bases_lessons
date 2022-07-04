from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://kfqfowsd:Kw5evNR-rV-lMQ3aDTzB5oGMhWyHOo0H@tiny.db.elephantsql.com/kfqfowsd')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()