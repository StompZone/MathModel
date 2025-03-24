# MathModel

*A neural network model to predict arithmetic operation results.*


 [![GitHub License](https://img.shields.io/github/license/StompZone/MathModel)](LICENSE) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/StompZone/MathModel)](https://github.com/StompZone/MathModel/archive/refs/heads/master.zip) [![Static Badge](https://img.shields.io/badge/python-%E2%89%A5%203.12-%2344aa33?style=flat&logo=python&logoColor=%23ffdd00)](https://github.com/StompZone/MathModel/blob/master/pyproject.toml) [![GitHub commit activity](https://img.shields.io/github/commit-activity/t/stompzone/mathmodel?logo=github&logoColor=%23ccc)](https://github.com/StompZone/MathModel/commits/master/)
 [![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/stompzone/mathmodel/test.yml?logo=github&logoColor=%23ccc&label=tests)](https://stompzone.github.io/MathModel/)
 [![Build Status](https://img.shields.io/github/actions/workflow/status/stompzone/mathmodel/test.yml?style=flat&logo=github)](https://stompzone.github.io/MathModel/)

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

## Usage

### Train the Model

```bash
poetry run python math_model.py
```

### Outputs

After training, the following files are created:

- `trained_math_model.keras` — Trained neural network model.
- `max_input_value.npy` — Scaling factor used for input normalization.


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

<a href="https://stompzone.github.io/MathModel/"><img src="https://img.shields.io/github/actions/workflow/status/stompzone/mathmodel/test.yml?logo=github&logoColor=%23ccc&label=tests&style=for-the-badge" height=25></img></a>

### Test Reports

Test reports are automatically generated and published to GitHub Pages after successful runs on the main branch.

<a href="https://stompzone.github.io/MathModel/"><img src="https://img.shields.io/github/actions/workflow/status/stompzone/mathmodel/test.yml?logo=github&style=for-the-badge&logoColor=%23ccc" height=25></img></a>

## Author

<h4>DJStomp <span><a href="https://github.com/DJStompZone"><img src="https://i.imgur.com/EtL4g49.png" height=16/></a></span></h3>

<a href="https://discord.stomp.zone/"><img src="https://img.shields.io/discord/599808270655291403?logo=discord&logoColor=%20%235865F2&label=Discord&style=for-the-badge" height=25></img></a>

## License

[MIT License](LICENSE)
