#!/usr/bin/python3
class OptionsData:

    def __init__(self):
        self.__row_data_matrix = []
        self.__column_name = ['Calls', 'Last', 'Change', 'Bid', 'Ask', 'Volume',
                              'Open Int', 'Root', 'Strike', 'Puts', 'Last', 'Change',
                              'Bid', 'Ask', 'Volume', 'Open Int', 'Price', 'NetChange', 'Percentage']

    def get_row_data_matrix(self):
        return self.__row_data_matrix

    def get_column_name(self):
        return self.__column_name

    def set_row_data_matrix(self, row_data_matrix):
        self.__row_data_matrix = row_data_matrix

    def set_column_name(self, column_name):
        self.__column_name = column_name
