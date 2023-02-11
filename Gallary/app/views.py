from app import app
from flask import render_template, make_response


@app.after_request
def restful_cros(reshead):
    resp = make_response(reshead)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return reshead


@app.route("/gallery/<int:placeid>")
def gallary(placeid):
    return render_template("gallery.html", placeid=placeid)


@app.route("/map/<int:imageid>/<string:site_name>")
def map(imageid, site_name):
    return render_template("map.html", site_name=site_name)
