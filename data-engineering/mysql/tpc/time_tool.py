# -*- coding: utf-8 -*

import time
import datetime

DAY_SECONDS = 24 * 60 * 60


def get_time():
    return time.time()


def get_time_struct():
    return time.localtime(time.time())


def get_time_struct_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_datetime():
    return datetime.datetime.now()


def construct_datetime(year, month, day, hour, minute, second):
    return datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)


def datetime_to_time(dt):
    return dt.timestamp()


def time_to_datetime(t):
    return datetime.datetime.fromtimestamp(t)


def str_to_datetime(str, date_format='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strptime(str, date_format)


def datetime_to_str(dt, date_format='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format=date_format)


def add_days(dt, days=1):
    return dt + datetime.timedelta(days=days)


def delta_seconds(seconds):
    return datetime.timedelta(seconds=seconds)


def delta_hours(hours):
    return datetime.timedelta(hours=hours)


if __name__ == '__main__':
    print(get_time())
    # print(get_time_struct())
    # print(get_time_struct_str())
    print(get_datetime())
    # print(datetime_to_time(get_datetime()))
    # print(time_to_datetime(get_time()))
    #
    # print(datetime_to_str(get_datetime()))
    # print(str_to_datetime(datetime_to_str(get_datetime())))
    # print(time.time())
    # time.sleep(2)
    # print(time.time())
