# -*- coding: utf-8 -*-
"""
Created on Sun May 18 01:52:23 2025

@author: micha
"""

    
from flask import Flask, render_template

app = Flask(__name__)

# --- PAGE 1: HOMEPAGE ---
@app.route("/")
def index():
    return render_template("index.html")

# --- PAGE 2: CALCULUS ---
@app.route("/calculus")
def calculus():
    return render_template("calculus.html")

# --- PAGE 3: VECTORS & MATRICES ---
@app.route("/maths")
def maths():
    return render_template("maths.html")

# --- PAGE 4: DISCRETE MATH ---
@app.route("/discrete")
def discrete():
    return render_template("discrete.html")

# --- PAGE 4: BIOGRAPHY  ---
@app.route("/biography")
def biography():
    return render_template("biography.html")

# --- PAGE 5: HTML
@app.route("/math-report")
def math_report():
    # This renders the exact HTML file you knitted in RStudio
    return render_template("meteor_markdown.html")

# --- PAGE 6: HTML
@app.route("/math-report2")
def math_report2():
    # This renders the exact HTML file you knitted in RStudio
    return render_template("covid.html")

@app.route("/cv")
def cv():
    # This renders the exact HTML file you knitted in RStudio
    return render_template("michael_cv_markdown.html")

# --- THE START BUTTON ---
if __name__ == "__main__":
    # use_reloader=False is safer in Spyder to prevent crashes
    app.run(debug=True, use_reloader=False)