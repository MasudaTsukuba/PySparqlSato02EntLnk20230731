# main020_create_genre_table.py
# create a CSV table for genre URI and genre label
# 2023/8/1, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

import csv

genre_set = set()
genre_list = []
with open('../../data/book20230728/csv/book_genre.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)

    first = True
    for line in csv_reader:
        if first:
            first = False
            continue
        genre_uri = line[1]
        genre_label = line[2]
        if genre_uri in genre_set:
            pass
        else:
            genre_list.append([genre_uri, genre_label])
            genre_set.add(genre_uri)

with open('../../data/book20230728/csv/genre_label.csv', 'w', encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["genre_uri", "genre_label"])
    csv_writer.writerows(genre_list)
