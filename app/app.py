import streamlit as st
from src.recommend import recommend

st.set_page_config(page_title="Market Basket Recommendation", page_icon="🛒", layout="centered")

st.title("🛒 Market Basket Recommendation System")

st.write("Enter a product and get recommended items based on purchase patterns.")

product = st.text_input("Enter a product")

if st.button("Get Recommendations"):
    
    if product:
        recommendations = recommend(product)

        if recommendations:
            st.subheader("Recommended Products")
            
            for item in recommendations:
                st.write(f"• {item}")
        else:
            st.warning("No recommendations found for this product.")

    else:
        st.warning("Please enter a product first.")