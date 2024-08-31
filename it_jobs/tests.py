from datetime import datetime
from elasticsearch import Elasticsearch
client = Elasticsearch(
    'https://localhost:9200',
    basic_auth=('elastics', 'elastic'),
    verify_certs=False
)

doc = {
    'author': 'im s',
    'text': 'Interesting content...',
    'timestamp': datetime.now(),
}
resp = client.index(index="test-indexs", id=2, document=doc)
print(resp['result'])