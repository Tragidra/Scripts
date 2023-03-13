select count(*) from orders
join orders_courses on orders_courses.order_id = orders.id
join course_lessons on course_lessons.course_id = orders_courses.course_id
join orders_fields_values on orders_fields_values.order_id = orders.id
where course_lessons.date_start >= '01.02.2023' and course_lessons.date_start < '01.03.2023' and (orders_fields_values.field_id = 1 and orders_fields_values.value <> '34') and (orders_fields_values.field_id = 1 and orders_fields_values.value <> '32') and (orders_fields_values.field_id = 1 and orders_fields_values.value <> '18')