-- BASIC COMMANDS

SHOW TABLES;
SHOW DATABASES;

-- DATABASE CREATION
CREATE DATABASE IF NOT EXISTS test;
USE test;

-- TABLE CREATION

CREATE TABLE IF NOT EXISTS students (
RollNo    INTEGER               NOT NULL PRIMARY KEY,
Name      VARCHAR(20)           NOT NULL,
Gender    CHAR(1),
Marks     INTEGER(11),
DOB       DATE,
Mobile    VARCHAR(25)
);

-- VIEW A TABLE (AND STRUCTURE)

SHOW TABLES;
-- DESCRIBE students;

-- ALTER A TABLE
ALTER TABLE students ADD City CHAR(6) DEFAULT "Delhi";
ALTER TABLE students ADD Passing CHAR(1);
ALTER TABLE students MODIFY Name VARCHAR(25);
ALTER TABLE students MODIFY Marks DECIMAL(3, 1);

DESCRIBE students;

-- ADD DATA TO A TABLE
INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(1, "Raj Kumar", "M", 93, "2008-03-03", "9876543210");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(2, "Priya Sharma", "F", 89, "2007-08-12", "9876543211");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(3, "Amit Verma", "M", 76, "2008-06-22", "9876543212");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(4, "Sneha Iyer", "F", 92, "2007-02-15", "9876543213");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(5, "Anil Gupta", "M", 85, "2008-04-05", "9876543214");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(6, "Neha Patel", "F", 88, "2007-12-25", "9876543215");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(7, "Vikram Singh", "M", 91, "2008-01-11", "9876543216");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(8, "Ritu Mehta", "F", 79, "2008-05-10", "9876543217");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(9, "Harsh Raj", "M", 80, "2007-09-09", "9876543218");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(10, "Simran Kaur", "F", 94, "2008-07-19", "9876543219");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(11, "Nikhil Soni", "M", 78, "2008-02-28", "9876543220");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(12, "Tanuja Joshi", "F", 90, "2007-10-13", "9876543221");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(13, "Shubham Rathi", "M", 87, "2008-03-17", "9876543222");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(14, "Suman Yadav", "F", 82, "2007-11-22", "9876543223");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(15, "Gaurav Mehra", "M", 95, "2008-04-30", "9876543224");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(16, "Ananya Rao", "F", 84, "2007-07-14", "9876543225");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(17, "Karan Kapoor", "M", 88, "2008-09-18", "9876543226");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(18, "Ravi Verma", "M", 91, "2008-12-03", "9876543227");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(19, "Pooja Soni", "F", 80, "2007-05-01", "9876543228");

INSERT INTO students(Rollno, Name, Gender, Marks, DOB, Mobile) 
VALUES(20, "Akash Patel", "M", 86, "2008-08-21", "9876543229");


-- SELECT * FROM students;

-- MOFIDYING DATA IN TABLE
UPDATE students
SET PASSING = "Y"
WHERE MARKS >= 33;

UPDATE students
SET PASSING = "N"
WHERE MARKS < 33;

-- SQL QUERIES

SELECT * FROM students;
SELECT Name, Rollno, DOB, Mobile FROM students
WHERE Passing = "Y";

SELECT DISTINCT DOB AS "Date of Birth" FROM STUDENTS;

-- PATTERN BASED SQL QUERIES

SELECT * FROM students
WHERE Name LIKE "%a_";

SELECT * FROM students
WHERE Name LIKE "_a%";

-- SQL ALIASES
SELECT Name AS "Student Name", Rollno AS "Roll Number"
FROM STUDENTS;

-- SQL ORDERING
SELECT * FROM STUDENTS
ORDER BY Gender DESC, Rollno ASC;

-- DELETE A TABLE

DROP TABLE students;

-- DELETE A DATABASE

DROP test;