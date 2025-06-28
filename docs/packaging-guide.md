# Packaging



### Packaging the project


First you have to make an archive.

```bash
python3 -m build -sdist
```

This is zipped file that contains your package.

You may optionally build a wheel. This can help users install the package faster.

```bash
python3 -m build --wheel
```

### Uploading to PyPi


Content coming soon!



---
## Resources

Tutorial for packaging a project

[https://packaging.python.org/en/latest/tutorials/packaging-projects/](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

Guide to writing `pyproject.toml`

[https://packaging.python.org/en/latest/guides/writing-pyproject-toml/](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

