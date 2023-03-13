select count(customers.*) from customers
left join customers_dialogs on customers_dialogs.customer_id = customers.id
where customers_dialogs.customer_id is null