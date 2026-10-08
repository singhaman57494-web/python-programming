SELECT version();

CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT
);

SELECT * FROM students;

INSERT INTO students (id, name, age)
VALUES (1, 'Rahul', 20);

INSERT INTO students(id, name, age)
VALUES (2, 'Aman', 21);

INSERT INTO students (id, name, age)
VALUES (3, 'Rohit', 19);

INSERT INTO students (id, name, age)
VALUES (4, 'Vikas', 22);

SELECT * FROM students;


SELECT * FROM students
WHERE name = 'Rahul';

SELECT * FROM students
WHERE age = 20;

SELECT * FROM students
WHERE age = 21;

UPDATE students
SET age = 22
WHERE id  = 2;

SELECT * FROM students
WHERE id = 2;

DELETE FROM students
WHERE id = 3;

SELECT * FROM students;

SELECT COUNT(*)
FROM students;

SELECT COUNT(*)
FROM students
WHERE age = 22;

SELECT SUM(age)
FROM students;

SELECT SUM(age)
FROM students
WHERE age > 20;

SELECT MIN(age)
FROM students;

SELECT MIN(age)
FROM students
WHERE age >= 20;

SELECT MAX(age)
FROM students
WHERE age < 25;