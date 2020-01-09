#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import main
import datetime
import os

# globals

one_day = datetime.timedelta(days=1)
start_date = (6 - datetime.datetime.day(datetime.datetime.now())) + datetime.datetime.now()
weeks = 12
schedule = main.schedule_per_plant(weeks, start_date)


class TestFunctions(unittest.TestCase):
        
    def test_no_weekends(self):
        '''checks to make sure that no plants are being watered on a weekend'''
        for plant in schedule:
            for date in sorted(plant['schedule']):
                self.assertNotEqual(date.weekday(), 5)
                self.assertNotEqual(date.weekday(), 6)

    def test_timedeltas(self):
        '''checks to make sure that the distance between waterings for any given plant
        is no more or less than one day from its desired watering interval'''
        for plant in schedule:
            date_list = plant['schedule']
            delta = datetime.timedelta(days=plant['water_after'])
            prev_day = date_list[0]
            for date in date_list[1:]:
                self.assertGreaterEqual(date - prev_day, delta - one_day)
                self.assertLessEqual(date - prev_day, delta + one_day)
                prev_day = date

    def test_twelve_weeks(self):
        for plant in schedule:
            date_list = plant['schedule']
            total_days = date_list[-1] - date_list[0]
            weeks = total_days.days / 7.0
            self.assertGreaterEqual(weeks, weeks - 1)

    def test_file_exists(self):
        self.assertTrue(os.path.exists('plant_schedule.txt'))

    
