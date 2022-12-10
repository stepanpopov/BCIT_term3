def binomial_coefs():
    prev = []
    cur = [1]
    while True:
        yield cur
        prev = cur
        
        cur = []
        cur.append(1)
        for i in range(len(prev) - 1):
            cur.append(prev[i] + prev[i + 1])
        cur.append(1)

if __name__ == '__main__':
    bin_gen = binomial_coefs()
    res = [next(bin_gen) for _ in range(11)]
    for i in res:
        print(i)