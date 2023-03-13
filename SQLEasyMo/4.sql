SELECT (orders_products_sets.design_file_url)
from orders_products_sets
left join orders_products
on orders_products.id = orders_products_sets.parent_product_id
where orders_products.name = 'Реализм'
limit 1