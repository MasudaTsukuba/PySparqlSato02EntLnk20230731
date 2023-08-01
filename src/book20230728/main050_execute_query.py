# main050_execute_query for execute sparql queries
# book20230728 dataset
# 2023/7/28, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass
from src.TimingClass import TimingClass


if __name__ == '__main__':
    path = PathClass('book20230728')  # set the path to the dataset
    path.set_mapping_file('mapping.json')  # set the mapping file
    execute = ExecuteQueryClass(path, 'book20230728', dbms='postgres')  # prepare for execution

    # uncomment to select a query
    query = 'q1.txt'
    query = 'q1_book_type.txt'
    query = 'q1_author_type.txt'
    query = 'q1_author_name.txt'
    query = 'q1_genre_type.txt'
    query = 'q1_genre_name.txt'
    # query = 'q2.txt'
    # query = 'q3.txt'
    # query = 'q4_author.txt'
    # query = 'q4_book_author.txt'
    # query = 'q4_IAmACat.txt'
    # query = 'q4_IAmACat_author.txt'
    # query = 'q4_book_Soseki.txt'
    # query = 'q4_book_name_Soseki.txt'
    query = 'q5_genre_label.txt'

    TimingClass.set_file_name('timing_book20230728.csv', initialize=True, time_stamp=True)  # start the time measurement
    execute.execute_query(query)  # execute the query
    TimingClass.store_timing()  # stop the time measurement
