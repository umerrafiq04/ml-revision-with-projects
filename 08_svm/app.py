import streamlit as st
import numpy as np
from PIL import Image
import joblib

# load model
model = joblib.load(r"C:\Users\malik\Desktop\ML_Revise\08_svm\svm_mnist.pkl")

st.title("🧠 Handwritten Digit Recognition")
st.write("Upload an image of a digit (0–9)")

# upload file
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # open image
    img = Image.open(uploaded_file).convert('L')  # convert to grayscale
    
    # resize to 28x28
    img = img.resize((28, 28))
    
    # display image
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    # convert to numpy array
    img_array = np.array(img)
    
    # invert colors (IMPORTANT for MNIST style)
    img_array = 255 - img_array
    
    # normalize
    img_array = img_array / 255.0
    
    # flatten
    img_array = img_array.reshape(1, -1)
    
    # prediction
    prediction = model.predict(img_array)
    
    st.success(f"Predicted Digit: {prediction[0]}")
    proba = model.decision_function(img_array)
    st.write("Confidence:", np.max(proba))