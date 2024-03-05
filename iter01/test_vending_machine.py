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

def test_release_change_when_7_coin_payment_expect_7_coin_returned():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coin(7)

    # Act
    actual = class_under_test.release_change()

    # Assert
    assert actual == 7

def test_display_when_0_coin_payment_expect_display_shows_insert_coin():
    # Arrange
    class_under_test = VendingMachine()

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == 'INSERT COIN'

def test_display_when_1_coin_payment_expect_display_not_insert_coin():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coin(1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual != 'INSERT COIN'
