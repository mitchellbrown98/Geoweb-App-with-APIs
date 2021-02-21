import os

from flask import Flask, session, render_template, request, flash, json, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import requests

app = Flask(__name__)

# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def home():
    info=[]
    info.append("none")
    info.append("none")

    return render_template("index.html", info=info)

@app.route("/search", methods=["POST"])
def search():
    startdate = request.form.get("datepicker")
    enddate = request.form.get("datepicker2")

    #convert date input to api param format
    sd = startdate.replace("/", "-")
    ed = enddate.replace("/", "-")
    url = "https://data.calgary.ca/resource/c2es-76ed.geojson?$where=issueddate > " + "'" + sd + "' " + "and issueddate < " + "'" + ed + "'"

    res = requests.get(url)
    #convert the response to a Json object
    rep = res.json()
    rep2=rep['features']

    #send date info for results
    info=[]
    info.append(sd)
    info.append(ed)


    return render_template("index.html", rep2=rep2, info=info)
