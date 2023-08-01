def inv_uri_genre(global_uri):
    return global_uri.replace('www.wikidata.org/entity', 'localhost/genre/genre_id')


local_uri = inv_uri_genre({})
