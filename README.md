# MathModel

*A neural network model to predict arithmetic operation results.*

## Overview

`MathModel` generates synthetic datasets of arithmetic operations (+, -, *, /) and trains a neural network to accurately predict the results of these operations.

## Installation

### Requirements

- Python >= 3.12
- Poetry (recommended)

### Setup

```bash
poetry install
```

## Usage

### Train the Model

```bash
poetry run python math_model.py
```

### Outputs

After training, the following files are created:

- `trained_math_model.keras` — Trained neural network model.
- `max_input_value.npy` — Scaling factor used for input normalization.

## Author

DJ Stomp ([GitHub](https://github.com/DJStompZone))

## License

[MIT License](LICENSE)