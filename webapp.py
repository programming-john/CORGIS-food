from flask import Flask, url_for, render_template, request, Markup, flash
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('food.json') as food_data:
        data = json.load(food_data)

def get_food_names():
	options = ""
	
	for food in data:
		options += Markup("<option value=" +'"'+ food["Description"] +'">'+ food["Description"] + "</option>")
    
	return options

	
def get_vit_fact(name):
	fact = ""
	for food in data:
		if name == food["Description"]:
			fact += Markup("<p><b>"+ food["Description"] + "</b></p>")
			fact += Markup("<p>"+"Vitamin A - IU: " + str(food["Data"]["Vitamins"]["Vitamin A - IU"]) + "</p>")
			fact += Markup("<p>"+"Vitamin A - RAE: " + str(food["Data"]["Vitamins"]["Vitamin A - RAE"])+"</p>")
			fact += Markup("<p>"+ "Vitamin B12: " + str(food["Data"]["Vitamins"]["Vitamin B12"]) + "</p>")
			fact += Markup("<p>"+"Vitamin B6: " + str(food["Data"]["Vitamins"]["Vitamin B6"])+"</p>")
			fact += Markup("<p>"+"Vitamin C: " + str(food["Data"]["Vitamins"]["Vitamin C"])+"</p>")
			fact += Markup("<p>"+"Vitamin E: " + str(food["Data"]["Vitamins"]["Vitamin E"])+"</p>")
			fact += Markup("<p>"+"Vitamin K: " + str(food["Data"]["Vitamins"]["Vitamin K"])+"</p>")
			
	return fact
	
def get_min_fact(name):
	fact = ""
	for food in data:
		if name == food["Description"]:
			fact += Markup("<p><b>"+ food["Description"] + "</b></p>")
			fact += Markup("<p>"+ "Calcium: " + str(food["Data"]["Major Minerals"]["Calcium"]) + "</p>")
			fact += Markup("<p>"+ "Copper: " + str(food["Data"]["Major Minerals"]["Copper"]) + "</p>")
			fact += Markup("<p>"+ "Iron: " + str(food["Data"]["Major Minerals"]["Iron"]) + "</p>")
			fact += Markup("<p>"+ "Magnesium: " + str(food["Data"]["Major Minerals"]["Magnesium"]) + "</p>")
			fact += Markup("<p>"+ "Phosphorus: " + str(food["Data"]["Major Minerals"]["Phosphorus"]) + "</p>")
			fact += Markup("<p>"+ "Potassium: " + str(food["Data"]["Major Minerals"]["Potassium"]) + "</p>")
			fact += Markup("<p>"+ "Sodium: " + str(food["Data"]["Major Minerals"]["Sodium"]) + "</p>")
			fact += Markup("<p>"+ "Zinc: " + str(food["Data"]["Major Minerals"]["Zinc"]) + "</p>")
			
			
	return fact
	

def get_vitamins():
     options = "memes"
     return options    
        

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/vitamins")
def render_stats():

    return render_template('vitamins.html', Vitamins = get_food_names())

@app.route("/minerals")
def render_minerals():
    return render_template('minerals.html', MajorMinerals = get_food_names())
    
@app.route("/pie")
def render_pie():
    return render_template('piechart.html', Goose = get_food_names())

@app.route("/go", methods=['GET','POST'])
def render_vitamininfo():
    place = request.args['vits']
    return render_template('vitamins.html', info = get_vit_fact(place), Vitamins = get_food_names())
	
@app.route("/yargg", methods=['GET','POST'])
def render_mineralinfo():
    place = request.args['mins']
    return render_template('minerals.html', info = get_min_fact(place), MajorMinerals = get_food_names())
		
		
		
if __name__=="__main__":
    app.run(debug=True, port=54321)
