import streamlit as st
import joblib

# load
model = joblib.load(r"C:\Users\malik\Desktop\ML_Revise\10_naive_bayes\model.pkl")
vectorizer = joblib.load(r"C:\Users\malik\Desktop\ML_Revise\10_naive_bayes\vectorizer.pkl")
labels = joblib.load(r"C:\Users\malik\Desktop\ML_Revise\10_naive_bayes\labels.pkl")

# UI
st.title("📧 Email / Text Categorization System")

st.write("Enter text and get predicted category")

user_input = st.text_area("Enter text here")

def predict_text(text):
    text = text.lower()
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec).max()
    return labels[pred], prob

if st.button("Predict"):
    if user_input.strip() != "":
        label, prob = predict_text(user_input)
        
        st.success(f"Prediction: {label}")
        st.info(f"Confidence: {prob:.2f}")
    else:
        st.warning("Please enter some text")