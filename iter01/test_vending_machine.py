from vending_machine import VendingMachine

def test_release_change_when_no_payment_expect_0_returned():
    # Arrange
    class_under_test = VendingMachine()

    # Act
    actual = class_under_test.release_change()

    # Assert
    assert actual == 0

def test_release_change_when_1_coin_payment_expect_1_coin_returned():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coin(1)

    # Act
    actual = class_under_test.release_change()

    # Assert
    assert actual == 1
