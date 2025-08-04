import random
import time

def get_random_date(start_date, end_date):
    print("Print a random date between ", start_date, "and", end_date)
    rand_gen = random.random()
    date_format = '%d/%m/%Y'
    start_time = time.mktime(time.strptime(start_date, date_format))
    end_time = time.mktime(time.strptime(end_date, date_format))
    rand_time = start_time + rand_gen * (end_time - start_time)
    rand_date = time.strftime(date_format, time.localtime(rand_time))
    return rand_date

print("Random date = ", get_random_date("1/1/2000", "31/12/2025"))