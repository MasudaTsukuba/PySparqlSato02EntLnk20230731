# main030_execute_query for execute sparql queries
# for npd20230626 dataset
# 2023/7/3, Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass


if __name__ == '__main__':
    path = PathClass('stock_exchange_20230705')
    path.set_mapping_file('mapping.json')
    execute = ExecuteQueryClass(path, 'stock_exchange_20230629', dbms='postgres')
    query = 'Q1.txt'  # uncomment to select a query
    query = 'Q1_trader.txt'  # uncomment to select a query
    query = 'Q2.txt'
    query = 'Q2a.txt'
    query = 'Q2_PhysicalPerson.txt'
    query = 'Q2_PhysicalPerson_hasAddress.txt'
    query = 'Q3a.txt'
    query = 'Q3a_Stock.txt'
    query = 'Q3a_FinantialInstrument_Stock.txt'
    query = 'Q4a.txt'
    query = 'Q4b.txt'
    query = 'Q4c.txt'
    query = 'Q4d.txt'
    query = 'Q4.txt'

    query = 'Q5a.txt'
    query = 'Q5b.txt'
    query = 'Q5c.txt'
    query = 'Q5d.txt'
    query = 'Q5e.txt'
    query = 'Q5f.txt'
    query = 'Q5.txt'

    execute.execute_query(query)