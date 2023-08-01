# data_set2 / test_landmark_db.py
# 2023/8/1, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

import sqlite3
import os

working_dir = os.getcwd()
if working_dir.endswith('src'):
    working_dir = os.path.dirname(working_dir)


def test_sql():
    conn = sqlite3.connect(working_dir+'/data/data_set2/csv/landmark.db')  # connect to sqlite3 database
    cursor = conn.cursor()
    sql = 'SELECT * FROM hotel;'
    cursor.execute(sql)
    results = cursor.fetchall()
    # print(results)
    assert len(results) == 822  # should contain 822 records in hotel table

    sql = 'SELECT * FROM building;'
    cursor.execute(sql)
    results = cursor.fetchall()
    # print(results)
    assert len(results) == 18556  # in building table

    sql = 'SELECT * FROM museum;'
    cursor.execute(sql)
    results = cursor.fetchall()
    # print(results)
    assert len(results) == 19958  # in museum table

    sql = 'SELECT * FROM heritage;'
    cursor.execute(sql)
    results = cursor.fetchall()
    # print(results)
    assert len(results) == 5154  # in heritage table


if __name__ == '__main__':
    test_sql()
