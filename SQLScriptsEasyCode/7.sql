select courses.id, count(orders_courses.id) from courses
join course_lessons on course_lessons.id = courses.id
join orders_courses on orders_courses.id = courses.id
join orders_fields_values on orders_fields_values.order_id = orders_courses.order_id
where course_lessons.date_start >= '01.12.2022' and courses.disbanded = false and ((orders_fields_values.field_id = 1 and orders_fields_values.value = '34') or (orders_fields_values.field_id = 1 and orders_fields_values.value = '18') or (orders_fields_values.field_id = 1 and orders_fields_values.value = '32'))
group by courses.id
