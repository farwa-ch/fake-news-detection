# fake-news-detection
# Fake News Detection System (AI & ML Project)
# AI Fake News Detection System (NLP + Machine Learning)

## 🚀 Project Overview
This project is an end-to-end Machine Learning system that detects whether a news article is **real or fake** using Natural Language Processing (NLP) techniques.  
It also includes a **web-based interactive application** for real-time predictions.

Fake news is a major problem in digital media, and this project demonstrates how AI can be used to address misinformation.

---

## 🎯 Objectives
- Build a machine learning model for text classification
- Apply NLP techniques to process and transform text data
- Compare and evaluate model performance
- Deploy the model using a simple web interface

---

## 🧠 Technologies Used
- Python
- Scikit-learn
- Pandas, NumPy
- NLP (TF-IDF Vectorization)
- Streamlit (Web App)
- Joblib (Model Saving)

---

## ⚙️ Project Pipeline
1. Data Collection (Fake News Dataset from Kaggle)
2. Data Cleaning & Preprocessing
3. Text Vectorization using TF-IDF
4. Model Training (Logistic Regression)
5. Model Evaluation
6. Deployment using Streamlit Web App

---

## 📊 Model Performance
- Achieved high accuracy using Logistic Regression
- Evaluated using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score

---

## 💻 Features
- Input any news article text
- Predicts whether news is REAL or FAKE
- Displays prediction instantly
- Lightweight and easy-to-use web interface

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/train_model.py
streamlit run app/app.py
