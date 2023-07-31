from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass

path = PathClass('book20230728')
execute = ExecuteQueryClass(path, 'book20230728', dbms='postgres')
exe_query = '''
SELECT DISTINCT book_title FROM (
SELECT CONCAT('http://localhost/book_title/book_id', book_id), "book_title" AS book_title 
FROM "book_title" WHERE book_id = 'Q35690') AS FOO0;
'''
execute.execute_sql(exe_query)
