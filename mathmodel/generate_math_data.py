import numpy as np
from numpy._typing import NDArray


def generate_math_data(num_samples: int) -> tuple[NDArray, NDArray]:
    """
    Generate random math operation samples and their results.

    Args:
        num_samples (int): Number of samples to generate.

    Returns:
        tuple: A tuple containing:
            - X (np.ndarray): Feature matrix (operands and one-hot encoded operators).
            - Y (np.ndarray): Result vector.
    """
    operations: list[str] = ["+", "-", "*", "/"]
    X: np.ndarray = np.empty(shape=(0, 6))
    Y: np.ndarray = np.empty(shape=(0, 1))

    while len(Y) < num_samples:
        num1: int = np.random.randint(low=-15, high=16)
        num2: int = np.random.randint(low=-15, high=16)
        op: str = np.random.choice(a=operations)

        if op == "/" and num2 == 0:
            continue

        operator_one_hot: list[int] = [int(op == x) for x in operations]
        features: NDArray[np.int_] = np.array([[num1, num2] + operator_one_hot])

        X = np.vstack(tup=[X, features])

        result = {
            "+": num1 + num2,
            "-": num1 - num2,
            "*": num1 * num2,
            "/": num1 / num2 if num2 != 0 else None,
        }[op]

        Y = np.vstack(tup=[Y, [round(number=result)]])

    X, Y = np.array(object=X), np.array(object=Y).reshape(-1)
    actual_samples = len(Y)
    shuffle_idx: NDArray[np.int_] = np.random.permutation(x=actual_samples)

    return X[shuffle_idx], Y[shuffle_idx]
