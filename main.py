from flask import *
from pprint import *
from datetimerange import DateTimeRange
from datetime import *
import pymysql.cursors

app = Flask(__name__)



def same_time(rows):
    ll = []
    counter = 0

    for i in range(0, len(rows)):
        for j in range(i + 1, len(rows)):
            if rows[i]['time'].is_intersection(rows[j]['time']):
                counter += 1
                ll.append([rows[i]['id'],rows[j]['id']])

    return ll

def same_days(rows,day_name):
    ll = []
    counter = 0

    for item in rows:
        if item['day'] == day_name :
            counter+=1
            ll.append(item)

    if counter > 1:
        return ll
    else:
        return []

def make_rows(rows):
    ll = []

    for item in rows:

        collection = {
            'id': item['id'],
            'day': item['day'],
            'time': DateTimeRange("2019-03-22T%s+0900" % item['start_time'], "2019-03-22T%s+0900" % item['end_time']),
        }

        ll.append(collection)

    return ll



@app.route('/')
def main():
    return render_template('index.html')




@app.route('/check')
def check():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='classplanning',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "SELECT * FROM `classes`"
            cursor.execute(sql)
            result = cursor.fetchall()

            rows = make_rows(result)

            return str(rows)


            ll = []

            for item in ['shanbe', 'yekshanbe', 'doshanbe', 'seshanbe', 'chaharshanbe']:
                day = same_days(rows, item)
                time = same_time(day)
                if (time):
                    ll.append(time[0])

            return jsonify(ll)


            for item in result:
                item['start_time'] = item['start_time'][:-3]
                item['end_time'] = item['end_time'][:-3]
                item['remove'] = "<a href='%s'>Remove</a>" % url_for('remove', id=item['id'])

            return jsonify(result)

    finally:
        connection.close()




@app.route('/add',methods=["POST"])
def add():

    startTime = "%s:%s" % (request.form.get('start_time'),'01')
    endTime = "%s:%s" % (request.form.get('end_time'),'01')
    day = request.form.get('day')
    lessonCode = request.form.get('lesson_code')



    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='classplanning',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `classes` (`id`, `lesson_code`, `day`, `start_time`, `end_time`) VALUES (NULL, %s, %s , %s, %s)"
            cursor.execute(sql, (lessonCode, day, startTime, endTime))

        connection.commit()

    finally:
        connection.close()
        return redirect('/')



    return  startTime + '<br>' + endTime + '<br>' + day + '<br>' + lessonCode



@app.route('/remove/<id>')
def remove(id):

    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='classplanning',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = "DELETE FROM `classes` WHERE `classes`.`id` = %s"
            cursor.execute(sql, (id))


        connection.commit()

    finally:
        connection.close()
        return redirect('/')



@app.route('/columns')
def columns():
    d = [
          {"name":"id","title":"ID","breakpoints":"xs sm","type":"number","style":{"width":80,"maxWidth":80}},
          {"name": "day", "title": "Day Name"},
          {"name": "lesson_code","title":"Lesson code"},
          {"name":"start_time","title":"Start Time"},
          {"name":"end_time","title":"End Time"},
          {"name":"remove","title":"Remove"},
        ]
    return jsonify(d)

@app.route('/rows')
def rows():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='classplanning',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "SELECT * FROM `classes`"
            cursor.execute(sql)
            result = cursor.fetchall()

            for item in result:
                item['start_time'] = item['start_time'][:-3]
                item['end_time'] = item['end_time'][:-3]
                item['remove'] = "<a href='%s'>Remove</a>" % url_for('remove',id=item['id'])

            return jsonify(result)

    finally:
        connection.close()




