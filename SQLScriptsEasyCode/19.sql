select customers.from_id from customers
left join orders on orders.customer_id = customers.id
where from_id <> '0' and orders.created_at > '06-10-2022' and orders.created_at <= '06-03-2023' and customers.customers_channel_id = 2 or customers.customers_channel_id = 3 or customers.customers_channel_id = 4 or customers.customers_channel_id = 5 or customers.customers_channel_id = 6 or customers.customers_channel_id = 8 or customers.customers_channel_id = 10 or customers.customers_channel_id = 12 or customers.customers_channel_id = 13 or customers.customers_channel_id = 14 or customers.customers_channel_id = 15 or customers.customers_channel_id = 16 or customers.customers_channel_id = 20 or customers.customers_channel_id = 23 or customers.customers_channel_id = 24 or customers.customers_channel_id = 25 or customers.customers_channel_id = 26 or customers.customers_channel_id = 27 or customers.customers_channel_id = 28 or customers.customers_channel_id = 29 or customers.customers_channel_id = 30 or customers.customers_channel_id = 31 or customers.customers_channel_id = 32 or customers.customers_channel_id = 33 or customers.customers_channel_id = 34 or customers.customers_channel_id = 35 or customers.customers_channel_id = 36