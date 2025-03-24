from unittest.mock import patch
import runpy


@patch("mathmodel.model_trainer.train_math_model")
def test_main_calls_train_math_model(mock_train_math_model):
    """Test if the main module correctly calls train_math_model."""
    # Run the main module
    runpy.run_module("mathmodel", run_name="__main__")

    # Verify train_math_model was called
    mock_train_math_model.assert_called_once()
