select count(orders.*) from orders
left join orders_products on orders_products.order_id <> orders.id
