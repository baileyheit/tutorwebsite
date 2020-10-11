DROP DATABASE IF EXISTS TutorProject;
CREATE DATABASE TutorProject;
USE TutorProject;

CREATE TABLE Users(
user_id VARCHAR(50) NOT NULL PRIMARY KEY,
user_name VARCHAR(50) NOT NULL,
location VARCHAR(50) NOT NULL,
school VARCHAR(50) NOT NULL,
age integer NOT NULL,
phone_number VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
address VARCHAR(50) NOT NULL,
venmo VARCHAR(50) NOT NULL,
bio VARCHAR(500) NOT NULL
);

CREATE TABLE Tutees(
phone_number VARCHAR(50) NOT NULL REFERENCES Users(phone_number),
address VARCHAR(200) NOT NULL REFERENCES Users(address),
user_name VARCHAR(50) NOT NULL REFERENCES Users(user_name),
user_id VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES Users(user_id),
location VARCHAR(50) NOT NULL REFERENCES Users(location),
school VARCHAR(50) NOT NULL REFERENCES Users(school),
age integer NOT NULL REFERENCES Users(age),
email VARCHAR(50) NOT NULL REFERENCES Users(email),
venmo VARCHAR(50) NOT NULL REFERENCES Users(venmo),
bio VARCHAR(500) NOT NULL REFERENCES Users(bio),
price_range VARCHAR(50) NOT NULL
);

CREATE TABLE Tutors(
phone_number VARCHAR(50) NOT NULL REFERENCES Users(phone_number),
address VARCHAR(200) NOT NULL REFERENCES Users(address),
user_name VARCHAR(50) NOT NULL REFERENCES Users(user_name),
user_id VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES Users(user_id),
location VARCHAR(50) NOT NULL REFERENCES Users(location),
school VARCHAR(50) NOT NULL REFERENCES Users(school),
age integer NOT NULL REFERENCES Users(age),
email VARCHAR(50) NOT NULL REFERENCES Users(email),
venmo VARCHAR(50) NOT NULL REFERENCES Users(venmo),
bio VARCHAR(500) NOT NULL REFERENCES Users(bio),
rating float NOT NULL,
hourly_rate VARCHAR(50) NOT NULL,
grade VARCHAR(50) NOT NULL
);

CREATE TABLE Session(
session_id VARCHAR(50) NOT NULL PRIMARY KEY,
zoom_link VARCHAR(100) NOT NULL,
session_day VARCHAR(50) NOT NULL,
session_time VARCHAR(50) NOT NULL,
price float NOT NULL,
booked VARCHAR(100) NOT NULL
);

CREATE TABLE Classes(
class_id VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES CanTutorIn(class_id), 
subject_name VARCHAR(50) NOT NULL,
class_name VARCHAR(50) NOT NULL
);

CREATE TABLE Cart(
user_id VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES Tutees(user_id),
user_name VARCHAR(50) NOT NULL REFERENCES Tutees(user_name),
location VARCHAR(50) NOT NULL REFERENCES Tutees(location),
school VARCHAR(50) NOT NULL REFERENCES Tutees(school),
age integer NOT NULL REFERENCES Tutees(age),
phone_number VARCHAR(50) NOT NULL REFERENCES Tutees(phone_number),
email VARCHAR(50) NOT NULL REFERENCES Tutees(email),
address VARCHAR (50) NOT NULL REFERENCES Tutees(address),
venmo VARCHAR(50) NOT NULL REFERENCES Tutees(venmo),
bio VARCHAR(150) NOT NULL REFERENCES Tutees(bio),
price_range VARCHAR(50) NOT NULL REFERENCES Tutees(price_range),
zoom_link VARCHAR(50) NOT NULL REFERENCES Session(zoom_link),
session_day VARCHAR(50) NOT NULL REFERENCES Session(session_day),
session_time VARCHAR(50) NOT NULL REFERENCES Session(session_time),
price integer NOT NULL REFERENCES Session(price),
booked VARCHAR(50) NOT NULL REFERENCES Session(booked)
);

CREATE TABLE NeedsHelpWith(
user_id VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES Tutees(user_id),
class_id VARCHAR(50) NOT NULL REFERENCES Classes(class_id)
);

CREATE TABLE CanTutorIn(
user_id VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES Tutors(user_id),
class_id VARCHAR(50) NOT NULL, 
expertise_lvl VARCHAR(50) NOT NULL
);

CREATE TABLE GivesRating(
user_id VARCHAR(50) NOT NULL REFERENCES Tutees(user_id),
rating_comment VARCHAR(50) NOT NULL,
rating_num float NOT NULL
);

CREATE TABLE TutorsIn(
zoom_link VARCHAR(50) NOT NULL REFERENCES Session(zoom_link),
user_id VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES Tutors(user_id)
);