
import time
import datetime

import collections


raw1 = {
    'day' : 1,
    'code' : 1298,
    'teacher' : 'damon',
    'classnumber' : 122,
    'classtime' :  {
        'start':datetime.time(8,0),
        'end':datetime.time(9,40)
    }
}

raw2 = {
    'day' : 2,
    'code' : 1321,
    'teacher' : 'esmaeil',
    'classnumber' : 111,
    'classtime' :  {
        'start':datetime.time(16,0),
        'end':datetime.time(19,20)
    }
}

raw3 = {
    'day' : 2,
    'code' : 9128,
    'teacher' : 'magid',
    'classnumber' : 127,
    'classtime' :  {
        'start':datetime.time(8,0),
        'end':datetime.time(9,40)
    }
}

raw4 = {
    'day' : 2,
    'code' : 1297,
    'teacher' : 'mohammad',
    'classnumber' : 114,
    'classtime' :  {
        'start':datetime.time(9,50),
        'end':datetime.time(14,20)
    }
}


raw5 = {
    'day' : 3,
    'code' : 1317,
    'teacher' : 'shadman',
    'classnumber' : 123,
    'classtime' :  {
        'start':datetime.time(9,50),
        'end':datetime.time(11,30)
    }
}

raw6 = {
    'day' : 3,
    'code' : 1315,
    'teacher' : 'milad',
    'classnumber' : 114,
    'classtime' :  {
        'start':datetime.time(15,10),
        'end':datetime.time(18,30)
    }
}

def same_day(items):
    days = []
    for item in items:
        days.append(item.get('day'))

    dup = [item for item, count in collections.Counter(days).items() if count > 1]

    dat = []
    for item in items:
        if item['day'] in dup:
            dat.append(item)
    return dat


def same_teacher(items):
    teachers = []
    for item in items:
        teachers.append(item.get('teacher'))

    dup = [item for item, count in collections.Counter(teachers).items() if count > 1]

    dat = []
    for item in items:
        if item['teacher'] in dup:
            dat.append(item)
    return dat


def same_classnumber(items):
    classes = []
    for item in items:
        classes.append(item.get('classnumber'))

    dup = [item for item, count in collections.Counter(classes).items() if count > 1]

    dat = []
    for item in items:
        if item['classnumber'] in dup:
            dat.append(item)
    return dat


# this need work
def same_time(items):

    start_times = []
    end_times = []

    for item in items:
        start_times.append(item.get('classtime').get('start'))

    for item in items:
        end_times.append(item.get('classtime').get('end'))

    print(start_times)
    print(end_times)
    exit(1)

    dup = [item for item, count in collections.Counter(classes).items() if count > 1]

    dat = []
    for item in items:
        if item['classtime'] in dup:
            dat.append(item)
    return dat





items = raw1, raw2, raw3, raw4, raw5, raw6

same_day = same_day(items)

#same_teacher= same_teacher(same_day)

# same_classnumber = same_classnumber(same_teacher)

same_time = same_time(same_day)

print(same_day)

print(same_time)
