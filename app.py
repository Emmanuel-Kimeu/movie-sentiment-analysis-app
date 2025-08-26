import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

# --- Pre-load necessary NLTK data ---
# This is a one-time download. Streamlit will cache it.
@st.cache_resource
def download_nltk_data():
    nltk.download('stopwords')
    return set(stopwords.words('english'))

stop_words = download_nltk_data()

# --- Load the saved model and vectorizer ---
try:
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model or vectorizer file not found. Make sure 'vectorizer.pkl' and 'model.pkl' are in the same directory as app.py.")
    st.stop()


# --- Text Cleaning Function (same as in the notebook) ---
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text).lower()
    words = text.split()
    words = [w for w in words if not w in stop_words]
    return ' '.join(words)

# --- Streamlit App Interface ---
st.title("🎬 Movie Review Sentiment Analyzer")
st.write("Enter a movie review below to find out if it's positive or negative!")

# Text input box
user_input = st.text_area("Your Movie Review")

if st.button("Analyze Sentiment"):
    if user_input:
        # 1. Clean the user's input
        cleaned_input = clean_text(user_input)
        
        # 2. Transform the cleaned input using the loaded vectorizer
        input_vector = vectorizer.transform([cleaned_input])
        
        # 3. Make a prediction using the loaded model
        prediction = model.predict(input_vector)
        
        # 4. Display the result
        st.subheader("Analysis Result:")
        if prediction[0] == 1:
            st.success("👍 This looks like a Positive review!")
        else:
            st.error("👎 This looks like a Negative review.")
    else:
        st.warning("Please enter a review to analyze.")