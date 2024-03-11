from vending_machine import VendingMachine

def test_release_payment_when_no_payment_expect_no_coins_returned():
    # Arrange
    class_under_test = VendingMachine()

    # Act
    actual = class_under_test.release_payment()

    # Assert
    assert actual == 0

def test_release_payment_when_3_quarters_inserted_expect_3_coins_returned():
    # Arrange
    expected = 3
    class_under_test = VendingMachine()
    class_under_test.insert_payment(3)

    # Act
    actual = class_under_test.release_payment()

    # Assert
    assert actual == expected

def test_select_product_when_no_payment_expect_no_product_dispensed():
    # Arrange
    class_under_test = VendingMachine()

    # Act
    actual = class_under_test.select_product()

    # Assert
    assert actual == 0
