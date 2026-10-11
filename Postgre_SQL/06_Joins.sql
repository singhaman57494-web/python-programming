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

--                         INNER JOIN

SELECT students.id, students.name, marks.subject, marks.marks
FROM students
INNER JOIN marks
ON students.id = marks.student_id;

SELECT students.name, marks.marks
FROM students
INNER JOIN marks
ON students.id = marks.student_id;