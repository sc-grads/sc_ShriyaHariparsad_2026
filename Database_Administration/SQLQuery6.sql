use OurFirstDatabase
go

SELECT * FROM dbo.student
GO

SELECT * FROM dbo.course

SELECT s.RollNo,s.StudentName,c.CourseID FROM student s
join course c
on s.RollNo = c.RollNO

SELECT s.RollNo,s.StudentName,c.CourseID FROM student s
left join course c
on s.RollNo = c.RollNO

SELECT s.RollNo,s.StudentName,c.CourseID FROM student s
right join course c
on s.RollNo = c.RollNO

SELECT s.RollNo,s.StudentName,c.CourseID FROM student s
full join course c
on s.RollNo = c.RollNO