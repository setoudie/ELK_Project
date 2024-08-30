**Seny Toutou DIEDHIOU** \
**ODC DEV DATA P6**

# Projet : Moteur de Recherche des Offres d'Emploi IT avec Django

Ce projet consiste à récupérer, traiter, et analyser des offres d'emploi IT depuis l'API Microsoft LinkedIn, puis à les stocker dans Elasticsearch. Enfin, un tableau de bord sera créé dans Kibana pour visualiser les tendances des données collectées.

## Prérequis

- **Python 3.11**
- **Django**
- **Elasticsearch** (Local ou Cloud)
- **Kibana** (pour la visualisation)
- **API Microsoft LinkedIn**
- **Bibliothèques Python :**
  - `elasticsearch`
  - `pandas`
  - `requests`
  - `django`

## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/setoudie/ELK_Project.git

   cd ELK_Project
   ```

2. **Créer et activer un environnement virtuel :**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données Elasticsearch :**

   Assurez-vous qu'Elasticsearch est installé et configuré correctement sur votre machine ou dans le cloud.

## Structure du Projet

```
├── ELK_project/                 # Répertoire principal du projet Django
│   ├── ELK_project/             # Répertoire de configuration Django
│   ├── it_jobs/                 # App Django pour gérer les jobs IT
│   ├── Data/                    # Repertoire contenant les donnnes scrapes
│   ├── templates/               # Répertoire pour les templates HTML
│   ├── manage.py                # Commande de gestion Django
│   ├── requirements.txt         # Liste des dépendances Python
│   └── README.md                # Documentation du projet
├── venv/                        # Environnement virtuel
```

## Configuration de l'API LinkedIn

- **Obtenir une clé API** : 
  Obtenez les informations nécessaires (clé API, secrets, etc.) via la plateforme Microsoft LinkedIn pour accéder aux données des offres d'emploi IT.

- **Configurer l'accès API** :
  Créez un fichier `.env` dans le répertoire principal pour stocker les informations d'accès à l'API :

  ```bash
  LINKEDIN_API_KEY=<votre_cle_api>
  ```

## Fonctionnalités

### 1. Récupération des Données

Un script Python, intégré dans l'application Django, envoie des requêtes à l'API Microsoft LinkedIn pour récupérer les offres d'emploi IT au format JSON.

```python
import requests

response = requests.get("https://api.linkedin.com/v2/jobSearch", headers={"Authorization": "Bearer <votre_cle_api>"})
job_data = response.json()
```

### 2. Traitement des Données

Les données récupérées sont traitées pour correspondre aux exigences d'indexation dans Elasticsearch.

### 3. Indexation des Données dans Elasticsearch

Une fois traitées, les données sont indexées dans Elasticsearch directement via un modèle Django ou un service dédié.

```python
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])

# Exemple de document
job_data = {
    "job_title": "Data Engineer",
    "company": "Tech Company",
    "location": "Dakar",
    "salary": 1200000,
    "date_posted": "2024-08-30"
}

# Indexer un document
es.index(index='it-jobs-index', body=job_data)
```

### 4. Création de Modèles Django

Des modèles Django sont créés pour représenter les données récupérées et stockées dans Elasticsearch.

```python
from django.db import models

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.IntegerField()
    date_posted = models.DateTimeField()
```

### 5. Visualisation des Données dans Kibana

Kibana est utilisé pour visualiser les données stockées dans Elasticsearch. Des graphiques et des tableaux de bord sont créés pour montrer les tendances des offres d'emploi IT.

## Exécution

1. **Démarrer le serveur Django :**

   ```bash
   python manage.py runserver
   ```

2. **Exécuter le script de récupération et d'indexation des données :**

   ```bash
   python manage.py fetch_jobs_data
   ```

3. **Visualiser les données dans Kibana :**

   Accédez à Kibana via votre navigateur et configurez des visualisations pour les données indexées.

## Conclusion

Ce projet permet de créer un moteur de recherche spécialisé pour les offres d'emploi IT en utilisant l'API de Microsoft LinkedIn, Django pour la gestion des données, Elasticsearch pour l'indexation, et Kibana pour la visualisation.
```