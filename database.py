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
  #opening connection with database
  with engine.connect() as con:
    result = con.execute(text('select * from jobs'))
    #converting sqlalchemy object to list
    result_all = result.all()
    #creating a empty list
    job_data_in_dict = []
    #Iterating list of jobs
    for result in result_all:
      #converting each item of list into dictionary and adding them to empty list
      job_data_in_dict.append(result._asdict())
  return job_data_in_dict


def load_job(id):
  #opening connection with databse
  with engine.connect() as conn:
    #executing sql query to get job data of a specific id
    result = conn.execute(text('select * from jobs WHERE id = :ids'),
                          {"ids": id})
    #converting sqlalchemy object to list
    row = result.all()
    if len(row) == 0:
      return None
    else:
      #converting list to dictionary
      jobdis = row[0]._asdict()
      return jobdis


#saving data to databse
def insert_application_to_db(job_id, data):
  #opening connecting to database
  with engine.connect() as conn:
    query = text(
      'insert into applications(job_id, full_name, email, linkedin_url, education, experience, resume_url) values(:job_id, :full_name, :email, :linkedin_url, :education, :experience, :resume_url)'
    )
    #executing insert query and passing data fields
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
