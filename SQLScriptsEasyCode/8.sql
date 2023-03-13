select count(*) from course_lessons_visits
join course_lessons on course_lessons.id = course_lessons_visits.lesson_id
join orders_fields_values on orders_fields_values.order_id = course_lessons_visits.order_id
where course_lessons.date_start >= '01.02.2023' and course_lessons.date_start < '01.03.2023' and (orders_fields_values.field_id = 1 and orders_fields_values.value <> '34') and (orders_fields_values.field_id = 1 and orders_fields_values.value <> '32') and (orders_fields_values.field_id = 1 and orders_fields_values.value <> '18')
