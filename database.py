#importing required libs from sqlalchemy
from sqlalchemy import create_engine, text
import os

#building connection with planetscale server
db_connection_cred = os.environ['DB_STRING']
engine = create_engine(db_connection_cred,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

#executing SQL query to get data from planetscale database
def get_data_from_db():
  with engine.connect() as con:
    result = con.execute(text('select * from jobs'))
    result_all = result.all()
    job_data_in_dict = []
    for result in result_all:
      job_data_in_dict.append(result._asdict())
  return job_data_in_dict