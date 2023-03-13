select sum(basket_fields_values.value::numeric)
from basket_fields_values
join orders
on basket_fields_values.order_id = orders.id
where orders.teacher_id = 100 and basket_fields_values.field_id = 4