"""TimingClass.py
A class for measuring and storing execution time
2023/8/1, Tadashi Masuda
Amagasa Laboratory, University of Tsukuba
"""
import time
from datetime import datetime
import csv


class TimingClass:
    """A class for measuring and storing execution time

    """
    timing_list = []
    file_name = None
    query_name = None
    time_stamp = None

    def __init__(self, query_name, keyword):
        self.query_name = query_name
        TimingClass.query_name = query_name
        self.keyword = keyword
        self.start_time = None
        self.end_time = None
        self.execution_time = None
        self.record_start()
        pass

    def record_start(self):
        """start the recording
        """
        self.start_time = time.time()
        # TimingClass.start_time = self.start_time

    def record_end(self):
        """Record the end time and calculate the execution time

        :return:
        """
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        TimingClass.timing_list.append([self.query_name, self.keyword, self.execution_time])

    @staticmethod
    def init_file(file_name):
        """Initialize the output file

        :param file_name: Output file name
        :return:
        """
        TimingClass.file_name = file_name
        with open(TimingClass.file_name, 'w') as output_file:
            output_file.write('query, date_time, keyword, exec_time\n')

    @staticmethod
    def set_file_name(file_name, initialize=False, time_stamp=False):
        """Set a file name for storing the timing info

        :param file_name: Output file name
        :param initialize: Initialize the file
        :param time_stamp: Record the start time
        :return: None
        """
        TimingClass.file_name = file_name
        if initialize:
            TimingClass.init_file(file_name)
        if time_stamp:
            TimingClass.record_time_stamp()

    @staticmethod
    def record_time_stamp():
        TimingClass.time_stamp = time.time()

    @staticmethod
    def store_timing():  #
        """store the results in a file

        :return: None
        """
        with open(TimingClass.file_name, 'a', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            for timing in TimingClass.timing_list:
                dt_object = datetime.fromtimestamp(TimingClass.time_stamp)
                date_time_string = dt_object.strftime('%Y-%m-%d %H:%M:%S')
                timing.insert(1, date_time_string)
                csv_writer.writerow(timing)
            TimingClass.timing_list = []  # clear list
