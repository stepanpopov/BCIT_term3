data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

def sort1(data):
    return sorted(data, key = abs, reverse = True)

def sort2(data):
    return sorted(data, key = lambda i: abs(i), reverse = True)

if __name__ == '__main__':
    result = sort1(data)
    print(result)

    result_with_lambda = sort2(data)
    print(result_with_lambda)
