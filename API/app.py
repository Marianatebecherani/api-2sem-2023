from flask import Flask, render_template

app = Flask('__name__')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/atividadepratica")
def atividadepratica():
    return render_template("atividadepratica.html")

@app.route("/burndownchart")
def burndownchart():
    return render_template("burndownchart.html")

@app.route("/dailyscrum")
def dailyscrum():
    return render_template("dailyscrum.html")

@app.route("/estruturatime")
def estruturatime():
    return render_template("estruturatime.html")

@app.route("/planningpoker")
def planningpoker():
    return render_template("planningpoker.html")

@app.route("/processbacklog")
def processbacklog():
    return render_template("processbacklog.html")

@app.route("/productbacklog")
def product_backlog():
    return render_template("productbacklog.html")

@app.route("/sprintplanning")
def sprintplanning():
    return render_template("sprintplanning.html")

@app.route("/sprintretrospective")
def sprin_retrospective():
    return render_template("sprintretrospective.html")


