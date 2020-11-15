from app import app
from app import db
from app.models import usertable

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': usertable, 'Course': coursetable, 'Session': sessiontable, 'Cart': carttable, 'Rating': ratingtable}
