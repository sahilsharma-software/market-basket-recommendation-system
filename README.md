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

## 📸 Project Screenshots

### Streamlit UI

<img width="960" height="695" alt="image" src="https://github.com/user-attachments/assets/9d50c2fd-92c1-49d2-a077-2b56d1854ee8" />


### FastAPI API Response

<img width="942" height="119" alt="image" src="https://github.com/user-attachments/assets/01a9596d-4f12-4067-86f7-b880166effc3" />


## 📂 Project Structure

market-basket-analysis
│
├── app
│   └── app.py
│
├── src
│   ├── api.py
│   └── recommend.py
│
├── models
│   └── rules.pkl
│
├── data
│   └── groceries.csv
│
├── notebook
│   └── fp-growth.ipynb
│
├── screenshots
│   ├── ui.png
│   └── api.png
│
├── requirements.txt
│
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
