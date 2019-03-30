from scrapper import Scrapper
from data import OptionsData
from csvcreator import CsvCreator


class Dispatcher:

    def __init__(self, company_name):
        self.__scrapper = Scrapper(company_name)

    def run(self):
        self.__scrapper._connect_to_website()
        return self.__scrapper.scan_url()

    def create_csv(self):
        csv_creator = CsvCreator(data_object.get_row_data_matrix(), data_object.get_column_name(), company_name)
        csv_creator.create_cvs_file()

if __name__ == '__main__':
    company_name = input("Company name please: ")
    dispatcher = Dispatcher(company_name)

    flag = True

    while flag:
        flag, data_object = dispatcher.run()

    dispatcher.create_csv()

