from vending_machine import VendingMachine

def test_release_change_when_no_payment_expect_0_returned():
    # Arrange
    class_under_test = VendingMachine()

    # Act
    actual = class_under_test.release_change()

    # Assert
    assert actual == 0
