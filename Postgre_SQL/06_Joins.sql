--                                     creating table

CREATE TABLE marks (
    student_id INT,
    subject VARCHAR(50),
    marks INT
);

INSERT INTO marks (student_id, subject, marks)
VALUES
(1, 'math', 85),
(2, 'English', 90),
(3, 'Science', 78),
(4, 'Math', 88),
(11, 'English', 72);

SELECT * FROM marks;

--                              INNER JOIN

SELECT students.id, students.name, marks.subject, marks.marks
FROM students
INNER JOIN marks
ON students.id = marks.student_id;

SELECT students.name, marks.marks
FROM students
INNER JOIN marks
ON students.id = marks.student_id;

--                              LEFT JOIN

SELECT students.name, marks.subject, marks.marks
FROM students
LEFT JOIN marks
ON students.id = marks.student_id;

--                             RIGHT JOIN

SELECT students.name, marks.student_id, marks.subject, marks.marks
FROM students
RIGHT JOIN marks
ON students.id = marks.student_id;

--                            FULL OUTHER JOIN

SELECT students.name, marks.student_id,
       marks.subject, marks.marks
FROM students
FULL OUTER JOIN marks
ON students.id = marks.student_id;

--                           CROSS JOIN

SELECT students.name, marks.subject, marks.marks
FROM students
CROSS JOIN marks;

--                           SELF JOIN

SELECT 
    s1.name AS student1,
    s2.name AS student2,
    S1.city
FROM students s1
JOIN students s2
    ON s1.city = s2.city
    AND s1.id < s2.id;
