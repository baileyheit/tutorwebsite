DROP DATABASE IF EXISTS TutorProject;
CREATE DATABASE TutorProject;
USE TutorProject;

CREATE TABLE tblUsers(
user_id VARCHAR(50) NOT NULL,
user_name VARCHAR(50),
location VARCHAR(50),
school VARCHAR(50),
age integer,
phone_number VARCHAR(50),
email VARCHAR(50),
address VARCHAR(50),
venmo VARCHAR(50),
bio VARCHAR(500) 
);

CREATE TABLE tblSession(
session_id VARCHAR(50) NOT NULL,
zoom_link VARCHAR(100),
session_day VARCHAR(50),
session_time VARCHAR(50),
price float,
booked VARCHAR(100),
tutorsin VARCHAR(50),
gets_help_in VARCHAR(50)
);

CREATE TABLE tblClasses(
class_id VARCHAR(50) NOT NULL,
subject_name VARCHAR(50),
class_name VARCHAR(50)
);

CREATE TABLE tblCart(
user_id VARCHAR(50) NOT NULL,
user_name VARCHAR(50),
location VARCHAR(50),
school VARCHAR(50),
age integer,
phone_number VARCHAR(50),
email VARCHAR(50),
address VARCHAR (50),
venmo VARCHAR(50),
bio VARCHAR(150),
price_range VARCHAR(50),
zoom_link VARCHAR(50),
session_day VARCHAR(50),
session_time VARCHAR(50),
price integer,
booked VARCHAR(50)
);

CREATE TABLE tblTutees(
user_id VARCHAR(50) NOT NULL,
user_name VARCHAR(50),
location VARCHAR(50),
school VARCHAR(50),
age integer,
phone_number VARCHAR(50),
email VARCHAR(50),
address VARCHAR(50),
venmo VARCHAR(50),
bio VARCHAR(500),
price_range VARCHAR(50)
);

CREATE TABLE tblTutors(
user_id VARCHAR(50) NOT NULL,
user_name VARCHAR(50),
location VARCHAR(50),
school VARCHAR(50),
age integer,
phone_number VARCHAR(50),
email VARCHAR(50),
address VARCHAR(50),
venmo VARCHAR(50),
bio VARCHAR(500),
rating float,
grade VARCHAR(50),
hourly_rate VARCHAR(50)
);

CREATE TABLE tblNeedsHelpWith(
user_id VARCHAR(50) NOT NULL,
class_id VARCHAR(50)
);

CREATE TABLE tblCanTutorIn(
user_id VARCHAR(50) NOT NULL,
class_id VARCHAR(50),
expertise_lvl VARCHAR(50)
);

CREATE TABLE tblGivesRating(
user_id VARCHAR(50) NOT NULL,
rating_comment VARCHAR(50),
rating_num float
);

CREATE TABLE tblTutorsIn(
zoom_link VARCHAR(50),
user_id VARCHAR(50) NOT NULL
);
