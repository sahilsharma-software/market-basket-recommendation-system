import streamlit as st
import sys
import os

# project root path add karna
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.recommend import recommend


st.set_page_config(page_title="Market Basket Recommendation", page_icon="🛒")

st.title("🛒 Market Basket Recommendation System")

product = st.text_input("Enter a product")

if st.button("Get Recommendations"):

    if product:
        recommendations = recommend(product)

        if recommendations:
            st.subheader("Recommended Products")

            for item in recommendations:
                st.write("•", item)
        else:
            st.warning("No recommendations found")

    else:
        st.warning("Please enter a product")