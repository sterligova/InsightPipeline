# Projet final : *InsightPipeline*
## Irina STERLIGOVA & David LECONTE - POEI Jems/LePont

Spark ETL pipeline

L'objectif principal de ce projet est de fournir un pipeline spark qui soit flexible et qui puisse être modifié en fonction des différentes options de traitement des données. L'accent est mis sur la simplicité et la logique du pipeline et de ses configurations, ce qui permet de l'adapter facilement en fonction des besoins de l'utilisateur. 

## Architecture du code et étapes clés

Pour faciliter l'utilisation du code et l'ajout rapide des modifications nécessaires à chaque projet, chaque étape du pipeline a été placée dans un fichier Python indépendant. 

```
src\insight_pipeline_package
 --ingest.py (fonction de lecture des données)
 --load.py (fonction de téléchargement des données )
 --pipeline_congig.py (une classe qui définit les paramètres de configuration: spark session name, raw data file location, path to operational data store (ods) layer, path to data mart layer, column name for data aggregation sum etc.
  
 --spark_pipeline.py (principale fonction exécutive de la pipeline)
 --transform.py (fonctions de traitement et d'agrégation des données)
 --utils.py (Démarrer et arrêter une session spark)

```
Les étapes clés: 

- lancement de la session spark
- lecture des données brutes
- traitement et agrégation des données
- téléchargement des données vers la couche nécessaire


### Documentation

Les dossiers **src** et **tests** contiennent respectivement une documentation du package et de la suite de tests.

### Stockage des données

Les données finales seront stockées au format CSV.

Le dossier **data** est structuré de manière à ce qu'à l'intérieur, le dossier **raw** puisse stocker les .csv bruts, le dossier **ods** (operational data store) puisse stocker les .csv nettoyés, et le dossier **dml** (data mart layer) puisse stocker les vues métiers .csv.

```
data
 --raw (bronze data)
 --ods (Operational data store, silver data)
 --dml (Data mart layer, gold data)
```

### Choix du langage

Nous avons établi qu'il était suffisant, plus simple et par conséquent plus efficace d'utiliser *Python* pour ce projet.

### CI/CD

Dans notre suite de tests, nous vérifions à chaque fois  à chaque fois si les dataframes créés contiennent des données sans doublons et que toutes les lignes contiennent des valeurs.

Un workflow Github Actions vérifie si les tests sont validés correctement à chaque opération *push*.

À chaque push sur la branche *main*, un workflow Github Actions publie le package .whl contenant la pipeline.

📦 Pypi: https://test.pypi.org/project/insight-pipeline/


## Dev section

### Build package

```bash
python3 -m build
```

### Run in local

La version de démo a été utilisée pour tester localement l'opérabilité du code.
Note, you need to install `spark`, `java 17` and `hadoop` locally

```bash
python3 ./demo.py 
```

### Run tests

```bash
python -m pytest tests/
```

### Publish package

1. Update package version in `pyproject.toml`
2. Create git tag

```bash
git tag 0.0.x
```

3. Push tag to github

```bash
git push origin --tags
```