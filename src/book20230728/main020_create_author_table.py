# main020_create_author_table.py
# create a CSV table for author URI and author name
# 2023/8/1, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

import csv

author_set = set()
author_list = []
with open('../../data/book20230728/csv/book_author.csv', 'r') as input_file:
    csv_reader = csv.reader(input_file)

    first = True
    for line in csv_reader:
        if first:  # skip the title line
            first = False
            continue
        author_uri = line[1]
        author_name = line[2]
        if author_uri in author_set:
            pass  # author is already registered
        else:
            author_list.append([author_uri, author_name])
            author_set.add(author_uri)

with open('../../data/book20230728/csv/author_label.csv', 'w', encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["author_uri", "author_label"])  # title line
    csv_writer.writerows(author_list)  # store in a CSV file
