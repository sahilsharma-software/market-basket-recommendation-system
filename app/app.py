import streamlit as st
import requests

st.title("🛒 Market Basket Recommendation System")

product = st.text_input("Enter a product")

if st.button("Get Recommendations"):

    url = f"http://127.0.0.1:8000/recommend/{product}"

    response = requests.get(url)

    data = response.json()

    recommendations = data["recommendations"]

    if recommendations:
        st.subheader("Recommended Products")

        for item in recommendations:
            st.write("👉", item)

    else:
        st.write("No recommendations found")