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


def load_job(id):
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs WHERE id = :ids'),
                          {"ids": id})
    row = result.all()
    if len(row) == 0:
      return None
    else:
      jobdis = row[0]._asdict()
      return jobdis


def insert_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      'insert into applications(job_id, full_name, email, linkedin_url, education, experience, resume_url) values(:job_id, :full_name, :email, :linkedin_url, :education, :experience, :resume_url)'
    )
    conn.execute(
      query, {
        'job_id': job_id,
        'full_name': data['name'],
        'email': data['email_id'],
        'linkedin_url': data['linkedin_url'],
        'education': data['education'],
        'experience': data['experience'],
        'resume_url': data['resume_url']
      })
