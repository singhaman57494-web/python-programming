--                                              SQL function

SELECT COUNT(*) 
FROM students;

SELECT COUNT(*) AS total_students
FROM students;

SELECT SUM(AGE) AS total_age
FROM students;

SELECT AVG(age) AS average_age
FROM students;

SELECT
    MIN(age) AS minimum_age,
    MAX(age) AS maximum_age
FROM students;

--                    all perform 1 query

SELECT 
    COUNT(*) AS total_student,
    SUM(age) AS total_age,
    AVG(age) AS average_age,
    MIN(age) as min_age,
    MAX(age) AS max_age
FROM students;
--                        GROUP BY

SELECT 
    city,
    COUNT(*) AS total_students
FROM students
GROUP BY city
ORDER BY city;

--                      HAVING 

SELECT 
    city,
    COUNT(*) AS total_students
FROM students
GROUP BY city
HAVING COUNT(*) >= 2;

--                          ROUND

SELECT ROUND(AVG(age), 1) AS average_age
FROM students;

SELECT ROUND(AVG(age), 2) AS average_age
FROM students;

--                        UPPER

SELECT UPPER(name) AS student_name
FROM students;

--                        LOWER

SELECT LOWER(name) AS student_name
FROM students;

--                         LENGTH

SELECT name,
    LENGTH(name) AS name_length
FROM students;

--                          CONCAT

SELECT CONCAT(name, ' ', city ) AS student_info
FROM students;

--                             TRIM

SELECT TRIM('    rahul    ') AS clean_name;

--                                COALESCE

SELECT 
    name, 
    COALESCE(city, 'unknown') AS city_name
FROM students;

SELECT 
    name,
    REPLACE(CITY, 'jaipur', 'Jodhpur') AS updated_city
FROM students;

SELECT 
    name, 
    SUBSTRING(name FROM 1 FOR 3) AS short_name
FROM students;

SELECT ABS(-42) AS result;

SELECT CEIL(23.2) AS result;

SELECT FLOOR(23.8) AS result;

SELECT MOD(10, 3) AS result;

SELECT POWER(2, 3) AS result;

SELECT NOW() AS current_time;

SELECT CURRENT_DATE AS today;