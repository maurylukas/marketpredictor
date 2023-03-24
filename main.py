# Start of imports
import pandas as pd
import numpy as np
import yfinance as yf
from prefect import task, flow
from process import generate_data
from model import train_model
from plot import plot_loss
# End of imports

# Start of functions


@task(
    name="Extract prices",
    retries=3,  # Number of retries if fails
    retry_delay_seconds=3   # Delay before retry
)
def extract_prices(tickers: str, period: str, interval: str) -> pd.DataFrame:
    # Fetch the market prices from yfinance API
    data = yf.download(tickers=tickers, period=period, interval=interval)

    return data


@task(name="Transform data")
def transform_data(data: pd.DataFrame):
    # Make sure the values are in correct order
    df = data.sort_values(data.columns[0])

    # Calculate the average prices
    df['Middle'] = (df['High'] + df['Low']) / 2

    data = df['Middle'].values

    # Normalize the data by dividing by the mean value
    data = data / np.mean(data)

    return data


@task(name="Load model")
def load_model(data, n_times, length_of_sequences, plot_chart) -> float:
    # Generate  the data to use on model
    X_train, X_test, y_train, y_test = generate_data(data=data, n_times=n_times, length_of_sequences=length_of_sequences)

    # Train and evaluate model
    history, improvement = train_model(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

    # Plot chart if needed, default is False
    if plot_chart:
        plot_loss(history)

    return improvement


@flow(name="Price pipeline")
def price_pipeline(tickers: str, period: str, interval: str, n_times: int):
    print(">>> Extracting prices <<<")
    df = extract_prices(tickers=tickers, period=period, interval=interval)

    print(">>> Transforming data<<<")
    data = transform_data(df)

    print(">>> Loading model <<<")
    # Generate 1/10 of the data length number of sequences of size between 50 and 70
    length_of_sequences = np.random.randint(50, 71, round(len(data)/10))

    # If plot chart is wanted, change 'plot_chart' to True in the next line
    improvement = load_model(data=data, n_times=n_times, length_of_sequences=length_of_sequences, plot_chart=False)
    print(f">>> Improvement over benchmark: {improvement}%<<<")


# End of functions

if __name__ == "__main__":
    price_pipeline(
        tickers="BTC-USD",  # Here goes the market ticker
        period="30d",   # Here goes the time period
        interval="5m",  # Here goes the time interval
        n_times=2   # Here goes the amount to predict
    )

# Instructions on how to deploy with Prefect are commented in the end of the plot.py file
