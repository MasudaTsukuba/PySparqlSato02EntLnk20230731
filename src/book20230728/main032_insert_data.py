# main032_insert_data.py
# read data from CSV files and insert them into postgresql tables
# 2023/8/1, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

import psycopg2
import csv
import os

postgres_username = os.environ.get('POSTGRES_USERNAME')  # user name is registered as an environmental variable
postgres_password = os.environ.get('POSTGRES_PASSWORD')
postgres_username = 'masuda'
postgres_password = 'masuda'
cnx = psycopg2.connect(user=postgres_username, password=postgres_password, host='localhost', port=5432, database='book20230728')
cursor = cnx.cursor()

# book_title
book_set = set()
print('book_title')
with open('../../data/book20230728/csv/book_title.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True

    sql = '''
    INSERT INTO book_title (book_id, book_title) VALUES (%s, %s);
    '''
    for row in csv_reader:
        if first:  # skip the title line
            first = False
            continue
        book_id = row[0].split('/')[4]  # extract Qnnnn part from URI
        book_title = row[1]  # book title is a literal
        try:
            cursor.execute(sql, [book_id, book_title])  # insert the data
            book_set.add(book_id)
        except Exception as e:
            print(e)
            pass
            break
        pass
cnx.commit()

# author
print('author_label')
with open('../../data/book20230728/csv/author_label.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True

    sql = '''
    INSERT INTO author (author_id, author_name) VALUES (%s, %s);
    '''
    for row in csv_reader:
        if first:
            first = False
            continue
        author_id = row[0].split('/')[4]
        name = row[1]
        try:
            cursor.execute(sql, [author_id, name])
        except Exception as e:
            print(e)
            pass
            break
        pass
cnx.commit()

# genre
print('genre_label')
with open('../../data/book20230728/csv/genre_label.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True

    sql = '''
    INSERT INTO genre (genre_id, genre_label) VALUES (%s, %s);
    '''
    for row in csv_reader:
        if first:
            first = False
            continue
        genre_id = row[0].split('/')[4]
        genre_label = row[1]
        try:
            cursor.execute(sql, [genre_id, genre_label])
        except Exception as e:
            print(e)
            pass
            break

    pass
cnx.commit()

# book_author
print('book_author')
with open('../../data/book20230728/csv/book_author.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True

    sql = '''
    INSERT INTO book_author (book_id, author_id) VALUES (%s, %s);
    '''
    for row in csv_reader:
        if first:
            first = False
            continue
        book_id = row[0].split('/')[4]
        author_id = row[1].split('/')[4]
        if book_id not in book_set:
            continue
        try:
            cursor.execute(sql, [book_id, author_id])
        except Exception as e:
            print(e)
            pass
            break
        pass
cnx.commit()

# book_genre
print('book_genre')
with open('../../data/book20230728/csv/book_genre.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True

    sql = '''
    INSERT INTO book_genre (book_id, genre_id) VALUES (%s, %s);
    '''
    for row in csv_reader:
        if first:
            first = False
            continue
        book_id = row[0].split('/')[4]
        genre_id = row[1].split('/')[4]
        if book_id not in book_set:
            continue
        try:
            cursor.execute(sql, [book_id, genre_id])
        except Exception as e:
            print(e)
            pass
            break
    pass
cnx.commit()

# book_date
print('book_date')
with open('../../data/book20230728/csv/book_date.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True

    sql = '''
    INSERT INTO book_date (book_id, pub_date) VALUES (%s, %s);
    '''
    for row in csv_reader:
        if first:
            first = False
            continue
        book_id = row[0].split('/')[4]
        pub_date = row[1]
        if book_id not in book_set:
            continue
        try:
            cursor.execute(sql, [book_id, pub_date])
        except Exception as e:
            print(e)
            pass
            break
    pass
cnx.commit()

# book_description
print('book_description')
with open('../../data/book20230728/csv/book_description.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    first = True

    sql = '''
    INSERT INTO book_description (book_id, book_description) VALUES (%s, %s);
    '''
    for row in csv_reader:
        if first:
            first = False
            continue
        book_id = row[0].split('/')[4]
        description = row[1]
        if book_id not in book_set:
            continue
        try:
            cursor.execute(sql, [book_id, description])
        except Exception as e:
            print(e)
            pass
            break

    pass

cnx.commit()
cursor.close()
cnx.close()
pass
