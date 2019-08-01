from flask import *
from pprint import pprint
from datetimerange import DateTimeRange

from datetime import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')



@app.route('/columns')
def columns():
    d = [
          {"name":"id","title":"ID","breakpoints":"xs sm","type":"number","style":{"width":80,"maxWidth":80}},
          {"name":"day","title":"Day Name"},
          {"name":"datetime","title":"Time"},
        ]
    return jsonify(d)

@app.route('/rows')
def rows():
    d = [
        {
            'id': 1,
            'day': 'shanbe',
            'datetime': DateTimeRange("2019-03-22T8:00:00+0900", "2019-03-22T10:00:00+0900"),
            # 'datetime' :  datetime.now(),
        },
    ]

    print(d)

    return 'asd'
    d = [
        {
            'id':1,
            'day':'shanbe',
            'datetime' :  DateTimeRange("2019-03-22T8:00:00+0900", "2019-03-22T10:00:00+0900"),
            # 'datetime' :  datetime.now(),
        },
    ]
    return jsonify(d)

