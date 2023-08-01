# dataset20230609 / main020_create_entity_linking_db.py
# create entity_linking.db
# 2023/6/1, Tadashi masuda
# Amagasa Laboratory, University of Tsukuba

from src.DatabaseClass import DataBase
from src.PathClass import PathClass
from src.UriClass import Uri


if __name__ == '__main__':
    path = PathClass('dataset20230609')  # set the path to the dataset
    database = DataBase(path, 'landmark.db')  # create an instance of database, default is sqlite3

    uri = Uri(path)
    # tables = ['country', 'building']
    tables = ['country']
    # sqls = [
    #     'CREATE TABLE building (id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), uri VARCHAR(255), status VARCHAR(255));',
    #     'CREATE TABLE country (id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), uri VARCHAR(255), status VARCHAR(255));'
    # ]
    sqls = [
        'CREATE TABLE country (id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), uri VARCHAR(255), status VARCHAR(255));'
    ]
    uri.create_entity_linking_db(tables, sqls)

    uri.build_entity_linking(database, tables, True, False)  # created at uri/entity_linking.db
    uri.test_entity_linking(True)
