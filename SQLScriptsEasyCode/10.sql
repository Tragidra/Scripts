select count(distinct course_lessons_visits.id) from course_lessons_visits
join orders_courses on orders_courses.order_id = course_lessons_visits.order_id
join course_lessons on course_lessons.id = course_lessons_visits.lesson_id
where course_lessons_visits.order_id = 1164 and course_lessons.date_start < '17.01.2023' and course_lessons.course_id = 71