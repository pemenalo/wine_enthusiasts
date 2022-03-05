# from crypt import methods
import os
import sys
from flask import Flask, render_template, request
# import tensorflow as tf
# from tensorflow import keras
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
# from keras.models import load_model
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
# from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.models import Model
# from tensorflow.keras.models import load_model
import numpy as np
from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier
from utils import prediction
from utils_w import prediction_w

app = Flask(__name__)


@app.route("/")
def red_calc():
	return render_template("index_r.html")

# @app.route("/sub", methods=['POST'])
@app.route("/white/")
def white_calc():
	return render_template("index_w.html")



@app.route("/sub", methods=['GET', 'POST'])
def submit():
	#return("Working!")
	# HTML to Python file
	if request.method == "POST":
		acidity = float(request.form.get("fixed acidity"))
		volacidity = float(request.form.get("volatile acidity"))
		citric = float(request.form.get("citric acid"))
		res_sugar = float(request.form.get("residual sugar"))
		chlorides = float(request.form.get("chlorides"))
		so2 = float(request.form.get("free sulfure dioxide"))
		tso2 = float(request.form.get("total sulfur dioxide"))
		density = float(request.form.get("density"))
		pH = float(request.form.get("pH"))
		sulphates = float(request.form.get("sulphates"))
		alcohol = float(request.form.get("alcohol"))

		# call preprocessDataAndPredict and pass inputs
		try:
			label=prediction(acidity, volacidity, citric, res_sugar,
        chlorides, so2, tso2, density, pH, sulphates, alcohol)

		 # .py to HTML
			return render_template("submit.html",label = label)

		except ValueError:
			return "Please Enter valid values"
			

	else:
		return render_template('index_r.html')


# White Wine Analysis

@app.route("/sub_w/", methods=['GET', 'POST'])
def submit_white():
	#return("Working!")
	# HTML to Python file
	if request.method == "POST":
		acidity = float(request.form.get("fixed acidity"))
		volacidity = float(request.form.get("volatile acidity"))
		citric = float(request.form.get("citric acid"))
		res_sugar = float(request.form.get("residual sugar"))
		chlorides = float(request.form.get("chlorides"))
		so2 = float(request.form.get("free sulfure dioxide"))
		tso2 = float(request.form.get("total sulfur dioxide"))
		density = float(request.form.get("density"))
		pH = float(request.form.get("pH"))
		sulphates = float(request.form.get("sulphates"))
		alcohol = float(request.form.get("alcohol"))

		# call preprocessDataAndPredict and pass inputs
		try:
			label_w=prediction_w(acidity, volacidity, citric, res_sugar,
        chlorides, so2, tso2, density, pH, sulphates, alcohol)

		 # .py to HTML
			return render_template("submit_w.html",label_w= label_w)

		except ValueError:
			return "Please Enter valid values"

	else:
		return render_template('index_w.html')
			
# def preprocessDataAndPredict(acidity, volacidity, citric, res_sugar, chlorides, so2,tso2,density, pH,sulphates,alcohol):
	
#     #keep all inputs in array
#     test_data = [acidity, volacidity, citric, res_sugar, chlorides, so2,tso2,density, pH,sulphates,alcohol]
#     print(test_data)
	
#     #convert value data into numpy array
#     test_data = np.array(test_data)
	
#     #reshape array
#     test_data = test_data.reshape(1,-1)
#     print(test_data)
	
#     # #load trained model
#     # global graph
#     # graph = tf.get_default_graph()
#     # graph = tf.reset_default_graph()
#     model = load_model('Wine_Enthusiast_Optimization_r.h5')
#     print("Model Loaded")
#     #predict
#     # prediction = model.predict(test_data)
#     # with graph.as_default():
#     # prediction = model.predict(test_data)
  
#     return 2 
# # prediction
	
 
# if __name__== "__main__": 
#   app.run(debug=True)
  