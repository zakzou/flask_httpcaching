Flask-HttpCaching
======================

http caching


## install

```shell

easy_install flask_httpcaching

pip install flask_httpcaching
```

## Usage

```python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.httpcaching import http_caching


app = Flask(__name__)

@app.route("/")
@http_caching(timeout=300, expires=20)
def home():
    return "home"


if __name__ == '__main__':
    app.run()
```
