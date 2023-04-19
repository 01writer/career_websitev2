from flask import Flask, render_template, jsonify, request
from database import get_data_from_db, load_job

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


@app.route("/")
def hello_world():
  JOBS = get_data_from_db()
  return render_template('home.html', jobs=JOBS, company_name='Webbullz')


@app.route('/api')
def list_job():
  JOBS = get_data_from_db()
  return jsonify(JOBS)


@app.route('/jobs/<id>')
def get_job_description(id):
  job_disc = load_job(id)
  print(type(job_disc))
  print(job_disc)
  # if not job_disc:
  #   return "Not Found"
  return render_template('job_page.html', job=job_disc)


@app.route('/job/<id>/apply', methods=['post'])
def get_applicant_details(id):
  data = request.form
  return jsonify(data)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
