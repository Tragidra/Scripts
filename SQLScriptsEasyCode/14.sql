select * from customers_payment_history
where customers_payment_history.success = true and customers_payment_history.deleted_at is null and customers_payment_history.created_at > '2023-01-01 00:00:00'