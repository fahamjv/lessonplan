from datetimerange import DateTimeRange


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
            'time': DateTimeRange("2019-03-22T%s+0900" % item['time']['start'], "2019-03-22T%s+0900" % item['time']['end']),
        }

        ll.append(collection)

    return ll


before = [
    {
        'id': 1,
        'day': 'shanbe',
        'time': {
            'start':'8:00:00',
            'end':'10:00:00',
        }
    },
    {
        'id': 2,
        'day': 'doshanbe',
        'time': {
            'start': '9:30:00',
            'end': '11:00:00',
        }
    },
    {
        'id': 3,
        'day': 'shanbe',
        'time': {
            'start': '9:00:00',
            'end': '14:30:00',
        }
    },
    {
        'id': 4,
        'day': 'shanbe',
        'time': {
            'start': '9:30:00',
            'end': '12:00:00',
        }
    }
]

rows = make_rows(before)


ll = []

for item in ['saturday','sunday','monday','tuesday','wednesday']:
    day = same_days(rows,item)
    time = same_time(day)
    if(time):
        ll.append(time)


print(ll[0])

