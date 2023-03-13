select users.name from orders o
left join users on o.teacher_id = users.id
left join basket_fields_values bfv on bfv.order_id = o.id
where bfv.field_id = 4
and o.department_id = 1
group by users.name, bfv.value