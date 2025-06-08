import pandas as pd
import numpy as np
from flask import Flask, render_template, request, url_for
from model import db, Studies
import datetime as dt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studies.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()


@app.route("/", methods=["GET", "POST"])
def landpage():
    studies = Studies.query.all()
    return render_template('landpage_oficial.html', studies=studies)

@app.route("/new", methods=["GET","POST"])
def new():
    Topic = request.form['Topic']
    Date = dt.datetime.today()
    Information = request.form['Information']

    new_study= Studies(Topic,Date,Information)

    db.session.add(new_study)
    db.session.commit()

    return "Ok"

@app.route("/delete/<int:id>")
def delete(id):
    d_study= Studies.query.get_or_404(id)
    db.session.delete(d_study)
    db.session.commit()

    return "HI"


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)