--                     CASE WHEN

SELECT
    name, 
    age,
    CASE
        WHEN age >= 20 THEN 'Adult'
        ELSE 'minor'
    END AS age_group
FROM students;

SELECT 
    name,
    age,
    CASE
        WHEN age < 20 THEN 'Young'
        WHEN age <= 25 THEN 'Adult'
        ELSE 'older'
    END AS age_group
FROM students;

SELECT 
    name,
    age,
    CASE
        WHEN age < 20 THEN 'young'
        WHEN age <= 25 THEN 'Adult'
        ELSE 'older'
    END AS age_group
FROM students
ORDER BY age DESC;

SELECT 
    name,
    age,
    CASE
        WHEN age >= 20 AND age <= 25 THEN '20-25 Age group'
        ELSE 'Other Age group'
    END AS age_group
FROM students
ORDER BY age_group DESC;