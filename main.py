import psycopg2 as psycopg2

con = psycopg2.connect(
  database="schooleasy",
  user="schooleasyusr",
  password="*",
  host="rc1a-o0igrrn40untvtoa.mdb.yandexcloud.net",
  port="6432"
)
k = 18
cur = con.cursor()
cur.execute(
  "SELECT id from courses where disbanded=false")
n = cur.fetchall()
print(n[0][0])
for i in range(len(n)):
  cur.execute("SELECT id,course_id,date_start from course_lessons where course_id=%s and date_start is not null ORDER BY date_start", [n[i][0]])
  a = cur.fetchall()
  print(len(a))
  for j in range(1, len(a)+1):
    cur.execute('''UPDATE course_lessons set lesson_number = %s WHERE id = %s''', (j, a[j-1][0]))
con.commit()
con.close()