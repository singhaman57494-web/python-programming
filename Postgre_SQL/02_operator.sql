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
