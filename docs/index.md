# hello-NOO Python Package

This is an example repository for a python package, for my own reference.

[PyPi Page](https://pypi.org/project/hello-NOO/)

[Documentation (GitHub Pages)](https://neonorangeorange.github.io/hello-NOO/)

[GitHub Repository](https://github.com/NeonOrangeOrange/hello-NOO)

---

## Install

Not that you would want to, but you can install with 

```
pip install hello-NOO
```

Developer install

1. Clone this repository and `cd` into it.
2. Create a virtual environment: `python3 -m venv .venv`
3. Activate the virtual environment: (linux) `source .venv/bin/activate`
4. Install the package locally: (linux) `pip install -e ./[dev,docs]`

---

## Building

```bash
# Build a source distribution (stored in dist/)
python -m build --sdist

# Build a wheel (stored in dist/)
python -m build --wheel

# Run a test to check all the builds in dist
twine check dist/*
```


---

## Upload to PyPi

Once your account is set up, run

```text
twine upload --verbose --repository pypi dist/*
```


---

## Other Notes

To reset the installation

```
pip freeze --exlucde hello-NOO | xargs pip uninstall -y
pip uninstall hello-NOO
```

---

## Resources

<https://pypi.org/classifiers/>

<https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#classifiers>


