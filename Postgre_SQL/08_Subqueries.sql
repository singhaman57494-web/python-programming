--                         subqueries in SQL

select name, age
FROM students
WHERE age > (
    SELECT AVG(age)
    FROM students
);

SELECT * FROM students;

SELECT name
FROM students
WHERE id IN (
    SELECT student_id
    FROM marks
);


SELECT name
FROM students
WHERE id NOT IN (
    SELECT student_id
    From marks
);

SELECT name, age
FROM students
WHERE age = (
    SELECT MAX(age)
    FROM students
);