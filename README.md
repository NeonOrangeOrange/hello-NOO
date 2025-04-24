# hello-NOO Python Package

This is an example repository for a python package, for my own reference.

PyPi Page: [https://pypi.org/project/hello-NOO/]()
GitHub Pages: [https://neonorangeorange.github.io/hello-NOO/]()
GitHub Repository: [https://github.com/NeonOrangeOrange/hello-NOO]()

---

## Install

Not that you would want to, but you can install with 

```
pip install hello-NOO
```


---

## Development: Things to remember

#### 1. Make a source distribution

```text
python -m build --sdist
```

This makes a `*tar.gz` in the `dist/` folder


#### 2. Make a wheel

```text
python -m build --wheel
```

This makes a `*.whl` in the `dist/` folder

#### 3. Check with twine

```text
twine check dist/*
```

Checks the files in the `dist/` folder

#### 4. Upload to PyPi

```text
twine upload --verbose --repository pypi dist/*
```


---

## Other Notes

```
pip freeze --exlucde hello-NOO | xargs pip uninstall -y
pip uninstall hello-NOO
```

---

## Resources

[https://pypi.org/classifiers/]()

[https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#classifiers]()


