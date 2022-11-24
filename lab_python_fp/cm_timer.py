import time
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time.time()
        
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            end = time.time()
            t = end - self.start
            print("time = {}".format(t))


@contextmanager
def cm_timer_2():
    start = time.time()
    yield None
    end = time.time()
    t = end - start
    print("time = {}".format(t))



if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(1.5)
    with cm_timer_2():
        time.sleep(1.3)
    
