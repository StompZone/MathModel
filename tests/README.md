# MathModel Tests

This directory contains tests for the MathModel project using pytest.

## Running Tests

To run the tests, install the dev dependencies and run pytest:

```bash
# Install dev dependencies
poetry install --with dev

# Run all tests
poetry run pytest

# Run tests with coverage report
poetry run pytest --cov=mathmodel

# Run specific test file
poetry run pytest tests/test_generate_math_data.py

# Run tests with verbose output
poetry run pytest -v
```

## Test Structure

- `test_generate_math_data.py`: Tests for data generation functionality
- `test_lr_scheduler.py`: Tests for learning rate scheduler
- `test_model_trainer.py`: Tests for model training logic
- `test_main.py`: Tests for the main entry point
- `conftest.py`: Shared fixtures for tests 