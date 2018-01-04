from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('food.json') as food_data:
        data = json.load(food_data)

def get_vitamins():
     category = ""
        
        
@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/vitamins")
def render_stats():
    return render_template('vitamins.html')

@app.route("/minerals")
def render_minerals():
    return render_template('minerals.html')
    
@app.route("/pie")
def render_pie():
        return render_template('piechart.html')


if __name__=="__main__":
    app.run(debug=True, port=54321)
