# Пример:
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        arg = args[0]
        return [ dict[arg] for dict in items if arg in dict and dict[arg] != None]
    else:
        res = [{ arg:dict[arg] for arg in args if arg in dict and dict[arg] != None} 
                for dict in items ]
        return list(filter(lambda dict: len(dict) != 0, res))

if __name__ == "__main__":
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(field(goods, 'title', 'price'))
    print(field(goods, 'title'))