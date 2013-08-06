# -*- coding: utf-8 -*-


from flask import Flask
from flask.ext.httpcaching import http_caching



app = Flask(__name__)


@app.route("/")
@http_caching(timeout=100)
def home():
    '''
    http response header
    Last-Modified
    will be set
    '''
    return "home"


@app.route("/cache/")
@http_caching(timeout=200, expires=100)
def cache():
    '''
    http response header
    Cache-Control,  Expires, Last-Modified
    will be set
    '''
    return "cache"


if __name__ == '__main__':
    app.run()
