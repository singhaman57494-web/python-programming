--                     operator in postgreSQL


SELECT name, city FROM students
WHERE city = 'jaipur';

select name, city FROM students
WHERE city ILIKE 'jaipur';

SELECT name, age FROM students
WHERE age >= 23;

SELECT name, age FROM students
WHERE age > 20 AND city = 'jaipur';

SELECT name, age FROM students
WHERE age > 20 OR age  < 25;

SELECT name, age FROM students
WHERE age BETWEEN 21 AND 30;


SELECT name, city FROM students
WHERE city IN ('jaipur', 'pune', 'mumbai');

--    check students whose city is missing

SELECT *
FROM students
WHERE city IS NULL;

--     check students whose city is not missing

SELECT *
FROM students
WHERE city IS NOT NULL;

--             DISTINCT: show unique cities

SELECT DISTINCT city
FROM students;

--            DISTINCT WITH MULTIPLE COLUMN

SELECT DISTINCT city, age
FROM students;

--            DISTINCT  with all columns

SELECT DISTINCT *
FROM students;

SELECT *
FROM students
WHERE name LIKE 'r%';

SELECT *
FROM students
WHERE name LIKE '%i';

SELECT *
FROM students
WHERE name LIKE '_a%';

SELECT *
FROM students
WHERE name ILIKE 'R%'