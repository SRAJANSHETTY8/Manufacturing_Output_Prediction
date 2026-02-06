Manufacturing Output Prediction Model
AI powered manufacturing productivity prediction system using Machine Learning and Web Application integration.

Manufacturing Output Prediction is a web based application that uses machine learning to predict hourly production output of injection molding machines based on machine operating parameters. The system allows users to enter machine settings such as temperature, pressure and cycle time, and the model predicts how many parts can be produced per hour.

Overview

Backend
Python FastAPI server using Linear Regression model to predict manufacturing output.

Frontend
Streamlit based user interface that allows users to input machine parameters and view predictions.

Purpose
Predict machine productivity based on operational parameters and help improve production planning and efficiency.

Tech Stack

Frontend
Streamlit  
Python  

Backend
Python  
FastAPI  
NumPy  
Pandas  
Scikit Learn  

Machine Learning
Model Used: Linear Regression  
Dataset: Manufacturing machine performance dataset  

Project Structure

backend  
Contains FastAPI application and prediction API  

frontend  
Contains Streamlit user interface code  

model  
Contains trained machine learning model, scaler and feature list  

training  
Contains training notebook used for building the model  

dataset  
Contains manufacturing dataset used for training  

requirements.txt  
Contains project dependencies  

Quick Start Development

Clone the repository

```
git clone https://github.com/SRAJANSHETTY8/Manufacturing_Output_Prediction.git
cd Manufacturing_Output_Prediction
```

Install dependencies

```
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```

Run Backend Server

```
cd backend
uvicorn main:app --reload
```

Run Frontend Application

```
cd frontend
streamlit run app.py
```

How It Works

User enters machine operating parameters such as injection temperature, pressure, cooling time and material properties.

The frontend sends input values to the backend prediction API.

The backend loads the trained machine learning model and scaler.

Input values are preprocessed and passed to the model.

The model predicts the number of parts that can be produced per hour.

Prediction results are displayed to the user interface.

Dataset Information

The dataset contains historical manufacturing machine performance data. It includes multiple machine parameters that influence productivity. The model learns relationships between machine settings and production output.

Data Preprocessing

Timestamp column was removed as it was not useful for prediction.  
Missing values were handled using mean imputation.  
Categorical variables were converted into numerical format using one hot encoding.  
Feature scaling was applied using standard scaling.  
Dataset was divided into training and testing sets.  

Model Training

The Linear Regression algorithm was used to train the model. The trained model learns the relationship between machine parameters and production output. After training, the model and scaler were saved for deployment.

Application Workflow

Data preprocessing and feature engineering  
Model training and evaluation  
Saving trained model and preprocessing objects  
Backend API development  
Frontend user interface development  
Application testing  

Future Improvements

The system can be enhanced by using advanced machine learning algorithms. Additional manufacturing datasets can improve prediction accuracy. Real time monitoring dashboards and visualization features can also be added in future versions.

Conclusion

This project demonstrates how machine learning can be applied to manufacturing industries to improve productivity and operational decision making. The system provides a complete workflow from data processing to real time prediction through a web application.

Developer

Developed by Srajan Shetty
