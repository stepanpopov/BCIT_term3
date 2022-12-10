import requests

def make_url(cnt):
    base_url = 'http://127.0.0.1:5000/num/'
    res = base_url + str(cnt)
    return res

def get_data(cnt):
    url = make_url(cnt)
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/num/10'
    # Вызовем сервис
    r = requests.get(url)
    print(r)
    data = r.json()
    print(data)

