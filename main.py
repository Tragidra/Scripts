import psycopg2 as psycopg2

con = psycopg2.connect(
  database="lakrul_plattform",
  user="postgres",
  password="astrafaz99",
  host="127.0.0.1",
  port="5432"
)
k = 18
cur = con.cursor()
con.close()