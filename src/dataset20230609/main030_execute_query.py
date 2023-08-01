# dataset20230609 / main030_execute_query.py
# for execute sparql queries against dataset20230609
# 2023/6/14, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass


if __name__ == '__main__':
    path = PathClass('dataset20230609')  # set the path to the dataset
    path.set_mapping_file('mapping_revised.json')  # specify the mapping file
    execute = ExecuteQueryClass(path)  # create an instance for preparing execution

    # uncomment to select a query
    query = '3_q1.txt'
    # query = '3_q2.txt'
    # query = '3_q3.txt'
    # query = 'query_with_OR_in_filter20230615.txt'
    # query = 'query_with_AND_in_filter20230616.txt'
    # query = 'query_with_OR_AND_in_filter20230616.txt'
    # query = 'query_with_OR_OR_AND_in_filter20230616.txt'
    # query = 'query_with_NOT_in_filter20230616.txt'
    execute.execute_query(query)  # execute the sparql query
