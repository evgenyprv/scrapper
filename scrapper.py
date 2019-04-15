#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from data import OptionsData

class Scrapper:

    __page_counter = 1

    def __init__(self, company_name):
        self.company_name = company_name
        self.__optionsData = OptionsData()
        self.__last_page_num = 0
        self.__soup = None

    def _connect_to_website(self):
        __url = "https://www.nasdaq.com/symbol/" + self.company_name.lower() + "/option-chain?&money=all&page=%i" % Scrapper.__page_counter
        page = requests.get(__url).text
        self.__soup = BeautifulSoup(page, 'lxml')
        self.__last_page_num = self.__get_max_number_of_pages(self.__soup)

    def scan_url(self):
        container = self.__soup.find('div', {'class': 'wrap cf'})

        price = container.find('div', {'class': 'qwidget-dollar'}).get_text().replace('$','')
        net_change = container.find('div', {'class': 'qwidget-cents'}).get_text()
        percentage = container.find('div', {'class': 'qwidget-percent'}).get_text()

        overview_list = [price, net_change, percentage]

        my_table = container.find('div', {'class': 'OptionsChain-chart'})

        data = my_table.find('table').find_all('tr')

        ##Get Data
        for line in data:
            if line.td is not None and len(line) > 0:
                line = line.get_text().replace('\n','|').split('|')
                filtered_line = line[1:len(line)-1]
                filtered_line.append(price)
                filtered_line.append(net_change)
                filtered_line.append(percentage)
                self.__optionsData.get_row_data_matrix().append(filtered_line)

        if self.__page_counter == self.__last_page_num:
            return False, self.__optionsData

        Scrapper.__page_counter += 1

        return True, self.__optionsData

    def __get_max_number_of_pages(self, soup):
        max_page_number = 1
        page_numbers = soup.find('div', {'id': 'pagerContainer'}).find_all('li')

        if len(page_numbers) > 1:
            for number in page_numbers:
                if number.get_text().isdigit():
                    max_page_number = int(number.get_text())

        return max_page_number


