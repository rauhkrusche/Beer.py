[![Build Status](https://travis-ci.org/rauhkrusche/Beer.py.svg?branch=master)](https://travis-ci.org/rauhkrusche/Beer.py)
[![PyPI](https://img.shields.io/pypi/v/Beer.py.svg?maxAge=2592000)](https://pypi.python.org/pypi/Beer.py)

Beer.py
=======

A [Beer](https://github.com/rauhkrusche/Beer) implementation in Python.

## Prerequisites ##
- Python 2.6 or higher

## Installation ##
The easiest way to install Beer.py is to use our [PyPI package](https://pypi.python.org/pypi/Beer.py):

for Python 2:
```
pip install Beer.py
```
or for Python 3:
```
pip3 install Beer.py
```

You can also build Beer.py yourself by executing `setup.py`.

## Usage ##
Simple example:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import beer

if __name__ == "__main__":
	b = beer.Beer

	serialized = b.serialize_beer("Hi");
	// Value: "µµµµµµµµµµµµµµµµ∫BEERBEERBEERBEERBEERBEERBEERBEER∫"

	deserialized = b.deserialize_beer("µµµµµµµµµµµµµµµµ∫BEERBEERBEERBEERBEERBEERBEERBEER∫");
	// Value: "Hi"
```
