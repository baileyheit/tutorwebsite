DROP DATABASE IF EXISTS TutorProject;
CREATE DATABASE TutorProject;
USE TutorProject;

CREATE TABLE tblUsers(
user_id VARCHAR(50) NOT NULL,
user_name VARCHAR(50) NOT NULL,
location VARCHAR(50),
school VARCHAR(50),
age integer,
phone_num integer,
email VARCHAR(50),
address VARCHAR(50),
venmo VARCHAR(50),
bio VARCHAR(150) 
);

CREATE TABLE tblSession(
zoom_link VARCHAR(100),
day_time DATETIME,
price float,
booked VARCHAR(100)
);

CREATE TABLE tblClasses(
class_id VARCHAR(50),
subject_name VARCHAR(50),
class_name VARCHAR(50)
);

CREATE TABLE tlbCart(
user_id VARCHAR(50),
user_name VARCHAR(50),
location VARCHAR(50),
school VARCHAR(50),
age integer,
phone_num integer,
email VARCHAR(50),
address VARCHAR (50),
venmo VARCHAR(50),
bio VARCHAR(150),
price_range VARCHAR(50),
zoom_link VARCHAR(50),
day_time DATETIME,
price integer,
booked VARCHAR(50)
);

CREATE TABLE tblTutees(
user_id VARCHAR(50),
price_range VARCHAR(50)
);

CREATE TABLE tblTutors(
user_id VARCHAR(50),
rating float,
hourly_rate float
);

CREATE TABLE tblNeedsHelpWith(
user_id VARCHAR(50),
class_id VARCHAR(50)
);

CREATE TABLE tblCanTutorIn(
user_id VARCHAR(50),
class_id VARCHAR(50),
expertise_lvl VARCHAR(50)
);

CREATE TABLE tblGivesRating(
user_id VARCHAR(50),
rating_comment VARCHAR(50),
rating_num float
);

CREATE TABLE tblTutorsIn(
zoom_link VARCHAR(50),
user_id VARCHAR(50)
);
