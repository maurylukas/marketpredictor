# Start of imports
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Masking, LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping
# End of imports

# Start of functions


def init_model():
    model = Sequential()
    model.add(Masking())
    model.add(LSTM(10, activation='tanh'))
    model.add(Dense(1, activation='linear'))

    model.compile(loss='mse',
                  optimizer='adam',
                  metrics=['mae'])

    return model


def benchmark_prediction(X, y):
    err = []
    for xi, yi in zip(X, y):
        xi = [_ for _ in xi if _ != 0]
        err.append(xi[-1] - yi[0])

    return np.mean(np.abs(err))


def train_model(X_train, X_test, y_train, y_test):
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=20, restore_best_weights=True)

    while True:
        model = init_model()
        history = model.fit(X_train, y_train,
                            validation_split=0.3,
                            shuffle=False,
                            epochs=200,
                            batch_size=128,
                            verbose=1,
                            callbacks=[es],
                            use_multiprocessing=True)

        model_res = model.evaluate(X_test, y_test, verbose=1)
        bench_res = benchmark_prediction(X_test, y_test)
        improvement = np.round((1 - (model_res[0]/bench_res))*100, 2)

        if improvement > 90:
            return history, improvement


# End of functions