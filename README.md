# MathModel

*A neural network model to predict arithmetic operation results.*


 [![GitHub License](https://img.shields.io/github/license/StompZone/MathModel)](LICENSE) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/StompZone/MathModel) ![Static Badge](https://img.shields.io/badge/python-%E2%89%A5%203.12-%2344aa33?style=flat&logo=python&logoColor=%23ffdd00) [![Run Tests](https://github.com/StompZone/MathModel/actions/workflows/test.yml/badge.svg)](https://github.com/StompZone/MathModel/actions/workflows/test.yml) [![Discord](https://img.shields.io/discord/599808270655291403?logo=discord&logoColor=%20%235865F2&label=StompZone%20Discord)](https://discord.stomp.zone)

## Overview

`MathModel` generates synthetic datasets of arithmetic operations (+, -, *, /) and trains a neural network to accurately predict the results of these operations.

## Development

This project uses Poetry for dependency management and pytest for testing.

### Installation

```bash
# Install dependencies
poetry install

# Install development dependencies
poetry install --with dev
```

### Testing

You can run tests locally using:

```bash
# Run all tests
poetry run pytest

# Run tests with coverage and HTML report
poetry run python run_tests.py --coverage --html
```

## Continuous Integration

This project uses GitHub Actions to run tests on every push to the main branch and on pull requests.

### Test Reports

Test reports are automatically generated and published to GitHub Pages after successful runs on the main branch.

You can view the latest test report at:
`https://{username}.github.io/{repository-name}/`

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
