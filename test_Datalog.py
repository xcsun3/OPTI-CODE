import pandas as pd
import Datalog
import time

# data = {'Time': [], 'Battery': [], 'AccX': [], 'AccY': [], 'GPS': []}

# for i in range(5):
    # data['Time'].append(i)
    # data['AccX'].append(i*3)
    # data['AccY'].append(i*5)
    # data['Battery'].append(i/5)
    # data['GPS'].append(i**2)

# df = pd.DataFrame(data)
# df.to_csv("dataframeoutput_sample.csv", encoding='utf-8', index=False)


# Testing that battery reading descends over time
def test_timer():
    get_dat = Datalog.Datalog(interval = 1, export = False)
    time.sleep(5)
    list = get_dat.data['Battery']
    print(list)
    assert list == sorted(list, reverse=True)
    

# Generate sample output data log
data_log = Datalog.Datalog(1)
time.sleep(3)
data_log.stop()
