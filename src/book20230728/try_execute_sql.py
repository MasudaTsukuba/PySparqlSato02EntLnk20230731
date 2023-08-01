# try_execute_sql.py
# direct execution of sql query against postgreql database
# 2023/8/1, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass

path = PathClass('book20230728')  # path to the dataset
execute = ExecuteQueryClass(path, 'book20230728', dbms='postgres')  # prepare for the execution
exe_query = '''
SELECT DISTINCT book_title FROM (
SELECT CONCAT('http://localhost/book_title/book_id', book_id), "book_title" AS book_title 
FROM "book_title" WHERE book_id = 'Q35690') AS FOO0;
'''
execute.execute_sql(exe_query)  # execute the SQL query
