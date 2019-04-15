#!/usr/bin/python3
import time
from dispatcher import Dispatcher

class Runner:

    def __init__(self):
        self.__name = ""

    def get_company_name(self):
        self.__name = input("Enter company name: ").lower()


    def job_dispatch(self):
        while True:
            if len(self.__name) == 0:
                self.get_company_name()
                continue
            print("Running...")
            job_dispatcher = Dispatcher(self.__name)
            job_dispatcher.run()
            print("Saved and Done.")
            time.sleep(180)

if __name__ == '__main__':
    runner = Runner()
    runner.job_dispatch()

