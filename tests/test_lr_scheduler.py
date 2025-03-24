from mathmodel.lr_scheduler import lr_scheduler


def test_lr_scheduler_reduction():
    """Test if lr_scheduler reduces learning rate at 10th epoch intervals."""
    initial_lr = 0.001

    # Learning rate should remain the same for epochs 0-9
    for epoch in range(10):
        assert lr_scheduler(epoch, initial_lr) == initial_lr

    # Learning rate should be reduced at epoch 10
    assert lr_scheduler(10, initial_lr) == initial_lr * 0.5

    # Learning rate should remain the same for epochs 11-19
    for epoch in range(11, 20):
        assert lr_scheduler(epoch, initial_lr * 0.5) == initial_lr * 0.5

    # Learning rate should be reduced again at epoch 20
    assert lr_scheduler(20, initial_lr * 0.5) == initial_lr * 0.25


def test_lr_scheduler_multiple_reductions():
    """Test if lr_scheduler correctly applies multiple reductions."""
    initial_lr = 0.01
    expected_lr = initial_lr

    for epoch in range(51):
        current_lr = lr_scheduler(epoch, expected_lr)

        if epoch > 0 and epoch % 10 == 0:
            expected_lr *= 0.5

        assert current_lr == expected_lr
