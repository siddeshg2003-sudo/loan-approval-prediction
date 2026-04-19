import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="ML Prediction App", page_icon="🤖", layout="centered")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 Smart Prediction App</h1>", unsafe_allow_html=True)
st.write("### Enter the values below:")

# Layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    i1 = st.number_input("Age", step=1.0)
    i2 = st.number_input("Anual Income", step=1.0)
    i3 = st.number_input("Spending score", step=1.0)

with col2:
    i4 = st.number_input("Credit score", step=1.0)
    i5 = st.number_input("Loan amount", step=1.0)

# Divider
st.markdown("---")

# Button
if st.button("🔍 Predict", use_container_width=True):
    
    data = np.array([[i1, i2, i3, i4, i5]])
    prediction = model.predict(data)
    
    if prediction[0] == 1:
        st.success("🎉 Congratulations! Your Loan is Approved ✅")
        st.balloons()
    else:
        st.error("⚠️ Sorry! Your Loan is Not Approved ❌")
        

    # Progress bar animation
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ using Streamlit</center>", unsafe_allow_html=True)