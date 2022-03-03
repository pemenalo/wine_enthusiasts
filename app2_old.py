from crypt import methods
from flask import Flask,render_template,request
import tensorflow as tf
# import keras
# from keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

# @app.route("/sub", methods=['POST'])
@app.route("/sub", methods=['GET','POST'])
def submit():   

    # HTML to Python file
    if request.method == "POST":
        name = request.form["username"]
        acidity = request.form["fixed acidity"]
        volacidity = request.form["volatile acidity"]
        citric = request.form["citric acid"]
        res_sugar = request.form["residual sugar"]
        chlorides = request.form["chlorides"]
        so2 = request.form["free sulfure dioxide"]
        tso2 = request.form["total sulfur dioxide"]
        density = request.form["density"]
        pH = request.form["pH"]
        sulphates = request.form["sulphates"]
        alcohol = request.form["alcohol"]
        
        #call preprocessDataAndPredict and pass inputs
        try:
            # prediction = preprocessDataAndPredict(acidity, volacidity, citric, res_sugar, chlorides, so2,tso2,density, pH,sulphates,alcohol)
            # ----
            
            #keep all inputs in array
            test_data = [acidity, volacidity, citric, res_sugar, chlorides, so2,tso2,density, pH,sulphates,alcohol]
            print(test_data)
    
    #convert value data into numpy array
            test_data = np.array(test_data)
    
    #reshape array
            test_data = test_data.reshape(1,-1)
            print(test_data)
    
    # #load trained model
      
            model = load_model('Wine_Enthusiast_Optimization_r.h5')
            print("Model Loaded")
    #predict
            prediction = model.predict(test_data)
            print(prediction)
            
            # ----
         
         
         
         #.py to HTML
            return render_template("submit.html",n=name,prediction = prediction)
   
        except ValueError:
            return "Please Enter valid values"
        
    pass
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
    
 
if __name__== "__main__": 
  app.run(debug=True)
  