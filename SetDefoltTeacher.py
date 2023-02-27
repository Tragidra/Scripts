import psycopg2 as psycopg2
import datetime

now = datetime.datetime(2023, 2, 21, 12, 0)
print(now)

con = psycopg2.connect(
    database="schooleasy",
    user="schooleasyusr",
    password="d2uOIqsjsu2nasu7nzx83",
    host="rc1a-o0igrrn40untvtoa.mdb.yandexcloud.net",
    port="6432"
)
cur = con.cursor()
cur.execute("SELECT id from courses ORDER BY id")
a = cur.fetchall()
for i in range(len(a)):
    teacher_id = None
    print(a[i][0])
    cur.execute("SELECT date_start, teacher_id from course_lessons where course_id = %s ORDER BY id", [a[i][0]])
    lessons = cur.fetchall()
    print(lessons)
    for j in range(len(lessons)):
        if lessons[j][0] < now:
            teacher_id = lessons[j][1]
        else:
            continue
    if teacher_id is None:
        teacher_id = lessons[0][1]
    cur.execute('''UPDATE courses set default_teacher_id = %s where id = %s''', (teacher_id, a[i][0]))
    con.commit()
con.close()
