from flask import *
from pprint import *
from datetimerange import DateTimeRange
from datetime import *
import pymysql.cursors
import random
from numpy import *


app = Flask(__name__)


def longest(l):
    if(not isinstance(l, list)): return(0)
    return(max([len(l),] + [len(subl) for subl in l if isinstance(subl, list)] +
        [longest(subl) for subl in l]))

def same_time(rows):
    ll = []
    counter = 0

    colors = ['#B0E2FF',
              '#A4D3EE',
              '#8DB6CD',
              '#1C86EE',
              '#7FFFD4',
              '#76EEC6',
              '#F0F8FF',
              '#F0F8FF',
              '#FFE4E1',
              '#BEBEBE',
              '#FFF68F',
              '#FFDAB9',
              '#CDC8B1',
              '#EE82EE',
              '#DDA0DD',
              '#A020F0',
              ]

    color = random.choice(colors)
    for i in range(0, len(rows)):
        for j in range(i + 1, len(rows)):
            if rows[i]['time'].is_intersection(rows[j]['time']):
                counter += 1
                ll.append([rows[i]['id'],rows[j]['id'],color])


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


            ll = []
            for item in ['شنبه','یکشنبه','دوشنبه','سه شنبه','چهارشنبه']:
                day = same_days(rows, item)
                time = same_time(day)
                if (time):
                    ll.append(time)

            return jsonify(ll)

    finally:
        connection.close()




@app.route('/add',methods=["POST"])
def add():


    # assert request.form.get('day') != ""
    # assert request.form.get('start_time') != ""
    # assert request.form.get('end_time') != ""



    startTime = "%s:%s" % (request.form.get('start_time'),'01')
    endTime = "%s:%s" % (request.form.get('end_time'),'01')
    day = request.form.get('day')
    lessonCode = request.form.get('lesson_code')
    lessonName = request.form.get('lesson_name')
    teacher = request.form.get('teacher')




    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='classplanning',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:

            # Create a new record
            sql = "INSERT INTO `classes` (`id`, `lesson_name`, `teacher`, `lesson_code`, `day`, `start_time`, `end_time`) VALUES (NULL, %s, %s, %s, %s, %s, %s)"
            print(sql)
            cursor.execute(sql, (lessonName,teacher,lessonCode,day,startTime,endTime))

        connection.commit()

    finally:
        connection.close()
        return redirect('/')




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
          {"name":"id","title":"شماره","breakpoints":"xs sm","type":"number","style":{"width":80,"maxWidth":80}},
          {"name": "lesson_name", "title": "نام درس"},
          {"name": "teacher", "title": "استاد"},
          {"name": "day", "title": "روز"},
          {"name": "lesson_code","title":"کد درس"},
          {"name":"start_time","title":" شروع"},
          {"name":"end_time","title":" پایان"},
          {"name":"remove","title":"تنظیمات"},
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
            sql = "SELECT * FROM `classes`  ORDER BY `day`"
            cursor.execute(sql)
            result = cursor.fetchall()

            for item in result:
                item['start_time'] = item['start_time'][:-3]
                item['end_time'] = item['end_time'][:-3]
                item['remove'] = "<a href='%s'>Remove</a>" % url_for('remove',id=item['id'])
                item['remove'] = "<a href='%s'><button type='button' class='btn btn-danger'>حذف</button></a>" % url_for('remove',id=item['id'])

            return jsonify(result)

    finally:
        connection.close()




