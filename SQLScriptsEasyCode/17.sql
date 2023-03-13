select users.name, count(course_lessons_visits.id) as January
from course_lessons_visits
left join course_lessons
on course_lessons.id = course_lessons_visits.lesson_id
left join users
on users.id = course_lessons.teacher_id
where course_lessons_visits.created_at <= '31.01.2023' and course_lessons_visits.created_at >= '01.01.2023'
group by users.id