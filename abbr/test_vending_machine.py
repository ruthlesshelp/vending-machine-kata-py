from vending_machine import VendingMachine

def test_release_payment_when_no_payment_expect_no_coins_returned():
    # Arrange
    class_under_test = VendingMachine()

    # Act
    actual = class_under_test.release_payment()

    # Assert
    assert actual == 0
