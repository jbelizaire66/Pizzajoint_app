#web.py
#
from flask import Flask, render_template, request
from findpizzajoints_api import get_pizza_joint_list
import os



app = Flask(__name__)

@app.route("/")

def index():
	#Initialize variables
	search_radius = 8000 #(approximately 5 miles)
	city_name = request.values.get('city')
	if city_name:
		joint_list = get_pizza_joint_list(city_name, search_radius)
	else:
		joint_list = []
	return render_template("index.html", city=city_name, pizzajointlist=joint_list)

@app.route("/about")

def about():
	return render_template("about.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
	#app.run()