from src.ExecuteQueryClass import ExecuteQueryClass
from src.PathClass import PathClass

path = PathClass('book20230728')
path.set_mapping_file('mapping.json')
execute = ExecuteQueryClass(path, 'book20230728', dbms='postgres')


def test_q1():
    results = execute.execute_query('q1.txt')
    assert len(results) == 100000

    results = execute.execute_query('q1_book_type.txt')
    assert len(results) == 100000

    results = execute.execute_query('q1_author_type.txt')
    assert len(results) == 29814

    results = execute.execute_query('q1_author_name.txt')
    assert len(results) == 29814

    results = execute.execute_query('q1_genre_type.txt')
    assert len(results) == 1988

    results = execute.execute_query('q1_genre_name.txt')
    assert len(results) == 1988


def test_q2():
    results = execute.execute_query('q2.txt')
    assert len(results) == 54987


def test_q3():
    results = execute.execute_query('q3.txt')
    assert len(results) == 1


def test_q4():
    results = execute.execute_query('q4_author.txt')
    assert len(results) == 54987

    results = execute.execute_query('q4_book_author.txt')
    assert len(results) == 54987

    results = execute.execute_query('q4_IAmACat.txt')
    assert len(results) == 1

    results = execute.execute_query('q4_IAmACat_author.txt')
    assert len(results) == 1

    results = execute.execute_query('q4_book_Soseki.txt')
    assert len(results) == 21

    results = execute.execute_query('q4_book_name_Soseki.txt')
    assert len(results) == 21
