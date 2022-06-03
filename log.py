from datetime import datetime as dt
# from time import time

def primer (v1, v2, o, r):
    time = dt.now().strftime('%H:%M')
    with open('log_calculate.csv', 'a') as file:     
        file.write('{}: primer {} {} {} = {}'.format(time, v1, o, v2, r))
