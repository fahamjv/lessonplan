from datetimerange import DateTimeRange


def same_time(rows):
    ll = []
    counter = 0

    for i in range(0, len(rows)):
        for j in range(i + 1, len(rows)):
            if rows[i]['datetime'].is_intersection(rows[j]['datetime']):
                counter += 1
                ll.append([rows[i]['id'],rows[j]['id']])

    return ll


def same_days(data,day_name):
    ll = []
    counter = 0

    for item in data:
        if item['day'] == day_name :
            counter+=1
            ll.append(item)

    if counter > 1:
        return ll
    else:
        return []




rows = [
    {
        'id':1,
        'day':'shanbe',
        'datetime' :  DateTimeRange("2019-03-22T8:00:00+0900", "2019-03-22T10:00:00+0900"),
    },
    {
        'id': 2,
        'day':'doshanbe',
        'datetime' :  DateTimeRange("2019-03-22T9:30:00+0900", "2019-03-22T11:00:00+0900"),
    },
    {
        'id': 3,
        'day':'yekshanbe',
        'datetime': DateTimeRange("2019-03-22T10:01:00+0900", "2019-03-22T14:30:00+0900"),
    },
    {
        'id': 4,
        'day':'seshanbe',
        'datetime': DateTimeRange("2019-03-22T9:00:00+0900", "2019-03-22T12:00:00+0900"),
    }
]

ll = []

for item in ['shanbe','yekshanbe','doshanbe','seshanbe','chaharshanbe']:
    day = same_days(rows,item)
    time = same_time(day)
    if(time):
        ll.append(time[0])


print(ll)

