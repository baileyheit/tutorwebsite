from flask import Flask
import app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import models
import forms

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@localhost/TutorProject'
#^change to this route when deployed


@app.route('/')
def all_tutors():
  tutors = db.session.query(models.Tutors.all())
  return render_template('all-tutors.html', tutors=tutors)                        #implement all-tutors.html template

@app.route('/tutors', methods=['GET', 'POST'])
def tutors():
  class_names = [c.class_id for c in deb.session.query(models.CanTutorIn).all()]
  form = forms.TutorsFormFactory.form(class_names=class_names)                    #implement TutorsFormFactory function in forms.py
  if form.validate_on_submit():
    return redirect('/tutors/'+form.class_sel.data)
  return render_template('tutors.html', form=form)                                #implement tutors.html template

@app.route('/tutors/<class_name>')
def tutors_in(class_name):
  results = db.session.query(models.CanTutorIn, models.Users) \
                      .filter(models.CanTutorIn.class_id == class_name) \
                      .join(models.Users).all()
  return render_template('tutors_in.html', class_name=class_name, data=results)   #implement tutors_in.html template


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# mysql://username:password@server/db

if __name__ == '__main__':
  app.run(host='0.0.0.0')