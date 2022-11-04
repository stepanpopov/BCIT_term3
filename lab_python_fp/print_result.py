# Здесь должна быть реализация декоратора
def print_result(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        
        if isinstance(res, list) or isinstance(res, tuple):
            for i in res:
                print(i)
        elif isinstance(res, dict):
            for key, value in res.items():
                print('{} = {}'.format(key, value))
        else:
            print(res)

        return res
    return wrapper


@print_result
def test_1(a, b):
    return a + b


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1(5, 6)
    print()
    test_2()
    print()
    test_3()
    print()
    test_4()