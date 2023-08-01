# main016_get_book_genre.py
# get uri of books and their genres with genre names registered in WikiData
# 2023/8/1, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from SPARQLWrapper import SPARQLWrapper, JSON
import csv

sparql_endpoint = SPARQLWrapper('https://query.wikidata.org/sparql')

sparql_query = '''
SELECT ?s ?genre ?genre_label
WHERE {
    ?s wdt:P31 wd:Q7725634;
        wdt:P136 ?genre.
    ?genre rdfs:label ?genre_label .
    FILTER (lang(?genre_label) = "en")
} LIMIT 100000
'''
sparql_endpoint.setQuery(sparql_query)
sparql_endpoint.setReturnFormat(JSON)
query_results = sparql_endpoint.query().convert()
rows = []
for result in query_results["results"]["bindings"]:
    rows.append([result['s']['value'], result['genre']['value'], result['genre_label']['value']])

with open('../../data/book20230728/csv/book_genre.csv', 'w', encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["uri", "genre" "genre_label"])
    csv_writer.writerows(rows)
