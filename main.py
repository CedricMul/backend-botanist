#!/usr/bin/env python

import datetime
import json


def parse_json(filename):
    with open(filename) as f:
        data = json.load(f)
    plant_dict = {}
    for di in data:
        name = di['name']
        rate_l = di['water_after'].split(' ')
        rate_int = int(rate_l[0])
        plant_dict[name] = rate_int
    return plant_dict


def schedule_per_plant(weeks, start_date):
    plant_dict = parse_json('plant_info.json')
    days = weeks * 7
    delt = datetime.timedelta(days=1)
    plant_schedule = {}
    for i in plant_dict:
        plant_schedule[i] = {'rate': plant_dict[i], 'schedule': []}
    c = 0
    for p in plant_schedule:
        d = start_date
        plant_schedule[p]['schedule'].append(d)
        for i in range(days):
            c += 1
            d = d + delt
            if c == plant_schedule[p]['rate']:
                plant_schedule[p]['schedule'].append(d)
                c = 0
    return plant_schedule



def final_schedule():
    days = 84
    delt = datetime.timedelta(days=1)
    d = datetime.date.today()
    plant_schedule = schedule_per_plant(12, d)
    date_schedule = {d: []}
    for i in range(days):
        d = d + delt
        date_schedule[d] = []
    for i in date_schedule:
        for plant in plant_schedule:
            for t in plant_schedule[plant]['schedule']:
                if t == i:
                    date_schedule[i].append(plant)
    return date_schedule


def weekend_filter():
    sched = final_schedule()
    day = datetime.timedelta(days=1)
    for date in sched:
        if date.weekday() == 5:
            for plant in sched[date]:
                sched[date - day].append(plant)
            sched[date].clear()
        if date.weekday() == 6:
            for plant in sched[date]:
                sched[date + day].append(plant)
            sched[date].clear()
    return sched


def create_table():
    docstring = "---------------------------------------------------\n"
    schedule = weekend_filter()
    for d in schedule:
        docstring = "{}|| {} ||||||||||||||||\n".format(docstring, d)
        for plant in schedule[d]:
            docstring = "{}||--{}\n".format(docstring, plant)
    return docstring


def main():
    s = create_table()
    with open('schedule.txt', 'w') as text:
        text.write(s)


if __name__ == "__main__":
    main()