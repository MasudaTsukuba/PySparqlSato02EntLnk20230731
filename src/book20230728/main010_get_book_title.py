# main010_get_book_title.py
# get uri of books and their names registered in WikiData
# 2023/8/1, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

from SPARQLWrapper import SPARQLWrapper, JSON
import csv

sparql_endpoint = SPARQLWrapper('https://query.wikidata.org/sparql')  # WikiData endpoint

sparql_query = '''
SELECT ?s ?title
WHERE {
    ?s wdt:P31 wd:Q7725634;
        rdfs:label ?title.
    FILTER(lang(?title) = "en")
} LIMIT 100000
'''
sparql_endpoint.setQuery(sparql_query)  # set query
sparql_endpoint.setReturnFormat(JSON)  # get the results in JSON format
query_results = sparql_endpoint.query().convert()  # execute the query
rows = []  # conver the results into 2D list
for result in query_results["results"]["bindings"]:
    rows.append([result['s']['value'], result['title']['value']])

with open('../../data/book20230728/csv/book_title.csv', 'w', encoding="utf-8") as csvfile:  # store the 2D results into a CSV file
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["uri", "title"])  # title line
    csv_writer.writerows(rows)
