import requests
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker

URL = 'http://127.0.0.1:5000'

def make_url(cnt):
    res = URL + '/num/' + str(cnt)
    return res

def get_bin_coefs(cnt):
    url = make_url(cnt)
    r = requests.get(url)
    return r.json()

def plot_show(data):
    y = data
    x = list(range(0, len(y)))

    fig, ax = plt.subplots()
    ax.bar(x, y)

    ax.set_yticks(data)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.set_xlabel('Степень x в разложении')
    ax.set_title('Коэффициенты бинома Ньютона для n = {}'.format(len(data) - 1))
    
    plt.show()


if __name__ == '__main__':
    bin_coefs_from_1_to_11 = get_bin_coefs(5)
    print(bin_coefs_from_1_to_11)

    plot_show(bin_coefs_from_1_to_11[-1])
