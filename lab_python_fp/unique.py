from lab_python_fp.gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_items = set()
        self.iterator = iter(items)
        if 'ignore_case' in kwargs and kwargs['ignore_case'] == True:
            self.ignore_case = True
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            item = None
            try:
                item = next(self.iterator)
            except StopIteration:
                raise StopIteration
            
            item_original = item
            if self.ignore_case:
                item = str(item).lower()

            if item not in self.used_items:
                self.used_items.add(item)
                return item_original 
            
    def __iter__(self):
        return self


if __name__ == "__main__":
    # data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 'A', 3, 'a', '1567', 1567, 'AAb', 'AAB', 'aAb', 'aab']
    data = gen_random(100, 1, 3)

    for i in Unique(data, ignore_case=True):
        print(i)
