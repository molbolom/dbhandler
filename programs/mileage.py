


#
#      mileage.py
#
#       Program for entering mileage data for my business.
#
#
import sys
from pathlib import Path

sys.path.insert(0, Path.cwd().as_posix())

from src.CLIUI import CLIUI
from src.Splitter import Splitter
from src.KeyWord import KeyWord




class MyMileage:

    directory = "~/Work/data"
    file      = "2026-mileage.csv"

    tempdata = {"miles":0, "date":"", "stops":""}
    data = []


    @classmethod
    def add_data(self, miles, date, stops):
        self.tempdata["miles"] = miles
        self.tempdata["date"]  = date
        self.tempdata["stops"] = stops

        self.data.append(self.tempdata.copy())






