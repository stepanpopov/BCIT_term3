import json
import sys

from field import field
from gen_random import gen_random
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1



try:
    path = sys.argv[1]
except:
    path = "data_light.json"
finally:
    print(path)

with open(path, 'r', encoding='utf8') as f:
    data = json.load(f)



@print_result
def f1(arg):
    return sorted([i for i in Unique(field(data, 'job-name'), ignore_case=True)], 
                    key = lambda x: x.lower())

@print_result
def f2(arg):
    return list(filter(lambda str: str.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda str: str + ' с опытом Python', arg))


@print_result
def f4(arg):
    job_salary = zip(arg, gen_random(len(arg), 100000, 200000))
    return ["{}, зарплата {} руб.".format(job, salary) for job, salary in job_salary]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))