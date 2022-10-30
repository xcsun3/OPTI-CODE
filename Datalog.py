import time
from xmlrpc.client import boolean
# import Accelerometer
import BatteryManagement
import gps
import pandas as pd
from datetime import datetime
from threading import Timer


class Datalog():

    def __init__(self, interval = 1, export = True):
        self._timer = None
        self.interval = interval
        self.export = export
        self.today = datetime.today()
        self.data = {'Time': [], 'Battery': []}
        self.is_running = False
        self.start()
        self.get_bat = BatteryManagement.BatteryManagement()
        # self.get_acc = Accelerometer.Accelerometer()
        # self.get_gps = gps.BerryGPS()

    # Get accelerometer information
    # def get_acceleration(self):
        # accXnorm, accYnorm = self.get_acc.get_measurement()
        # return accXnorm, accYnorm

    # Get battery information
    def get_batterty(self):
        battery = self.get_bat.get_BSoC()
        return battery

    # Get gps information
    # def get_gps(self):
        # res = self.get_gps.getData()
        # lat, dirLat, lon, dirLon, speed, time, trCourse, date = res
        # return res

    # What to do in each time step
    def _run(self):
        self.is_running = False
        self.start()
        now = datetime.now()
        self.current_time = now.strftime("%H:%M:%S")
        # data_x, data_y = self.get_acceleration()
        data_bat = self.get_batterty()
        # data_gps = self.get_gps()
        self.data['Time'].append(self.current_time)
        # self.data['AccX'].append(data_x)
        # self.data['AccY'].append(data_y)
        self.data['Battery'].append(data_bat)
        # self.data['GPS'].append(data_gps)

    # Start data collection
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    # End data collection
    def stop(self):
        self._timer.cancel()
        self.is_running = False
        if self.export:
            self.output_csv()

    # Output saved data of the current run in csv
    def output_csv(self):
        df = pd.DataFrame(self.data)
        df['Time'] = pd.to_datetime(df['Time'])
        d4 = self.today.strftime("%b-%d-%Y-%H-%M")
        file_name = "CMSR_log_" + d4 + ".csv"
        df.to_csv(file_name, encoding='utf-8', index=False)
        return True
