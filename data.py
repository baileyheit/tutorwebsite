import faker
from faker import Factory
import random
from random import randint
import uuid
from datetime import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', database='TutorProject')
cursor = cnx.cursor()

user = Factory.create()

users = {}
cart = {}
sessions = {}
classes = {}
ratings = {}

uids = []
usernames = []
emails = []
sids = []
rids = []
cids = []


# Create phone numbers: xxx-xxx-xxxx
def create_digits(n):
    number = ''
    for i in range(n):
        number += str(randint(0, 9))
    return int(number)


# Create 1000 users
for i in range(1000):
    username = user.simple_profile()['username']
    while username in usernames:
        username = user.simple_profile()['username']
    usernames.append(username)
    email = user.free_email()
    while email in emails:
        email = user.free_email()
    emails.append(email)
    uid = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1 & (1<<32)-1 
    while uid in uids:
        uid = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1
    uids.append(uid)
    
    users[uid] = {
        'id': uid,
        'username': username,
        'email': email,
        'password_hash': str(create_digits(8)),
        'name': user.name(),
        'phone_number': create_digits(10),
        'school': random.choice(['trinity', 'pratt']),
        'venmo': '@' + username,
        'about_me': user.text(),
        'last_seen': None,
        'rating': None,
        'hourly_rate': None,
        'rating': None,
        'grade': None,
        'price_range': None
    }
    
    choice = randint(0, 3)
    if choice == 1 or choice == 3:
        users[uid]['rating'] = user.random_int(min=1, max=20, step=1)/4.0
        users[uid]['hourly_rate'] = round(user.random_int(min=0, max=50) + create_digits(2)/100, 2)
        users[uid]['grade'] = random.choice(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'])
    if choice == 2 or choice == 3:
        users[uid]['price_range'] = round(user.random_int(min=0, max=50) + create_digits(2)/100, 2)


# Class list
cids = []
for i in range(0, 46):
    cids.append(uuid.uuid4().int & (1<<32)-1 & (1<<32)-1)
classes[cids[0]] = {'subject': 'computer science', 'number': 101, 'class_name': 'Introduction to Computer Science'}
classes[cids[1]] = {'subject': 'computer science', 'number': 201, 'class_name': 'Data Structures and Algorithms'}
classes[cids[2]] = {'subject': 'computer science', 'number': 230, 'class_name': 'Discrete Math for Computer Science'}
classes[cids[3]] = {'subject': 'computer science', 'number': 250, 'class_name': 'Computer Architecture'}
classes[cids[4]] = {'subject': 'electrical and computer engineering', 'number': 250, 'class_name': 'Computer Architecture'}
classes[cids[5]] = {'subject': 'computer science', 'number': 310, 'class_name': 'Introduction to Operating Systems'}
classes[cids[6]] = {'subject': 'computer science', 'number': 316, 'class_name': 'Introduction to Database Systems'}
classes[cids[7]] = {'subject': 'computer science', 'number': 330, 'class_name': 'Introduction to the Design and Analysis of Algorithms'}
classes[cids[8]] = {'subject': 'math', 'number': 111, 'class_name': 'Laboratory Calculus I'}
classes[cids[9]] = {'subject': 'math', 'number': 112, 'class_name': 'Laboratory Calculus II'}
classes[cids[10]] = {'subject': 'math', 'number': 122, 'class_name': 'Introductory Calculus II'}
classes[cids[11]] = {'subject': 'math', 'number': 212, 'class_name': 'Multivariable Calculus'}
classes[cids[12]] = {'subject': 'math', 'number': 216, 'class_name': 'Linear Algebra and Differential Equations'}
classes[cids[12]] = {'subject': 'math', 'number': 221, 'class_name': 'Linear Algebra and Applications'}
classes[cids[13]] = {'subject': 'math', 'number': 353, 'class_name': 'Ordinary and Partial Differential Equations'}
classes[cids[14]] = {'subject': 'math', 'number': 401, 'class_name': 'Introduction to Abstract Algebra'}
classes[cids[15]] = {'subject': 'math', 'number': 431, 'class_name': 'Introduction to Real Analysis'}
classes[cids[16]] = {'subject': 'math', 'number': 531, 'class_name': 'Real Analysis I'}
classes[cids[17]] = {'subject': 'math', 'number': 230, 'class_name': 'Probability'}
classes[cids[18]] = {'subject': 'statistics', 'number': 101, 'class_name': 'Data Analysis and Statistical Inference'}
classes[cids[19]] = {'subject': 'statistics', 'number': 199, 'class_name': 'Introduction to Data Science and Statistics'}
classes[cids[20]] = {'subject': 'statistics', 'number': 230, 'class_name': 'Probability'}
classes[cids[21]] = {'subject': 'statistics', 'number': 250, 'class_name': 'Statistics'}
classes[cids[22]] = {'subject': 'economics', 'number': 101, 'class_name': 'Economic Principles'}
classes[cids[23]] = {'subject': 'economics', 'number': 201, 'class_name': 'Intermediate Microeconomics I'}
classes[cids[24]] = {'subject': 'economics', 'number': 205, 'class_name': 'Intermediate Microeconomics II'}
classes[cids[25]] = {'subject': 'economics', 'number': 208, 'class_name': 'Introduction to Econometrics'}
classes[cids[26]] = {'subject': 'economics', 'number': 210, 'class_name': 'Intermediate Macroeconomics'}
classes[cids[27]] = {'subject': 'economics', 'number': 372, 'class_name': 'Asset Pricing & Risk Management'}
classes[cids[28]] = {'subject': 'spanish', 'number': 101, 'class_name': 'Elementary Spanish 1'}
classes[cids[29]] = {'subject': 'spanish', 'number': 102, 'class_name': 'Elementary Spanish 2'}
classes[cids[30]] = {'subject': 'spanish', 'number': 203, 'class_name': 'Intermediate Spanish'}
classes[cids[31]] = {'subject': 'spanish', 'number': 204, 'class_name': 'Advanced Intermediate Spanish'}
classes[cids[32]] = {'subject': 'spanish', 'number': 301, 'class_name': 'Advanced Spanish Writing'}
classes[cids[33]] = {'subject': 'french', 'number': 101, 'class_name': 'Elementary French 1'}
classes[cids[34]] = {'subject': 'french', 'number': 102, 'class_name': 'Elementary French 2'}
classes[cids[35]] = {'subject': 'french', 'number': 203, 'class_name': 'Intermediate French Language and Culture'}
classes[cids[36]] = {'subject': 'spanish', 'number': 204, 'class_name': 'Advanced Intermediate French Language and Culture'}
classes[cids[37]] = {'subject': 'chemistry', 'number': 101, 'class_name': 'Core Conecpts in Chemistry'}
classes[cids[38]] = {'subject': 'chemistry', 'number': 201, 'class_name': 'Organic Chemistry I'}
classes[cids[39]] = {'subject': 'chemistry', 'number': 202, 'class_name': 'Organic Chemistry II'}
classes[cids[40]] = {'subject': 'chemistry', 'number': 201, 'class_name': 'Gateway to Biology: Molecular Biology'}
classes[cids[41]] = {'subject': 'chemistry', 'number': 202, 'class_name': 'Gateway to Biology: Genetics and Evolution'}
classes[cids[42]] = {'subject': 'physics', 'number': 141, 'class_name': 'General Physics I'}
classes[cids[43]] = {'subject': 'physics', 'number': 142, 'class_name': 'General Physics II'}
classes[cids[44]] = {'subject': 'physics', 'number': 151, 'class_name': 'Introductory Mechanics'}
classes[cids[45]] = {'subject': 'physics', 'number': 152, 'class_name': 'Introductory Electricity, Magnetism, and Optics'}


# Create 500 sessions
for i in range(500):
    tutor = random.choice(list(users.values()))
    tutor_uid = tutor['id']
    tutee = random.choice(list(users.values()))
    if randint(0, 1) == 1:
        tutee_uid = tutee['id']
        booked = True
    else:
        tutee_uid = None
        booked = False
    
    cid = random.choice(list(classes.keys()))
    sid = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1
    while sid in sids:
        sid = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1
    sids.append(sid)

    price = round(user.random_int(min=0, max=50) + create_digits(2)/100, 2)
    if tutor['hourly_rate'] is not None:
        price = tutor['hourly_rate']
    elif booked and tutee['price_range'] is not None:
        price = tutee['hourly_rate']

    sessions[sid] = {
        'session_id': sid,
        'zoom_link': user.numerify(text='https://us02web.zoom.us/j/###########?'),
        'date': user.future_date(end_date='+30d', tzinfo=None),
        'time': user.time(),
        'price': price,
        'booked': booked,
        'tutor': tutor_uid,
        'tutee': tutee_uid,
        'subject': classes[cid]['subject'],
        'class_num': classes[cid]['number']
    }

    if not booked:
        if randint(0, 1) == 1:
            u = random.choice(list(users.values()))['id']
            cid = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1
            while u == tutor_uid:
                u = random.choice(list(users.values()))['id']
            while cid in cids:
                cid = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1
            cids.append(cid)
            cart[cid] = {
                'cart_id': cid,
                'session_id': sid,
                'user': u
            }
        continue
    
    # Give a rating
    if random.choice([True, False]):
        rid = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1
        while rid in rids:
            rid = uuid.uuid4().int & (1<<32)-1 & (1<<32)-1
        rids.append(rid)

        ratings[rid] = {
            'rating_id': rid,
            'tutor': tutor_uid,
            'tutee': tutee_uid,
            'session': sid,
            'subject': classes[cid]['subject'],
            'class_num': classes[cid]['number'],
            'comment': user.text(),
            'rating_num': randint(1, 5)
        }
