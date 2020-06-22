import elasticsearch
from elasticsearch import Elasticsearch
import json


# Method to get data from elasticsearch
def get_data_from_es():
 es=Elasticsearch(['localhost:9200'])
 r = es.search(index="songs", body={"query": {"match": {'mainArtist':'Praneeth Perera'}}})
 print(r)
 print(type(r))
 print(r["hits"]["hits"][0]["_source"])

# Main function from where the execution starts
if __name__== "__main__":
 get_data_from_es()