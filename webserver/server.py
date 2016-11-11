import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@<IP_OF_POSTGRE_SQL_SERVER>/postgres
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://ewu2493:foobar@<IP_OF_POSTGRE_SQL_SERVER>/postgres"
DATABASEURI = "sqlite:///test.db"
# This line creates a database engine that knows how to connect to the URI above
engine = create_engine(DATABASEURI)

@app.before_request
def before_request():
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None
    
@app.teardown_request
def teardown_request(exception):
  try:
    g.conn.close()
  except Exception as e:
    pass
  
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
@app.route('/')
def index():pass


#sign up
@app.route('/signup')
def signup():pass

#add user
@app.add('/signup/add')
def add():pass


#sign up successfully
@@app.route('/signupsuccessfully')
def sus():pass


#employer
@app.route('/employer/<username>')
def profile_e(username): pass

#jobseeker
@app.route('/jobseeker/<username>')
def profile_j(username): pass

#friendlist
@app.route('/friendlist/<username>')
def list(username):pass

#add friend
@app.route('/friendlist/<username>/add')
def add_f(username):pass

#delete friend
@app.route('/friendlist/<username>/delete)
def delete_f
           
#update employer profile
@app.route('/employer/<username>/update')
def update_e(username):pass

           
#update jobseeker profile
@app.route('/jobseeker/<username>/update')
def update_j(username):pass 
           
           
#jobs of an employer
@app.route('/employer/<username>/job)
def job_posted(username):pass
           
       
#post new job
@app.route('/employer/<username>/postjob')
def add_j(username):pass
           
  
#delete job
@app.route('/employer/<username>/deletejob')
def delete_j(username):pass


#all jobs for employer
@app.route('/job)
def job():pass
           

#resume
@app.route('/jobseeker/<username>/resume')
def resume(username):pass
           

#update resume
@app.route('/jobseeker/<username>/resume/update')
def resume_update(username):pass
          
           
#search job
@app.route('jobseeker/<username>/search')
def search_j(username):pass
           
           
#apply job
@app.route('jobseeker/<username>/applyjob')
def apply_job(username):pass
           
           
#view job apply and interview for jobseeker
@app.route('jobseeker/<username>/status')
def apply(username):pass
           

#search resume
@app.route('/employer/<username>/searchresume')
def search_r(username):pass
           

#resume followed
@app.route('/employer/<username>/resume')
def resume_followed(username):pass

          
#follow resume
@app.route('/employer/<username>/follow')
def follow(username):pass

           
#view application and interview for employer
@app.route('/employer/<username>/application')
def application(username):pass
           
           
#edit status of application
@app.route('/editstatus')
def edit():pass