# main030_execute_query_benchmark20230728.py
# for execute sparql queries against npd20230626 dataset
# 2023/7/28, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass
from src.TimingClass import TimingClass


if __name__ == '__main__':
    path = PathClass('npd20230626')
    path.set_mapping_file('mapping.json')
    execute = ExecuteQueryClass(path, 'npd20230626', dbms='postgres')

    TimingClass.set_file_name('timing_npd20230626.csv', initialize=True, time_stamp=True)  # start the recording of execution time measurement
    for i in range(5):  # repeat 5 times
        query = 'q1.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'q3.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'q4.txt'
        execute.execute_query(query)  # the results are 0
        TimingClass.store_timing()

        query = 'q5.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'npd_q01.txt'
        execute.execute_query(query)
        TimingClass.store_timing()

        query = 'npd_q08.txt'
        execute.execute_query(query)
        TimingClass.store_timing()
