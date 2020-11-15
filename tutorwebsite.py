from app import app
from app import db
from app.models import user

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'user': user, 'course': course, 'session': session, 'cart': cart, 'rating': rating}
