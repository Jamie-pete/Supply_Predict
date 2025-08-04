import streamlit as st
import plotly.express as px
import joblib
import pandas as pd
from datetime import datetime

# Load model + encoder
model = joblib.load('models/xgb_sales_model.pkl')
encoder = joblib.load('models/category_encoder.pkl')

st.title("📦 Supply Chain Sales Forecasting")

# Input fields
category = st.selectbox("Select Product Category", ['WomenClothing', 'MenClothing', 'OtherClothing'])
month = st.selectbox("Select Month", list(range(1, 13)))
year = st.selectbox("Select Year", list(range(2023, 2026)))

# Feature engineering
quarter = (month - 1) // 3 + 1
category_code = encoder.transform([category])[0]

# Prediction
input_df = pd.DataFrame({
    'Month_Num': [month],
    'Quarter': [quarter],
    'Year': [year],
    'Category_Code': [category_code]
})

if st.button("Predict Sales"):
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Predicted Sales: ${prediction:.2f}K")

    st.success(f"💰 Predicted Sales for {category} in {month}/{year}: **${prediction:.2f}K**")

    # --- Forecast next 6 months
    st.subheader("📊 6-Month Forecast")

    forecast_data = []
    forecast_month = month
    forecast_year = year

    for i in range(6):
        forecast_quarter = (forecast_month - 1) // 3 + 1
        category_code = encoder.transform([category])[0]

        input_row = pd.DataFrame({
            'Month_Num': [forecast_month],
            'Quarter': [forecast_quarter],
            'Year': [forecast_year],
            'Category_Code': [category_code]
        })

        pred = model.predict(input_row)[0]
        forecast_data.append({
            'Month': f"{forecast_month}-{forecast_year}",
            'Sales': pred
        })

        # Move to next month
        forecast_month += 1
        if forecast_month > 12:
            forecast_month = 1
            forecast_year += 1

    forecast_df = pd.DataFrame(forecast_data)

    import plotly.express as px

# Plotly chart
    fig = px.line(forecast_df, x='Month', y='Sales', markers=True,
              title='📈 6-Month Sales Forecast',
              labels={'Sales': 'Predicted Sales ($K)', 'Month': 'Month-Year'},
              template='plotly_white')

    st.plotly_chart(fig, use_container_width=True)