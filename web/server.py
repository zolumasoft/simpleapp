import os
from flask import Flask, render_template

server = Flask(__name__)


@server.route("/")
def home():
    host_name =os.uname().nodename
    return render_template("index.html", hostname=host_name)


@server.route("/health")
def health_status():
    return "App is healthy\n"