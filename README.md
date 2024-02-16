# Insight Pipeline

Spark ETL pipeline

📦 Pypi: https://test.pypi.org/project/insight-pipeline/

## Data organization

```
data
 --raw (bronze data)
 --ods (Operational data store, silver data)
 --dml (gold data)
```

## Build package

```bash
python3 -m build
```

## Run in local
Note, you need to install `spark`, `java 17` and `hadoop` locally

```bash
python3 ./run.py 
```

## Run tests

```bash
python -m pytest tests/
```

## Publish package

1. Update package version in `pyproject.toml`
2. Create git tag

```bash
git tag 0.0.x
```

3. Push tag to github

```bash
git push origin --tags
```