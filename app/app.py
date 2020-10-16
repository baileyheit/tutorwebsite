import sqlalchemy
from flask import Flask, render_template, redirect, url_for
# import models
import forms


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'

@app.route('/')
def hello_world():
  return 'Hello, World!'
# def all_tutors():
#   tutors = db.session.query(models.Tutors).all()
#   return render_template('all-tutors.html', tutors=tutors)                        #implement all-tutors.html template

# @app.route('/tutors', methods=['GET', 'POST'])
# def tutors():
#   class_names = [c.class_id for c in db.session.query(models.CanTutorIn).all()]
#   form = forms.TutorsFormFactory.form(class_names=class_names)                    #implement TutorsFormFactory function in forms.py
#   if form.validate_on_submit():
#     return redirect('/tutors/'+form.class_sel.data)
#   return render_template('tutors.html', form=form)                                #implement tutors.html template

# @app.route('/tutors/<class_name>')
# def tutors_in(class_name):
#   results = db.session.query(models.CanTutorIn, models.Users) \
#                       .filter(models.CanTutorIn.class_id == class_name) \
#                       .join(models.Users).all()
#   return render_template('tutors_in.html', class_name=class_name, data=results)   #implement tutors_in.html template


# # @app.route('/')
# # def hello_world():
# #     return 'Hello, World!'

# # mysql://username:password@server/db

if __name__ == '__main__':
  app.init_db()
  app.run(host='0.0.0.0')