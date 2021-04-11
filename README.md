# Snooker :black_circle: :red_circle: :white_circle:

[![PyPI version](https://badge.fury.io/py/snooker.svg)](https://badge.fury.io/py/snooker)
![Build Status](https://github.com/mgorsk1/snooker/actions/workflows/release.yml/badge.svg?branch=main)
[![License](http://img.shields.io/:license-Apache%202-blue.svg)](LICENSE)

---

`snooker` is a Python package providing thin wrapper over publicly available API for retrieving Snooker statistics.

### What is Snooker ?

Following [Wikipedia's definition](https://en.wikipedia.org/wiki/Snooker):

 > Snooker (pronounced UK: /ˈsnuːkər/, US: /ˈsnʊkər/)[2][3] is a cue sport that was first played by British Army officers stationed in India in the second half of the 19th century. It is played on a rectangular table covered with a green cloth (or "baize"), with six pockets: one at each corner and one in the middle of each long side. Using a cue stick, the players[a] take turns to strike the white "cue ball" to pot the other twenty-one snooker balls in the correct sequence, accumulating points for each pot. An individual frame of snooker is won by the player who has scored the most points by the end of the frame. A snooker match ends with one of the players having won a predetermined number of frames, thus winning the match.

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

> If you plan to collect data automatically please contact us so we can agree on what you should put in the header. E.g. "X-Requested-By": "PetersAndroidApp".

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
