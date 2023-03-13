select * from courses
join course_lessons
on course_lessons.course_id = courses.id
join users
on users.id = course_lessons.teacher_id
where course_id = 22