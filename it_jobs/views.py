from dataclasses import field

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from elasticsearch import Elasticsearch

# view de la page de Home
def index(request):
    return render(request, 'it_jobs/index.html')


# view pour chercher un document par keyword
def search_view(request):
    # Configuration pour la connection a elastic
    client = Elasticsearch(
        'https://localhost:9200',
        basic_auth=('elastics', 'elastic'),
        verify_certs=False
    )
    keyword = request.GET.get('keywords')

    found_data = []
    if keyword:
        # response = client.search(index='job-it-senegal', body={
        #     "query": {
        #         "match": {
        #             "Description": query
        #         }
        #     }
        # })

        response = client.search(index='job-it-senegal', body={
            "query":{
                "multi_match": {
                    "query": f"{keyword}",
                    "fields":["Title", "Description", "Skills", "ContractType"]
                }
            }
        })
        # print(response)
        results = response['hits']['hits']
        # print(results)
        for i in range(len(results)):
            found_data.append(results[i]['_source'])
        # print(len(found_data), found_data)

    return render(request, 'it_jobs/search.html', {'found_datas': found_data})

# Creation de la view pour afficher le dashboard
def dashboard(request):
    return render(request, 'it_jobs/dashboard.html')