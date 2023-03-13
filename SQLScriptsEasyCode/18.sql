select sum(sum) from customers_payment_history where success = true and created_at >= '2023-02-13 00:00:00' and created_at <= '2023-02-13 23:59:00'
