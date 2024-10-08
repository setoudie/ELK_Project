"""
    Dans ce code on un fichier csv en json  puis onrecupere chaque ligne comme comme un dictionnaire.
    Ce dictionnaire est indexe et stocke dans elasticsearch ou on fera des visualisation avec kibana.
"""
from django.db.models.signals import pre_init
import json
from elasticsearch import Elasticsearch

# Connection to elasticsearch
client = Elasticsearch(
    'https://localhost:9200',
    basic_auth=('elastics', 'elastic'),
    verify_certs=False
)

# Chemin vers le fichier JSON
json_data_path = 'EmploisSenegal_IT_jobs.json'

# Liste pour stocker les documents JSON
json_list = []

# Lire le fichier et ajouter chaque ligne à la liste
with open(json_data_path, 'r') as json_file:
    for line in json_file:
        # Convertir chaque ligne en dictionnaire et ajouter à la liste
        json_list.append(json.loads(line))

# liste des documents JSON
jobs_data = json_list[0]

# Initialisation des variables
i = 0
doc = dict()


for job in jobs_data:
    i+=1
    # print(i)
    # print()
    # print(job)

    # Creat a new dict (doc)
    doc['Title'] = job['Title']
    doc['Description'] = job['Description']
    doc['ContractType'] = job['ContractType']
    doc['Skills'] = job['Skills']

    # print(doc)
    #indexation des donnnes
    resp = client.index(index="job-it-senegal", id=i, document=doc)
    print(resp['result'])
    doc=dict()
    # break
