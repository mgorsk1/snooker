# Snooker :black_circle: :red_circle: :white_circle:

[![PyPI version](https://badge.fury.io/py/snooker.svg)](https://badge.fury.io/py/snooker)
![Build Status](https://github.com/mgorsk1/snooker/actions/workflows/release.yml/badge.svg?branch=main)
[![License](http://img.shields.io/:license-Apache%202-blue.svg)](LICENSE)

---

`snooker` is a Python package providing thin wrapper over publicly available API for retrieving Snooker statistics.

### What is Snooker ?

@todo

## Getting started

### Installation

```bash
pip install snooker
```

### Api Usage

#### Snooker Org

```python
from snooker.api import SnookerOrgApi

client = SnookerOrgApi()

player = client.player(5)

print(player)
```

##### Custom headers

Following [snooker.org API documentation](http://api.snooker.org/):

```baazar
If you plan to collect data automatically please contact us so we can agree on what you should put in the header. E.g. "X-Requested-By": "PetersAndroidApp".
```

To achieve this, simply pass appropriate headers when instantiating the client:

```python
from snooker.api import SnookerOrgApi

client = SnookerOrgApi(headers={'X-Requested-By': 'mgorsk1'})
```

#### JSON Data

Returned data is serialized using Python native functionality called `dataclasses`. If you need to convert it to JSON, simply do:

```python
from snooker.api import SnookerOrgApi

client = SnookerOrgApi()

player = client.player(5).to_dict()

print(player)
```
