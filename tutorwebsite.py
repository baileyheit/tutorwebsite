from app import app
from app import db
from app.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'user': User, 'course': Course, 'session': Session, 'cart': Cart, 'rating': Rating}
