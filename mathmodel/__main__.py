"""
Module: math_model

Generates mathematical operation datasets and trains a neural network model to predict
the result of arithmetic operations. The model uses a multilayer perceptron architecture
with normalization, dropout, and leaky ReLU activation to enhance performance.

Author: DJ Stomp
License: MIT
"""

from mathmodel.model_trainer import train_math_model


if __name__ == "__main__":
    train_math_model()
