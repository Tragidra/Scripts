select customers.from_id from customers
left join orders on orders.customer_id = customers.id
left join orders_fields_values on orders_fields_values.order_id = orders.id
where customers.utm_source = 'vk_easycode' and orders_fields_values.field_id = 8 and orders_fields_values.value is not null