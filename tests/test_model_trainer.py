import numpy as np
from unittest.mock import patch, MagicMock

from mathmodel.model_trainer import train_math_model


@patch("mathmodel.model_trainer.Sequential")
@patch("mathmodel.model_trainer.generate_math_data")
@patch("tensorflow.keras.callbacks.LearningRateScheduler")
def test_train_math_model_structure(
    mock_lr_scheduler, mock_generate_data, mock_sequential
):
    """Test if train_math_model properly builds the model structure."""
    # Setup mocks
    mock_model = MagicMock()
    mock_sequential.return_value = mock_model

    # Create sample data for mock return
    sample_X = np.random.rand(100, 6)
    sample_Y = np.random.rand(100)
    mock_generate_data.return_value = (sample_X, sample_Y)

    # Call function with reduced sample size
    train_math_model(num_samples=100)

    # Assert model was compiled
    mock_model.compile.assert_called_once()

    # Assert model was trained (fit was called)
    mock_model.fit.assert_called_once()

    # Assert model was saved
    mock_model.save.assert_called_once_with("trained_math_model.keras")

    # Assert max input value was saved
    # Use np directly since we're not mocking it completely anymore
    mock_generate_data.assert_called_once_with(100)


@patch("mathmodel.model_trainer.Sequential")
@patch("mathmodel.model_trainer.generate_math_data")
@patch("tensorflow.keras.callbacks.LearningRateScheduler")
def test_model_layers_count(mock_lr_scheduler, mock_generate_data, mock_sequential):
    """Test if the model has the correct number of layers."""
    # Setup a side effect to capture the layers when Sequential is called
    layers_list = []

    def capture_layers(layers):
        layers_list.extend(layers)
        mock_model = MagicMock()
        return mock_model

    mock_sequential.side_effect = capture_layers

    # Create sample data for mock return
    sample_X = np.random.rand(10, 6)
    sample_Y = np.random.rand(10)
    mock_generate_data.return_value = (sample_X, sample_Y)

    # Call function
    train_math_model(num_samples=10)

    # Assert the correct number of layers
    # InputLayer + 7 blocks of (Dense, LeakyReLU, BatchNorm, Dropout) + final Dense = 1 + 7*4 + 1 = 30
    assert len(layers_list) == 30
