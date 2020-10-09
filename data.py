import faker
from faker import Factory
import random
from random import randint
import mysql.connector

cnx = mysql.connector.connect(user='root', database='TutorProject')
cursor = cnx.cursor()

user = Factory.create()

userids = []
tutors = {}
tuttees = {}


# Create phone numbers: xxx-xxx-xxxx
def create_phone_number():
    number = ''
    for i in range(12):
        if i in [3, 7]:
            number += '-'
        else:
            number += str(randint(0, 9))
    return number


# Create unique random user ids
def create_user_id():
    uid = randint(0, 999999)
    if uid in userids:
        create_user_id()
    userids.append(uid)
    return uid


# Create 1000 tutors
for i in range(1000):
    uid = create_user_id()
    tutors[uid] = {
        'phone_number': create_phone_number(),
        'address': user.address(),
        'name': user.name(),
        'user_id': uid,
        'location': random.choice(['remote', 'in person']),
        'school': random.choice(['trinity', 'pratt']),
        'age': user.random_int(min=17, max=24, step=1),
        'email': user.free_email(),
        'venmo': '@' + user.user_name(),
        'bio': user.text(),
        'rating': user.random_int(min=1, max=20, step=1)/4.0,
        'hourly_rate': '$' + str(user.random_int(min=0, max=50)),
        'grade': random.choice(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'])
    }


# Create 1000 tuttees
for i in range(1000):
    uid = create_user_id()
    tuttees[uid] = {
        'phone_number': create_phone_number(),
        'address': user.address(),
        'name': user.name(),
        'user_id': uid,
        'location': random.choice(['remote', 'in person']),
        'school': random.choice(['trinity', 'pratt']),
        'age': user.random_int(min=17, max=24, step=1),
        'email': user.free_email(),
        'venmo': '@' + user.user_name(),
        'bio': user.text(),
        'price_range': '$' + str(user.random_int(min=0, max=50))
    }


# Class list
classes = [{'subject_name': 'computer science', 'class_name': 'Introduction to Computer Science', 'class_id': ' COMPSCI 101'}, {'subject_name': 'computer science', 'class_name': 'Data Structures and Algorithms', 'class_id': 'COMPSCI 201'},
{'subject_name': 'computer science', 'class_name': 'Discrete Math for Computer Science', 'class_id': 'COMPSCI 230'}, {'subject_name': 'computer science', 'class_name': 'Computer Architecture', 'class_id': 'COMPSCI 250'},
{'subject_name': 'electrical and computer engineering', 'class_name': 'Computer Architecture', 'class_id': 'ECE 250'},
{'subject_name': 'computer science', 'class_name': 'Introduction to Operating Systems', 'class_id': 'COMPSCI 310'}, {'subject_name': 'computer science', 'class_name': 'Introduction to Database Systems', 'class_id': 'COMPSCI 316'},
{'subject_name': 'computer science', 'class_name': 'Introduction to the Design and Analysis of Algorithms', 'class_id': 'COMPSCI 330'},
{'subject_name': 'math', 'class_name': 'Laboratory Calculus I', 'class_id': 'MATH 111'}, {'subject_name': 'math', 'class_name': 'Laboratory Calculus II', 'class_id': 'MATH 112'},
{'subject_name': 'math', 'class_name': 'Introductory Calculus II', 'class_id': 'MATH 122'}, {'subject_name': 'math', 'class_name': 'Multivariable Calculus', 'class_id': 'MATH 212'},
{'subject_name': 'math', 'class_name': 'Linear Algebra and Differential Equations', 'class_id': 'MATH 216'}, {'subject_name': 'math', 'class_name': 'Linear Algebra and Applications', 'class_id': 'MATH 221'}, {'subject_name': 'math', 'class_name': 'Ordinary and Partial Differential Equations', 'class_id': 'MATH 353'},
{'subject_name': 'math', 'class_name': 'Introduction to Abstract Algebra', 'class_id': 'MATH 401'}, {'subject_name': 'math', 'class_name': 'Introduction to Real Analysis', 'class_id': 'MATH 431'},
{'subject_name': 'math', 'class_name': 'Real Analysis I', 'class_id': 'MATH 531'}, {'subject_name': 'math', 'class_name': 'Probability', 'class_id': 'MATH 230'},
{'subject_name': 'statistics', 'class_name': 'Data Analysis and Statistical Inference', 'class_id': 'STA 101'}, {'subject_name': 'statistics', 'class_name': 'Introduction to Data Science and Statistical Thinking', 'class_id': 'STA 199'},
{'subject_name': 'statistics', 'class_name': 'Probability', 'class_id': 'STA 230'}, {'subject_name': 'statistics', 'class_name': 'Statistics', 'class_id': 'STA 250'}, {'subject_name': 'economics', 'class_name': 'Economic Principles', 'class_id': 'ECON 101'},
{'subject_name': 'economics', 'class_name': 'Intermediate Microeconomics I', 'class_id': 'ECON 201'}, {'subject_name': 'economics', 'class_name': 'Intermediate Microeconomics II', 'class_id': 'ECON 205'},
{'subject_name': 'economics', 'class_name': 'Introduction to Econometrics', 'class_id': 'ECON 208'}, {'subject_name': 'economics', 'class_name': 'Intermediate Macroeconomics', 'class_id': 'ECON 210'},
{'subject_name': 'economics', 'class_name': 'Asset Pricing & Risk Management', 'class_id': 'ECON 372'}, {'subject_name': 'spanish', 'class_name': 'Elementary Spanish 1', 'class_id': 'SPANISH 101'},
{'subject_name': 'spanish', 'class_name': 'Elementary Spanish 2', 'class_id': 'SPANISH 102'}, {'subject_name': 'spanish', 'class_name': 'Intermediate Spanish', 'class_id': 'SPANISH 203'},
{'subject_name': 'spanish', 'class_name': 'Advanced Intermediate Spanish', 'class_id': 'SPANISH 204'}, {'subject_name': 'spanish', 'class_name': 'Advanced Spanish Writing', 'class_id': 'SPANISH 301'},
{'subject_name': 'french', 'class_name': 'Elementary French 1', 'class_id': 'FRENCH 101'}, {'subject_name': 'french', 'class_name': 'Elementary French 2', 'class_id': 'FRENCH 102'},
{'subject_name': 'french', 'class_name': 'Intermediate French Language and Culture', 'class_id': 'FRENCH 203'}, {'subject_name': 'french', 'class_name': 'Advanced Intermediate French Language and Culture', 'class_id': 'FRENCH 204'},
{'subject_name': 'chemistry', 'class_name': 'Core Conecpts in Chemistry', 'class_id': 'CHEM 101'}, {'subject_name': 'chemistry', 'class_name': 'Organic Chemistry I', 'class_id': 'CHEM 201'}, {'subject_name': 'chemistry', 'class_name': 'Organic Chemistry II', 'class_id': 'CHEM 202'},
{'subject_name': 'biology', 'class_name': 'Gateway to Biology: Molecular Biology', 'class_id': 'BIOLOGY 201'}, {'subject_name': 'biology', 'class_name': 'Gateway to Biology: Genetics and Evolution', 'class_id': 'BIOLOGY 202'},
{'subject_name': 'physics', 'class_name': 'General Physics I', 'class_id': 'PHYSICS 141'}, {'subject_name': 'physics', 'class_name': 'General Physics II', 'class_id': 'PHYSICS 142'},
{'subject_name': 'physics', 'class_name': 'Introductory Mechanics', 'class_id': 'PHYSICS 151'}, {'subject_name': 'physics', 'class_name': 'Introductory Electricity, Magnetism, and Optics', 'class_id': 'PHYSICS 152'}]


# Class ids
def get_class_ids():
    class_ids = []
    for c in classes:
        class_ids.append(c['class_id'])
    return class_ids


# Classes tuttees need help in
needs_help_with = {}
for t in list(tuttees.values()):
    needs_help_with[t['user_id']] = {'user_id': t['user_id'], 'classes': random.sample(get_class_ids(), randint(1, 5))}


# Classes tutors can help with
can_tutor_in = {}
for t in list(tutors.values()):
    subjects = random.sample(get_class_ids(), randint(1, 5))
    experience = {}
    for s in subjects:
        experience[s] = {'subject': s, 'experience_level': random.choice(['beginner', 'intermediate', 'advanced'])}
    can_tutor_in[t['user_id']] = {'user_id': t['user_id'], 'subjects': experience}


# Create unique session ids
sessionids = []
sessions = {}

def create_session_id():
    sid = randint(0, 999999)
    if sid in sessionids:
        create_user_id()
    sessionids.append(sid)
    return sid


# Ensure sessions are only between tuttees and tutors who have common classes
def choose_tuttee(tid, booked):
    if booked == False:
        return
    potential_tuttees = []
    for o in list(needs_help_with.values()):
        if (set(o['classes']) & set(can_tutor_in[tid]['subjects'].keys())):
            potential_tuttees.append(o['user_id'])
    return random.choice(potential_tuttees)


# Create 500 session
for i in range(500):
    booked = random.choice([True, False])
    tutor = random.choice(list(tutors.values()))
    sid = create_session_id()
    sessions[sid] = {
        'session_id': sid,
        'zoom_link': user.numerify(text='https://us02web.zoom.us/j/###########?'),
        'day': user.future_date(end_date='+30d', tzinfo=None),
        'time': user.time(),
        'price': tutor['hourly_rate'],
        'booked': booked,
        'tutorsin': tutor['user_id'],
        'gets_help_in': choose_tuttee(tutor['user_id'], booked)
    }
