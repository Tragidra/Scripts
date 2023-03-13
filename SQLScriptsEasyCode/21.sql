select customers.from_id from customers
left join orders on orders.customer_id = customers.id
left join orders_fields_values ofv2 on ofv2.order_id = orders.id
where customers.utm_source = 'vk_easycode'
and ofv2.field_id = 1
and ofv2.value::numeric in (10,33,19,35,34)