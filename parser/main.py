import psycopg2 as psycopg2
import requests

con = psycopg2.connect(
  database="easymo_db_db",
  user="easymo_db_user",
  password="83jasd8j2AJS2ujsad72",
  host="rc1a-su3030gd5zgpxds4.mdb.yandexcloud.net",
  port="6432"
)

cur = con.cursor()
cur.execute("SELECT design_file_url from orders_products_sets left join orders_products on orders_products.id = orders_products_sets.parent_product_id where orders_products.name = 'Реализм' and orders_products_sets.design_status = 'finish' and orders_products_sets.design_file_url is not null")
a = cur.fetchall()
print(a[0][0])
for i in range(len(a)):
  img_data = requests.get(a[i][0]).content
  with open('downloads\image_name'+str(i)+'.jpg', 'wb') as handler:
      handler.write(img_data)
con.commit()
con.close()
