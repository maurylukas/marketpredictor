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
    retries=3,
    retry_delay_seconds=3
)
def extract_prices(tickers: str, period: str, interval: str) -> pd.DataFrame:
    data = yf.download(tickers=tickers, period=period, interval=interval)
    return data


@task(name="Transform data")
def transform_data(data: pd.DataFrame):
    df = data.sort_values(data.columns[0])
    df['Middle'] = (df['High'] + df['Low']) / 2
    data = df['Middle'].values
    data = data / np.mean(data)
    return data


@task(name="Load model")
def load_model(data, n_times, length_of_sequences, plot_chart) -> float:
    X_train, X_test, y_train, y_test = generate_data(data=data, n_times=n_times, length_of_sequences=length_of_sequences)
    history, improvement = train_model(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)
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
    length_of_sequences = np.random.randint(50, 71, round(len(data)/10))
    improvement = load_model(data=data, n_times=n_times, length_of_sequences=length_of_sequences, plot_chart=False)
    print(f">>> Improvement over benchmark: {improvement}%<<<")


# End of functions

if __name__ == "__main__":
    price_pipeline(
        tickers="BTC-USD",
        period="30d",
        interval="5m",
        n_times=2
    )
