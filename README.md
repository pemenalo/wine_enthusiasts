# Project 4 - Wine Quality Predictor
### Group Project on Machine Learning Integration
## Project Team
-   Rudy Duvnjak 
-   Alex Lorin 
-   Prince Emenalo
-   Joby Augustine
## Project Description
Develop a machine learning model to predict the quality of wine based on the following characteristics: 
Fixed Acidity,
Volatile Acidity
Citric Acid, 
Residual Sugar, 
Chlorides,
Free Sulfur Dioxide, 
Total Sulfur Dioxide, 
Density, 
pH, 
Sulphates,  and Alcohol.
## Development Process
### Data Analysis Preparation
Data is gathered from [here](https://archive.ics.uci.edu/ml/datasets/wine+quality)
For Red and White wine data, two separate .csv files are used.
Red Wine Data - /Wine_Data/winequality-red%20(1).csv
White Wine Data  - /Wine_Data/winequality-white.csv
Data is analysed and prepared using 
-   Jupyter Notebook 
-   Python 
-   Pandas libraries.
Scikit Learn is used for the development of different machine learning models and testing.
Developed models using these algorithms to get a model with high accuracy.
-  K Nearest Neighbors
- Neural Network Model
- Support Vector Machine 
- Random Forest Classifier 
Developed a Random Forest Model with high accuracy in determining the quality.
Model is tested, evaluate and saved for prediction.
### Web Development 
Using Flask and  HTML/CSS, web page is developed which can be used to input the wine features for prediction.
User is able to input features for the Red wine and White Wine for prediction.
Good quality wine will be predicted as 1.
The application for Wine Prediction is deployed with Heroku.
## Conclusion
After analyzing the data and with the Wine Quality Predictor model, the model is able to predict correctly the quality of wine.
Many features contribute to the quality of the wine. 
Different models were used to predict the quality. The greatest accuracy was with the Random Forest Model.
With the Wine Quality Predictor, we can predict the quality of the wine with 80% accuracy.
