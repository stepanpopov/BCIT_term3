import sys
import math       

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()

    # Переводим строку в действительное число
    try:
        coef = float(coef_str)
    except:
        print(prompt)
        coef_str = input()
        while True:
            try:
                coef = float(coef_str)
                break
            except:
                print(prompt)
                coef_str = input()

    return coef

def t_to_x(t):
    x_list = []
    if t == 0:
        x_list.append(0)
    elif t > 0:
        sq_t = math.sqrt(t)
        x_list.append(sq_t)
        x_list.append((-1) * sq_t)
    return x_list

def get_roots(a, b, c):
    result = []
    D_t = b*b - 4*a*c
    if D_t == 0.0:
        t = -b / (2.0*a)
        result += t_to_x(t) 
    elif D_t > 0:
        sq_D = math.sqrt(D_t)
        t1 = (-b + sq_D) / (2.0*a)
        t2 = (-b - sq_D) / (2.0*a)
        result += t_to_x(t1)
        result += t_to_x(t2)
    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    if a == 0:
        print("Биквадратного уравнения не получается (a == 0) ")
        return
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)

    print()
    if len_roots == 0:
        print('Нет корней')
    else:
        print("Количество корней {}".format(len_roots))
        for root in roots:
            print(round(root, 4), end = ' ')
        print()


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
