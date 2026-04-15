-- practice problems
use xyz_company;
create table children(
student_id INT auto_increment PRIMARY KEY ,
name VARCHAR(50),
city VARCHAR(50),
course VARCHAR(50),
marks INT
);

INSERT INTO children (student_id, name, city, course, marks) VALUES
(1, 'Aditi', 'Delhi', 'B.Tech', 85),
(2, 'Rohan', 'Mumbai', 'B.Sc', 78),
(3, 'Priya', 'Delhi', 'B.Tech', 92),
(4, 'Arjun', 'Chennai', 'B.Com', 66),
(5, 'Sneha', 'Mumbai', 'B.Sc', 81),
(6, 'Neha', 'Delhi', 'B.Tech', 75),
(7, 'Karan', 'Chennai', 'B.Com', 88),
(8, 'Meera', 'Delhi', 'B.Sc', 90),
(9, 'Aman', 'Mumbai', 'B.Com', 60),
(10, 'Riya', 'Chennai', 'B.Tech', 73);

-- Find total students in each city.
SELECT city ,COUNT(*) AS total_students FROM children GROUP BY city ;

-- Find the average marks of each course.
SELECT course , AVG(marks) AS avg_marks From children GROUP BY course;

-- Find the highest marks in each city.
SELECT city , MAX(MARKS) AS highest_marks FROM children GROUP BY city;

-- Find the number of students in each course who scored above 80.
SELECT course ,COUNT(name) AS number_of_students FROM children WHERE marks>80 GROUP BY course;

-- Find total marks obtained by students from each city.
SELECT city, SUM(MARKS) AS total_marks FROM children GROUP BY city; 

-- Display all students sorted by marks (highest first).
SELECT name,marks FROM children  ORDER BY marks DESC;

-- List students sorted by city name (alphabetically).
SELECT name,city FROM children ORDER BY city; 

-- Show all students sorted by course first, then by marks (highest first).
SELECT name,course,marks FROM children ORDER BY course , marks DESC;

-- Find average marks per city and show the result with highest average first.
SELECT city , AVG(marks) AS avg_marks FROM children GROUP BY city ORDER BY avg_marks DESC;

-- Find number of students in each course, ordered from most to least students.
SELECT course, COUNT(name) AS number_of_students FROM children GROUP BY course ORDER BY number_of_students DESC;

-- “Find students whose marks are above the average marks.”-- 
SELECT name, marks
FROM students
WHERE marks > (SELECT AVG(marks) FROM students);


-- “Find students whose marks are above the average of their own class.”-- 

SELECT s1.name, s1.marks
FROM students s1
WHERE s1.marks >
    (SELECT AVG(s2.marks)
     FROM students s2
     WHERE s2.class = s1.class);


CREATE INDEX idx_name ON children(name);
select * from children;
SHOW INDEX FROM children;

