import time
def pro_bar(scale):
    start = time.perf_counter()
    for i in range(scale + 1):
        a = '*' * i
        b = '.' * (scale - i)
        c = (i / scale) * 100
        dur = time.perf_counter() - start
        print('\r{:^3.0f}% '.format(c, a, b, dur), end = '')
        time.sleep(0.05)
pro_bar(50)
