

from elasticsearch import RequestsHttpConnection
from elasticsearch import Elasticsearch
es = Elasticsearch(["localhost"], port="9200", connection_class=RequestsHttpConnection, http_auth=("elastic", "QmpYd7O-Jt-1vZIAO4Bv"), use_ssl=True, verify_certs=False)
# es = Elasticsearch()
# es.indices.create(index="first_index")
# es.indices.exists(index="first_index")

# es.indices.delete(index="first_index")

doc_1 = {"city": "Paris", "country": "France"}
doc_2 = {"city": "Vienna", "country": "Austria"}
doc_3 = {"city": "London", "country": "England"}

es.index(index="cities", doc_type="places", id=1, body=doc_1)
es.index(index="cities", doc_type="places", id=2, body=doc_2)
es.index(index="cities", doc_type="places", id=3, body=doc_3)
res = es
print(res['result'])
# Getting the data

res = es.get(index="cities", doc_type="places", id=1)
print(res)


print(res["_source"])







