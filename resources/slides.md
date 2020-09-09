---
title: pyPackaging
version: 1.0.0
paginate: true
size: 4K
marp: false
header: pyPackaging
footer: Gisolfi
theme: dracula
---


# Python Packaging

From the basics to publishing packages on PyPI. Plus a bit of **Swagger**

Daniel Nicolas Gisolfi

![bg left](./img/package.jpg)

---

# What's it all for? 🤔

- Creates a simpler process for distributing packages (hopefully) 
- Allows developers to build upon tools
- Forces you to follow at least some of the python standard
 - Follow [PEP8](https://www.python.org/dev/peps/pep-0008/)!

--- 

# The Basics - `__init__.py`

*Q: What's an `__init__.py` for?*

```
coffee
├── LICENSE
├── README.md
├── coffee
│ └── __init__.py
└── setup.py
```

*A: Is required to import the directory as a package*

[Python Docs](https://docs.python.org/3/reference/import.html#regular-packages)

---

# The Basics - `setup.py`

*Q: What's a `setup.py` for?*

```
coffee
├── LICENSE
├── README.md
├── coffee
│ └── __init__.py
└── setup.py
```

*A: is the build script for your package. It tells setuptools about your package and which code files to include.*

---

# The Basics - `setup.py`
```python
from setuptools import setup, find_packages

if __name__ == "__main__":
 setup(
 name=coffee.__title__,
 version=coffee.__version__,
 author=coffee.__author__,
 author_email=coffee.__author_email__,
 description=coffee.__description__,
 license=coffee.__license__,
 packages=setuptools.find_packages(),
 )
```




--- 

# Defining Dependencies

A Requirements.txt file is very simple Ex:

```
setuptools >= 21.0.0
```
How can we define dependencies for:
- Testing
- Development
- Production

---
# Requirements.txt

```
coffee
├── LICENSE
├── README.md
├── coffee
│ └── __init__.py
├── test
│ └── __init__.py
├── requirements.txt
├── test-requirements.txt
├── dev-requirements.txt
└── setup.py
```

**This is getting messy...**

---

# Pipfiles


```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
twine = "*"

[packages]
click = "*"

[requires]
python_version = "3.7"
```

---

# What makes this better?

- You can define separate collections of requirements
- Packages can be specified from separate pypi repositories
- Creates a virtual env and manages it for you

![bg right](./img/dependency.jpg)

---

# Demo 

** Let's take a look at the example coffee package!**

[Check it out here](https://github.com/dgisolfi/PythonPackaging)

![bg right](./img/coffee.jpg)

---

# Swagger

*Q: Why are you derailing this talk to focus on swagger?*

> A specification for machine-readable interface files for describing, producing, consuming, and visualizing RESTful web services. - Wikipedia

*A: It's important...trust me*

[Swagger Editor](https://editor.swagger.io)

---

# Twine

Now that we have a package, how do we publish it?


```
python3 -m twine upload dist/*
```

Upload to a private or public PyPI repository.

![bg right](./img/twine.jpg)

---

# Questions?

<style scoped>
h1 {
 padding-top: 210px;
 text-align: center;
}
</style>

---
# Advice

* Write code.
* Write a tool that is useful to you in some capacity
    * [MKP](https://github.com/dgisolfi/mkp) - The multidimensional 0–1 knapsack problem solved using a greedy algorithm.
    * [RotatingProxyBot](https://github.com/dgisolfi/RotatingProxyBot) - A Bot that uses a Rotating Proxy to simulate many clients making a request to a single server