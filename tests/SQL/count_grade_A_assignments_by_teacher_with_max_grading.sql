-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*) AS GradeCount
FROM assignments
JOIN teachers on assignments.teacher_id = teachers.id
WHERE assignments.grade = 'A'
GROUP BY teachers.id
ORDER BY COUNT(*) DESC
LIMIT 1;