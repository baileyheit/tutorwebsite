from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@vcm-17138.vm.duke.edu/TutorProject'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:21bH1267@localhost/TutorProject'


db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# mysql://username:password@server/db

if __name__ == '__main__':
  app.run(host='0.0.0.0')