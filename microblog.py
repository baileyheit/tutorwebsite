from app import app
from app import db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Course': Course, 'Session': Session, 'Cart': Cart, Rating: 'Rating'}
