from autots import AutoTS
import pandas as pd
import streamlit as st

# Streamlit title
st.title("Crypto Price Prediction Model")

# Input field for prediction
df = st.text_input("Enter the asset name to predict future prices:")

if df == "ethereum":
    try:
        # Load data
        data = pd.read_csv("data/ETH_USD.csv")
        st.write("Data preview:")
        st.write(data.head())
        
        # Drop missing values
        data = data.dropna()

        # Set up and train the model
        model = AutoTS(forecast_length=5, frequency='infer', ensemble='simple', drop_data_older_than_periods=200, min_allowed_train_percent=0.1)
        model = model.fit(data, date_col='Date', value_col='Price', id_col=None)

        # Generate predictions
        prediction = model.predict()
        forecast = prediction.forecast
        st.write("Forecasted values:")
        st.write(forecast)

    except FileNotFoundError:
        st.error("File not found: Please ensure 'data/ETH_USD.csv' exists in the correct path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")


if df == "Bitcoin":
    try:
        # Load data
        data = pd.read_csv("data/Bitcoin.csv")
        st.write("Data preview:")
        st.write(data.head())
        
        # Drop missing values
        data = data.dropna()

        # Set up and train the model
        model = AutoTS(forecast_length=5, frequency='infer', ensemble='simple', drop_data_older_than_periods=200, min_allowed_train_percent=0.1)
        model = model.fit(data, date_col='Date', value_col='Price', id_col=None)

        # Generate predictions
        prediction = model.predict()
        forecast = prediction.forecast
        st.write("Forecasted values:")
        st.write(forecast)

    except FileNotFoundError:
        st.error("File not found: Please ensure 'data/ETH_USD.csv' exists in the correct path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if df == "Polkadot":
    try:
        # Load data
        data = pd.read_csv("data/Polkadot.csv")
        st.write("Data preview:")
        st.write(data.head())
        
        # Drop missing values
        data = data.dropna()

        # Set up and train the model
        model = AutoTS(forecast_length=5, frequency='infer', ensemble='simple', drop_data_older_than_periods=200, min_allowed_train_percent=0.1)
        model = model.fit(data, date_col='Date', value_col='Close', id_col=None)

        # Generate predictions
        prediction = model.predict()
        forecast = prediction.forecast
        st.write("Forecasted values:")
        st.write(forecast)

    except FileNotFoundError:
        st.error("File not found: Please ensure 'data/ETH_USD.csv' exists in the correct path.")
    except Exception as e:
        st.error(f"An error occurred: {e}")