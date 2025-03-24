"""
Module: model_trainer

Contains the training logic for the mathematical operation prediction model.
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import (
    BatchNormalization,
    Dense,
    Dropout,
    InputLayer,
    LeakyReLU,
)
from tensorflow.keras.optimizers import Adam


from mathmodel.generate_math_data import generate_math_data
from mathmodel.lr_scheduler import lr_scheduler

Sequential = tf.keras.models.Sequential


def train_math_model(num_samples: int = 175000) -> None:
    """
    Generate data, build, and train the math prediction neural network model.

    Args:
        num_samples (int, optional): Total samples to generate and use for training.
            Defaults to 175,000.
    """
    X, Y = generate_math_data(num_samples)

    max_input_value: int = np.max(a=np.abs(X[:, :2]))
    X[:, :2] /= max_input_value

    model: Sequential = Sequential(
        [
            InputLayer(input_shape=(X.shape[1],)),
            Dense(units=400, kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            LeakyReLU(),
            BatchNormalization(),
            Dropout(rate=0.2),
            Dense(units=200, kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            LeakyReLU(),
            BatchNormalization(),
            Dropout(rate=0.2),
            Dense(units=100, kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            LeakyReLU(),
            BatchNormalization(),
            Dropout(rate=0.2),
            Dense(units=50, kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            LeakyReLU(),
            BatchNormalization(),
            Dropout(rate=0.2),
            Dense(units=25, kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            LeakyReLU(),
            BatchNormalization(),
            Dropout(rate=0.2),
            Dense(units=15, kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            LeakyReLU(),
            BatchNormalization(),
            Dropout(rate=0.2),
            Dense(units=10, kernel_regularizer=tf.keras.regularizers.l2(0.01)),
            LeakyReLU(),
            BatchNormalization(),
            Dropout(rate=0.2),
            Dense(units=1),
        ]
    )

    model.compile(optimizer=Adam(0.001), loss="mse", metrics=["mae"])

    model.fit(
        X,
        Y,
        epochs=100,
        batch_size=128,
        callbacks=[tf.keras.callbacks.LearningRateScheduler(schedule=lr_scheduler)],
        validation_split=0.1,
    )

    model.save("trained_math_model.keras")
    np.save(file="max_input_value.npy", arr=max_input_value)
