CREATE DATABASE sql_practice;

CREATE TABLE students (
    id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

INSERT INTO students (id, name, age, city)
VALUES
(1, 'rahul', 20, 'Jaipur'),
(2, 'priya', 21, 'delhi'),
(3, 'Aman', 19, 'mumbai'),
(4, 'mukul', 34, 'Dubai'),
(5, 'rakesh', 23, 'bengluru'),
(6, 'sumit', 26, 'lakhnow'),
(7, 'vikas', 23, 'jaipur'),
(8, 'harish', 20, 'dehradun'),
(9, 'subhash', 25, 'pune'),
(10, 'ritika', 24, 'gujraat');

SELECT * FROM students;

UPDATE students
SET city = 'jaipur'
WHERE city = 'Jaipur';

DELETE FROM students
WHERE id = 10;