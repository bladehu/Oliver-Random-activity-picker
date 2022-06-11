from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from forms import AddActivityForm
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///activities.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)


class ActivitiesDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(1000), unique=True, nullable=False)
    time_of_the_day = db.Column(db.String(200), unique=False, nullable=False)
    type = db.Column(db.String(100), unique=False, nullable=False)
    location = db.Column(db.String(500), unique=False, nullable=True)


db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    form = AddActivityForm()
    if form.validate_on_submit():
        new_activity = ActivitiesDB(
            activity=form.activity.data,
            time_of_the_day=form.time_of_the_day.data,
            type=form.type.data,
            location=form.location.data
        )
        db.session.add(new_activity)
        db.session.commit()
        return redirect(url_for("home"))
    activities = ActivitiesDB.query.all()
    return render_template("index.html", activities=activities, form=form)


@app.route("/pick", methods=["GET", "POST"])
def pick_activity():
    activities = ActivitiesDB.query.all()
    rnd_activity = random.choice(activities)
    return render_template("random-activity.html", activity=rnd_activity)


if __name__ == "__main__":
    app.run(debug=True)
