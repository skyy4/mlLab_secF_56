import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("Gender Prediction Based on Facial Features")

# Input fields for each feature
long_hair = st.radio("Long Hair", ("Not Long Hair", "Long Hair"))
forehead_width_cm = st.number_input("Forehead Width (cm)", min_value=0.0, step=0.1)
forehead_height_cm = st.number_input("Forehead Height (cm)", min_value=0.0, step=0.1)
nose_wide = st.radio("Wide Nose", ("Not Wide Nose", "Wide Nose"))
nose_long = st.radio("Long Nose", ("Not Long Nose", "Long Nose"))
lips_thin = st.radio("Thin Lips", ("Not Thin Lips", "Thin Lips"))
distance_nose_to_lip_long = st.radio("Long Distance Between Nose and Lips", ("Short Distance", "Long Distance"))

# Convert inputs into appropriate format for prediction
long_hair = 1 if long_hair == "Long Hair" else 0
nose_wide = 1 if nose_wide == "Wide Nose" else 0
nose_long = 1 if nose_long == "Long Nose" else 0
lips_thin = 1 if lips_thin == "Thin Lips" else 0
distance_nose_to_lip_long = 1 if distance_nose_to_lip_long == "Long Distance" else 0

# Model prediction when the user clicks the button
if st.button("Predict Gender"):
    features = np.array([[long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]])
    
    # Make prediction
    prediction = model.predict(features)
    
    # Display the prediction result
    if prediction == 1:
        st.success("The predicted gender is: Female")
    else:
        st.success("The predicted gender is: Male")
