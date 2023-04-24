#importing Flask, render_template, jasonify and request classes from flask module
from flask import Flask, render_template, jsonify, request
from database import get_data_from_db, load_job, insert_application_to_db

#Initializing Flask class object
app = Flask(__name__)

# JOBS = [{
#   'id': 1,
#   'title': 'Data Scientist',
#   'location': 'Gurugram, India',
#   'salary': 'Rs.12,00,000'
# }, {
#   'id': 2,
#   'title': 'Font End Developer',
#   'location': 'Pune, India',
#   'salary': ''
# }, {
#   'id': 3,
#   'title': 'Full Stack',
#   'location': 'London, United Kingdom',
#   'salary': '$120,000'
# }]


#decorating hello_world function with app
@app.route("/")
#hello_world funtion which get the data from database and pass that to rendered template
def hello_world():
  JOBS = get_data_from_db()
  #fetching job data and showing list of available job to home page
  return render_template('home.html', jobs=JOBS, company_name='Webbullz')


@app.route('/api')
def list_job():
  #fetching data from database
  JOBS = get_data_from_db()
  #returning data in json format
  return jsonify(JOBS)


#funtion to get job details from database with the help of id 
@app.route('/jobs/<id>')
def get_job_description(id):
  job_disc = load_job(id)
  #showing details job description to user for which user click apply
  return render_template('job_page.html', job=job_disc)

#function to collect data filled in form by post method and save that in database
@app.route('/job/<id>/apply', methods=['post'])
def get_applicant_details(id):
  #get data filled in form and assign it into data
  data = request.form
  #fetching job details by id
  job = load_job(id)
  #saving form data into database
  insert_application_to_db(id, data)
  #showing thank you page to user
  return render_template('thank_you.html', application=data, job=job)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
