
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

conn_str = 'clickhouse://default:slieer@192.168.122.83/default'

engine = create_engine(conn_str)
session = sessionmaker(bind=engine)()