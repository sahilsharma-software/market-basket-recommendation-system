# 🛒 Market Basket Recommendation System

This project is a **Market Basket Analysis Recommendation System** built using Machine Learning.
It analyzes customer purchase patterns and recommends products that are frequently bought together.

---

## 🚀 Features

* Product recommendation system
* Association rule mining using FP-Growth
* Interactive UI using Streamlit
* High-performance API using FastAPI
* End-to-end ML pipeline

---

## 🧠 Technologies Used

* Python
* Pandas
* MLxtend
* Streamlit
* FastAPI
* Uvicorn

---

## ⚙️ Project Architecture

User Input (Streamlit UI)
↓
FastAPI Backend
↓
Recommendation Logic
↓
FP-Growth Model
↓
Recommended Products

---

## 📂 Project Structure

market-basket-analysis
│
├── app
│   └── app.py

├── src
│   ├── api.py
│   └── recommend.py

├── models
│   └── rules.pkl

├── data
│   └── groceries.csv

├── notebook
│   └── fp-growth.ipynb

└── README.md

---

## 📊 Model

The recommendation system uses the **FP-Growth algorithm** to find frequent itemsets and generate association rules.

These rules are used to recommend products based on user input.

---

## 🖥️ Running the Project

### 1️⃣ Run FastAPI Backend

uvicorn src.api:app --reload

### 2️⃣ Run Streamlit UI

streamlit run app/app.py

---

## 💡 Example Recommendation

Input Product:
whole milk

Recommended Products:

* rolls/buns
* butter
* ice cream
* brown bread
* pork

---

## 👨‍💻 Author

Sahil Sharma

Machine Learning / AI Enthusiast
