DROP DATABASE IF EXISTS TutorProject;
CREATE DATABASE TutorProject;
USE TutorProject;

CREATE TABLE Users(
user_id VARCHAR(50) NOT NULL PRIMARY KEY,
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

CREATE TABLE Session(
zoom_link VARCHAR(100) PRIMARY KEY,
day_time DATETIME,
price float,
booked VARCHAR(100)
);

CREATE TABLE Classes(
class_id VARCHAR(50),
subject_name VARCHAR(50),
class_name VARCHAR(50)
);

CREATE TABLE Cart(
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

CREATE TABLE Tutees(
user_id VARCHAR(50),
price_range VARCHAR(50)
);

CREATE TABLE Tutors(
user_id VARCHAR(50),
rating float,
hourly_rate float
);

CREATE TABLE NeedsHelpWith(
user_id VARCHAR(50),
class_id VARCHAR(50)
);

CREATE TABLE CanTutorIn(
user_id VARCHAR(50),
class_id VARCHAR(50),
expertise_lvl VARCHAR(50)
);

CREATE TABLE GivesRating(
user_id VARCHAR(50),
rating_comment VARCHAR(50),
rating_num float
);

CREATE TABLE TutorsIn(
zoom_link VARCHAR(50),
user_id VARCHAR(50)
);