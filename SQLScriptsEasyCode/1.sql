create view lessons_income(lesson_id, date_start, total) as
SELECT clv.lesson_id,
       cl.date_start,
       round(sum(bfv.value::numeric / ofv.value::numeric), 2) AS total
FROM course_lessons_visits clv
         LEFT JOIN basket_fields_values bfv ON clv.order_id = bfv.order_id
         LEFT JOIN orders_fields_values ofv ON ofv.order_id = bfv.order_id
         LEFT JOIN course_lessons cl ON cl.id = clv.lesson_id
WHERE bfv.field_id = 6
  AND ofv.field_id = 11
  AND ofv.value::numeric <> 0::numeric
  AND bfv.value::numeric <> 0::numeric
GROUP BY clv.lesson_id, cl.date_start;

alter table lessons_income
    owner to schooleasyusr;