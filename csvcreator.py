#!/usr/bin/python3
import pandas as pd
import os

from datetime import datetime


class CsvCreator:

    def __init__(self, row_data, column_name, company_name):
        self.__company_name = company_name
        self.__data = pd.DataFrame(row_data, columns=column_name)

    def create_cvs_file(self):
        __path = os.getcwd()
        self.__data.to_csv(__path+'/csv_files/%s_%s.csv' % (self.__company_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')), index=False)
