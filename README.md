📦 SupplyPredict — Sales Forecasting & Insight Dashboard

Welcome to SupplyPredict, a complete machine learning solution for forecasting retail category sales — built with a strong business focus, visual storytelling, and a lightweight deployment using Streamlit.

---

🎯 Project Purpose

Retail companies lose millions due to poor inventory planning and unpredictable demand patterns.

SupplyPredict helps business teams:

- Forecast monthly sales for different product categories
- Visualize sales trends across years and quarters
- Identify key demand drivers using feature importance
- Make data-driven decisions with confidence

Whether you're a supply chain manager, retail analyst, or startup founder — this tool gives you an end-to-end analytics pipeline that connects raw data to actionable insights.

---

⚙️ What’s Inside

| Feature                  | Description                               |
| ------------------------ | ----------------------------------------- |
| 📊 Interactive Dashboard | Built with Streamlit and Plotly           |
| 🤖 ML Prediction Engine  | XGBoost model trained on historical sales |
| 📈 Feature Engineering   | Month, Quarter, Category Encoding         |
| 🔍 Exploratory Analysis  | Visualized trends and patterns            |
| 🧠 Model Evaluation      | MAE and RMSE metrics to validate accuracy |
| 💾 Saved Models          | `xgb_sales_model.pkl` + encoders          |
| ⬇️ Forecast CSV Download | Users can download their predictions      |

---

🛠️ Tech Stack

- Python 3.10.12
- Pandas & NumPy for data wrangling
- Matplotlib & Seabornfor EDA
- XGBoost for predictive modeling
- Scikit-learn for preprocessing and evaluation
- Plotly for modern charting
- Streamlit for the web interface

---

🧠 How It Works

1. User uploads monthly sales data (or uses existing)
2. App cleans and engineers features like Month, Quarter, Category
3. Trained XGBoost model predicts future sales
4. Forecasts are visualized and downloadable

📁 Project Structure

SupplyPredict/
├── app.py # Streamlit application
├── models/
│ ├── xgb_sales_model.pkl
│ └── category_encoder.pkl
├── notebooks/
│ └── EDA_and_Modeling.ipynb
├── data/
│ └── sales_data.csv
├── requirements.txt
├── README.md
└── .gitignore

🧾 Sample Use Case
“I’m a regional manager at a retail company. I want to see how Women’s Clothing sales will trend over the next few months based on past data.”

This app allows you to:

Select the product category
View a visual forecast of the next 6 months
Download forecast data for planning meetings
Understand which features influence demand most.

Project: SupplyPredict – Retail Sales Forecasting App
Live Demo: https://supplypredict-9mpcqzertslhpzcutcb5lq.streamlit.app/




What I learnt:

Handling missing data and feature engineering

Label encoding and ML modeling with XGBoost

Model evaluation using MAE & RMSE

Saving and loading .pkl models

Building Streamlit front-end

Deploying ML apps to production with Git & Streamlit Cloud


