# Import elasticsearch module
from elasticsearch import Elasticsearch 
#import json
# import pandas as pd
#
# songs = pd.read_csv('/home/katta/Desktop/ES/Sinhala_songs.csv')
# songs.fillna("-", inplace=True)
#
#
# print(songs.columns)
# # Method to store data in elasticsearch
# def send_data_to_es(data):
#  es=Elasticsearch(['localhost:9200'])
#  res = es.index(index='employee',doc_type='devops',body=data)
#  print(res)
#
# # Method to get data from elasticsearch
# def get_data_from_es():
#  es=Elasticsearch(['localhost:9200'])
#  r = es.search(index="employee", body={"query": {"match": {'Name':'john'}}})
#  print(r)
#  print(type(r))
#  print(r["hits"]["hits"][0]["_source"])
#
# # Main function from where the execution starts
# if __name__== "__main__":
#  # Define a dictoinary having required data to be stored in ES
#  data = df
#  # Call method to store data in ES
#  send_data_to_es(data)
#  # Call method to get data from ES
#  get_data_from_es()