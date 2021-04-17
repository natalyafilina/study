#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask, request

from egcd1 import *

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )


@app.route('/name', methods=['GET', 'POST'])
def hello_name():
    first = request.form.get('first')
    second = request.form.get('second')

    if first is None:
        first = "0"

    if second is None:
        second = "0"

    return flask.render_template(
        'name.html',
        answ=result(first, second),
        method=request.method
    )

if __name__ == '__main__':
    app.run(debug=True)
