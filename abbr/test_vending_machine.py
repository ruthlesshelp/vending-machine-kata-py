import pytest
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

def test_select_product_when_no_payment_expect_raise_runtime_error():
    # Arrange
    class_under_test = VendingMachine()

    # Act
    with pytest.raises(RuntimeError) as exception:
        actual = class_under_test.select_product()

    # Assert
    assert exception is not None

def test_select_product_when_4q_payment_expect_product_dispensed_eq_1():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_payment(4)

    # Act
    actual = class_under_test.select_product()

    # Assert
    assert actual == 1

def test_display_when_4q_and_product_dispensed_expect_shows_thank_you():
    # Arrange
    expected = 'THANK YOU'
    class_under_test = VendingMachine()
    class_under_test.insert_payment(4)
    class_under_test.select_product()

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected
