days = {
    'Mon': 0,
    'Tue': 1,
    'Wed': 2,
    'Thu': 3,
    'Fri': 4,
    'Sat': 5,
    'Sun': 6,
}

def get_minutes(start, end):
    global days
    meets = {
        'start': {
            'day': days[start[:3]],
            'hour': int(start[4:6]),
            'minutes': int(start[7:9]),
        },
        'end': {
            'day': days[end[:3]],
            'hour': int(end[4:6]),
            'minutes': int(end[7:9]),
        }
    }

    diffs = {
        'hour': meets['end']['hour'] - meets['start']['hour'],
        'minutes': meets['end']['minutes'] - meets['start']['minutes'],
    }

    if meets['start']['day'] != meets['end']['day']:
        diffs['hour'] += (meets['end']['day'] - meets['start']['day']) * 24

    if diffs['minutes'] < 0:
        diffs['minutes'] *= -1
        diffs['hour'] -= 1

    return diffs['minutes'] + (60 * diffs['hour'])

def format_to_int(meet):
    global days
    return "{} {}".format(days[meet[:3]], meet[4:])

def format_to_Ddd(meet):
    global days
    for key, value in days.items():
        if value == int(meet[0]):
            return "{} {}".format(key, meet[2:])

def make_pair(meet):
    day = meet[:3]
    schedules = meet[4:].split('-')
    return ["{} {}".format(day, schedules[0]), "{} {}".format(day, schedules[1])]

def solution(S):
    # write your code in Python 3.6
    meetings = S.splitlines()
    global days

    # Ordenar os encontros
    meetings = [format_to_int(meet) for meet in meetings]
    meetings = sorted(meetings)
    meetings = [format_to_Ddd(meet) for meet in meetings]

    # Estruturar entradas
    first = 'Mon 00:00'
    last = 'Sun 24:00'
    list_meetings = [make_pair(meet) for meet in meetings]
    list_meetings = [item for sublist in list_meetings for item in sublist]
    list_meetings = [first, *list_meetings, last]
    pairs = []

    for i in range(1, len(list_meetings), 2):
        pairs.append([list_meetings[i-1], list_meetings[i]])

    # Pegar o intervalo entre dois encontros
    minutes = []
    for pair in pairs:
        minutes.append(get_minutes(pair[0], pair[1]))

    return max(minutes)

test = "Sun 10:00-20:00\nFri 05:00-10:00\nFri 16:30-23:50\nSat 10:00-24:00\nSun 01:00-04:00\nSat 02:00-06:00\nTue 03:30-18:15\nTue 19:00-20:00\nWed 04:25-15:14\nWed 15:14-22:40\nThu 00:00-23:59\nMon 05:00-13:00\nMon 15:00-21:00"
solution(test)