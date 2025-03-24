def lr_scheduler(epoch: int, lr: float) -> float:
    """
    Custom learning rate scheduler reducing the learning rate every 10 epochs.

    Args:
        epoch (int): Current epoch number.
        lr (float): Current learning rate.

    Returns:
        float: Adjusted learning rate.
    """
    return lr * 0.5 if epoch > 0 and epoch % 10 == 0 else lr
