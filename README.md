Movie Review Sentiment Analysis App 🎬
An interactive web application built with Python and Streamlit to classify movie reviews as either positive or negative in real-time. This project demonstrates a complete end-to-end Natural Language Processing (NLP) workflow, from data cleaning and model training to deployment.

[➡️ View Live Demo](https://movie-sentiment-analysis-app-sxlgb7nzlfrfvnklfrrah7.streamlit.app)

## Features
Real-Time Sentiment Prediction: Enter any movie review and get an instant sentiment classification.

Simple & Interactive UI: A clean and user-friendly interface powered by Streamlit.

Machine Learning Backend: Utilizes a Logistic Regression model trained on the IMDb movie reviews dataset.

End-to-End Workflow: Showcases all steps from data preprocessing to final deployment.

## Technology Stack
Language: Python 3

Web Framework: Streamlit

Machine Learning: Scikit-learn

Data Manipulation: Pandas

Text Processing: NLTK

Model Serialization: Pickle

## How to Run Locally
To run this application on your local machine, please follow these steps:

Clone the Repository

Bash

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
Create a Virtual Environment (Recommended)

Bash

python -m venv venv
On Windows, activate it with:

Bash

venv\Scripts\activate
On macOS/Linux, activate it with:

Bash

source venv/bin/activate
Install Dependencies
Install all the required libraries from the requirements.txt file.

Bash

pip install -r requirements.txt
Run the Streamlit App

Bash

streamlit run app.py
The application will open in your web browser.

## Project Files
app.py: The main Python script containing the Streamlit web application code.

model.pkl: The serialized, pre-trained Logistic Regression model.

vectorizer.pkl: The serialized TF-IDF vectorizer fitted on the training data.

requirements.txt: A list of all Python libraries required to run the project.

## Model Details
The sentiment classification model is a Logistic Regression classifier trained on the IMDb dataset, which consists of 50,000 movie reviews. The model achieved an accuracy of approximately 89% on the held-out test set.

## License
This project is licensed under the MIT Lice
