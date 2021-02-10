import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    lines = ["<h1>Hello World!</h1>"]
    if os.environ.get("MY_ENV_VAR"):
        lines.append(os.environ.get("MY_ENV_VAR"))

    return "\n".join(lines)
