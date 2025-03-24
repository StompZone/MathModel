import numpy as np
import pytest
import tensorflow as tf


@pytest.fixture
def sample_math_data():
    """Fixture providing a small set of sample math operation data."""
    # Create a small deterministic dataset for testing
    X = np.array(
        [
            [5, 3, 1, 0, 0, 0],  # 5 + 3 = 8
            [7, 2, 0, 1, 0, 0],  # 7 - 2 = 5
            [4, 6, 0, 0, 1, 0],  # 4 * 6 = 24
            [10, 2, 0, 0, 0, 1],  # 10 / 2 = 5
        ]
    )
    Y = np.array([8, 5, 24, 5])

    return X, Y


@pytest.fixture
def suppress_tf_logging():
    """Fixture to suppress TensorFlow logging during tests."""
    original_level = tf.get_logger().level
    tf.get_logger().setLevel("ERROR")
    yield
    tf.get_logger().setLevel(original_level)
