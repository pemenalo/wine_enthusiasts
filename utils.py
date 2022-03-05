from joblib import load

def prediction(acidity, volacidity, citric, res_sugar,
        chlorides, so2, tso2, density, pH, sulphates, alcohol):
	#return("Working!")
	# HTML to Python file
	
		# call preprocessDataAndPredict and pass inputs
			# prediction = preprocessDataAndPredict(acidity, volacidity, citric, res_sugar, chlorides, so2,tso2,density, pH,sulphates,alcohol)
			# ----

    # keep all inputs in array
    test_data = [acidity, volacidity, citric, res_sugar,
        chlorides, so2, tso2, density, pH, sulphates, alcohol]
    print(test_data)

# convert value data into numpy array
    # test_data = np.array(test_data)

# reshape array
    # test_data = test_data.reshape(1, -1)


# #load trained model

    # model = load_model('Wine_Enthusiast_Optimization_r_2.h5')
    model = load('Wine_Enthusiast_RF_r.joblib')
    scaler = load('scaler_RF_r.joblib')
    print("Model Loaded")
    # test_data = preprocess_input(test_data, mode='tf')
# predict    
    prediction = model.predict(scaler.transform([test_data]))
    # scaler.transform([clean_df_r.iloc[3,0:11].to_list()])
    # prediction = str(prediction).lstrip('[').rstrip(']')
    # print(f"Prediction Value: {prediction}")
    # print(scaler.transform(test_data))


    # ----

    # .py to HTML
    # return render_template("submit.html",prediction = prediction)
    return prediction[0]




if __name__ == '__main__':
    print(prediction(1,2,3,4,5,6,7,8,9,10,11))