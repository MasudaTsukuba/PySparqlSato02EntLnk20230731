def uri_genre(local_uri):
    return local_uri.replace('localhost/genre/genre_id', 'www.wikidata.org/entity')


uri_results = uri_genre({})
