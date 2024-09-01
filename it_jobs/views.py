from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from elasticsearch import Elasticsearch

def index(request):
    return render(request, 'it_jobs/index.html')

def search_view(request):
    client = Elasticsearch(
        'https://localhost:9200',
        basic_auth=('elastics', 'elastic'),
        verify_certs=False
    )
    query = request.GET.get('q')

    found_data = []
    if query:
        response = client.search(index='job-it-senegal', body={
            "query": {
                "match": {
                    "Description": query
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

