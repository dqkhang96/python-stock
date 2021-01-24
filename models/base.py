from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

server = 'localhost' 
database = 'master' 
username = 'SA' 
password = '????' 
db_string = 'mssql+pymssql://{}:{}@{}:{}/{}'.format(username,password,server,1433,database)


#db_string = "postgresql://mapping:storymapping@104.155.128.44:5432/story_mapping"

engine = create_engine(db_string)

Session = sessionmaker(bind=engine)

Base = declarative_base()