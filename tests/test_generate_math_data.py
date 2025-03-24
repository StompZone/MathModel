import numpy as np

from mathmodel.generate_math_data import generate_math_data


def test_generate_math_data_output_shape():
    """Test if generate_math_data returns arrays of correct shape."""
    num_samples = 100
    X, Y = generate_math_data(num_samples)

    assert isinstance(X, np.ndarray)
    assert isinstance(Y, np.ndarray)
    assert X.shape[0] == num_samples
    assert X.shape[1] == 6  # 2 numbers + 4 one-hot encoded operations
    assert Y.shape[0] == num_samples


def test_generate_math_data_shuffle():
    """Test if generate_math_data properly shuffles the data."""
    num_samples = 1000
    X, Y = generate_math_data(num_samples)

    # Test if the operands and results match the expected operations
    # Extract operands and operation indices
    num1 = X[:, 0]
    num2 = X[:, 1]
    op_idx = np.argmax(X[:, 2:], axis=1)

    # Sample a few indices to verify calculations
    operations = ["+", "-", "*", "/"]
    for i in range(min(20, num_samples)):
        op = operations[op_idx[i]]
        expected_result = {
            "+": num1[i] + num2[i],
            "-": num1[i] - num2[i],
            "*": num1[i] * num2[i],
            "/": num1[i] / num2[i] if num2[i] != 0 else None,
        }[op]

        if op != "/" or num2[i] != 0:
            assert abs(Y[i] - round(expected_result)) < 1e-6


def test_generate_math_data_division_by_zero():
    """Test if generate_math_data handles division by zero correctly."""
    num_samples = 500
    X, Y = generate_math_data(num_samples)

    # Find division operations
    division_indices = np.where(X[:, 5] == 1)[0]

    # Verify no division by zero
    for idx in division_indices:
        assert X[idx, 1] != 0  # Second operand shouldn't be zero for division
