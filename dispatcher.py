#!usr/bin/python3

import pandas as pd
import os
import boto3

from datetime import datetime


class CsvCreator:

    def __init__(self, row_data, column_name, company_name):
        self.__company_name = company_name
        self.__data = pd.DataFrame(row_data, columns=column_name)

    def create_cvs_file(self):
        __path = os.getcwd()
        s3 = boto3.client('s3')
        name = '%s_%s.csv' % (self.__company_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        path_file = __path + '/csv_files/%s_%s.csv' % (
        self.__company_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.__data.to_csv(path_file, index=False)
        s3.upload_file(Filename=path_file, Bucket='scrapperbucket', Key='scrapper_csv/%s' % name)
        os.remove(path_file)
