select course_lessons.id
from course_lessons
left join orders_courses
on
    orders_courses.course_id = course_lessons.course_id
left join orders
on
    orders.id = orders_courses.order_id
where orders.created_at > '01-01-2023' and orders.created_at <= '31-01-2023'