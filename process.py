# Start of imports
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
# End of imports

# Start of functions


def get_sample(data, length, temporal_horizon):
    temporal_horizon = temporal_horizon - 1
    last_possible = np.abs(len(data) - temporal_horizon - length)
    random_start = np.random.randint(0, last_possible)
    X_sample = data[random_start: random_start + length]
    X_sample = [[_] for _ in X_sample]

    y_sample = data[random_start + length + temporal_horizon]

    return X_sample, y_sample


def get_X_y(data, temporal_horizon, length_of_sequences):
    X, y = [], []
    for len_ in length_of_sequences:
        xi, yi = get_sample(data, len_, temporal_horizon)
        X.append(xi)
        y.append([yi])

    y = np.array(y)

    return X, y


def generate_data(data, n_times, length_of_sequences):
    X, y = get_X_y(data=data, temporal_horizon=n_times, length_of_sequences=length_of_sequences)

    X_pad = pad_sequences(X, padding='post', value=0, dtype='float32')

    n_train = int(0.7 * len(X_pad))

    X_train, X_test = X_pad[:n_train, :], X_pad[n_train:, :]
    y_train, y_test = y[:n_train], y[n_train:]

    return X_train, X_test, y_train, y_test


# End of functions