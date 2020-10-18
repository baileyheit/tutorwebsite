import faker
from faker import Factory
import random
from random import randint
import uuid
import mysql.connector

cnx = mysql.connector.connect(user='root', database='TutorProject')
cursor = cnx.cursor()

user = Factory.create()
id = uuid.uuid1()

users = {}
tutors = {}
tutees = {}
cart = {}
sessions = {}

can_tutor_in = {}
needs_help_with = {}
tutors_in = {}
gets_help_in = {}
for_help_in = {}
gives_rating = {}


# Create phone numbers: xxx-xxx-xxxx
def create_digits(n):
    number = ''
    for i in range(n):
        number += str(randint(0, 9))
    return int(number)


# Create 1000 tutors
for i in range(1000):
    uid = id.int
    tutors[uid] = {
        'phone_number': create_digits(10),
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
        'hourly_rate': round(user.random_int(min=0, max=50) + create_digits(2)/100, 2),
        'grade': random.choice(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']), 
    }

    users[uid] = tutors[uid]


# Create 1000 tutees
for i in range(1000):
    uid = id.int
    tutees[uid] = {
        'phone_number': create_digits(10),
        'address': user.address(),
        'name': user.name(),
        'user_id': uid,
        'location': random.choice(['remote', 'in person']),
        'school': random.choice(['trinity', 'pratt']),
        'age': user.random_int(min=17, max=24, step=1),
        'email': user.free_email(),
        'venmo': '@' + user.user_name(),
        'bio': user.text(),
        'price_range': round(user.random_int(min=0, max=50) + create_digits(2)/100, 2),
    }

    cart[uid] = {
        'user_id': uid,
        'sessions': None
    }

    users[uid] = tutees[uid]


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
class_ids = ['COMPSCI 101', 'COMPSCI 201', 'COMPSCI 230', 'COMPSCI 250', 'ECE 250', 'COMPSCI 310', 'COMPSCI 316', 'COMPSCI 330', 'MATH 111', 'MATH 122', 'MATH 212',
'MATH 216', 'MATH 221', 'MATH 353', 'MATH 401', 'MATH 431', 'MATH 531', 'MATH 230','STA 101', 'STA 199', 'STA 230', 'STA 250', 'ECON 101', 'ECON 201', 'ECON 205', 
'ECON 208', 'ECON 210', 'ECON 372', 'SPANISH 101', 'SPANISH 102', 'SPANISH 203', 'SPANISH 204', 'SPANISH 301', 'FRENCH 101', 'FRENCH 102', 'FRENCH 203', 'FRENCH 204',
'CHEM 101', 'CHEM 201', 'CHEM 202', 'BIOLOGY 201', 'BIOLOGY 202', 'PHYSICS 141', 'PHYSICS 142', 'PHYSICS 151', 'PHYSICS 152']


# Classes tutees need help in
for t in list(tutees.values()):
    needs_help_with[t['user_id']] = {'user_id': t['user_id'], 'subjects': random.sample(class_ids, randint(1, 5))}


# Classes tutors can help with
for t in list(tutors.values()):
    classes = random.sample(class_ids, randint(1, 5))
    experience = {}
    for c in classes:
        experience[c] = {'subject': c, 'experience_level': random.choice(['beginner', 'intermediate', 'advanced'])}
    can_tutor_in[t['user_id']] = {'user_id': t['user_id'], 'subject': experience}


# Ensure sessions are only between tutees and tutors who have common classes
def choose_tutee(tid):
    potential_tutees = []
    for o in list(needs_help_with.values()):
        matches = set(o['subjects']) & set(can_tutor_in[tid]['subject'].keys())
        if matches:
            potential_tutees.append({'user_id': o['user_id'], 'subject': random.choice(list(matches))})
    if potential_tutees and random.choice([True, False]):
        return random.choice(potential_tutees)
    return {'user_id': None, 'subject': None}


# Create 500 sessions
for i in range(500):
    tutor = random.choice(list(tutors.values()))
    tutor_uid = tutor['user_id']
    tutee = choose_tutee(tutor_uid)
    tutee_uid = tutee['user_id']
    subject = tutee['subject']
    if tutee_uid is not None:
        booked = True
    else:
        booked = False
    sid = id.int

    sessions[sid] = {
        'session_id': sid,
        'zoom_link': user.numerify(text='https://us02web.zoom.us/j/###########?'),
        'day': user.future_date(end_date='+30d', tzinfo=None),
        'time': user.time(),
        'price': tutor['hourly_rate'],
        'booked': booked,
        'tutor': tutor_uid,
        'tutee': tutee_uid
    }

    for_help_in[sid] = {
        'session': sid,
        'class': subject
    }

    if not sessions[sid]['booked']:
        continue
    
    # Add to tutors_in
    if uid in tutors_in.keys():
        if subject not in tutors_in[uid]['subjects']:
            tutors_in[uid]['subjects'].append(subject)
    else:
        tutors_in[uid] = {
            'user_id': uid,
            'subjects': [subject]
        }
    
    # Add to gets_help_in
    if tutee_uid in gets_help_in.keys():
        if subject not in gets_help_in[tutee_uid]:
            gets_help_in[tutee_uid]['subjects'].append(subject)
    else:
        gets_help_in[tutee_uid] = {
            'user_id': tutee_uid,
            'subjects': [subject]
        }
    
    # Add to cart
    if cart[tutee_uid]['sessions']:
        cart[tutee_uid]['sessions'].append(sid)
    else:
        cart[tutee_uid] = {
            'user_id': tutee_uid,
            'sessions': [sid]
        }
    
    # Give a rating
    if random.choice([True, False]):
        gives_rating[tutor_uid] = {
            'tutor': tutor_uid,
            'tutee': tutee_uid,
            'comment': user.text(),
            'rating': randint(1, 5)
        }