import streamlit as st
import joblib

# Load model
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.title("Fake News Detection System")
st.write("Enter a news article to check if it's REAL or FAKE")

text = st.text_area("Enter News Text")

if st.button("Predict"):
    if text:
        vec = vectorizer.transform([text])
        prediction = model.predict(vec)[0]

        if prediction == 1:
            st.error("⚠ FAKE NEWS")
        else:
            st.success("REAL NEWS")
    else:
        st.warning("Please enter text")