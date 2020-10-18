from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import SelectField, SubmitField
import models
import app


class TutorsFormFactory:
    @staticmethod
    def form(class_names):
        class F():
            class_sel = SelectField('Class Name', choices= models.Classes)
            submit = SubmitField('Submit')
        return F()