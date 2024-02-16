# InsightPipeline

Spark pipeline

## Build package

```bash
python3 -m build
```

## Run in local

```bash
python3 ./run.py
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