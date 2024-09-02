import pandas as pd
from elasticsearch import Elasticsearch

csv_path = 'dataset_jobs.csv'

job_df = pd.read_csv(csv_path)
# print(job_df['Title'][0])

# Connection to elasticsearch
client = Elasticsearch(
    'https://localhost:9200',
    basic_auth=('elastics', 'elastic'),
    verify_certs=False
)

doc = dict()

for i in range(len(job_df)):
    doc['Title'] = job_df['Title'][i]
    doc['Description'] = job_df['Description'][i]
    doc['ContractType'] = job_df['ContractType'][i]
    doc['Skills'] = job_df['Skills'][i]

    resp = client.index(index="job-it-senegal", id=i, document=doc)
    print(i)
    print(resp['result'])
    print(doc)
    print()
    doc=dict()

