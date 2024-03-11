import pytest
from vending_machine import VendingMachine

@pytest.fixture()
def class_under_test():
    return VendingMachine()

def test_release_payment_when_no_payment_expect_no_coins_returned(class_under_test):
    # Arrange

    # Act
    actual = class_under_test.release_quarters()

    # Assert
    assert actual == 0

def test_release_payment_when_3_quarters_inserted_expect_3_coins_returned(class_under_test):
    # Arrange
    expected = 3
    class_under_test.insert_quarters(3)

    # Act
    actual = class_under_test.release_quarters()

    # Assert
    assert actual == expected

def test_select_product_when_no_payment_expect_raise_runtime_error(class_under_test):
    # Arrange

    # Act
    with pytest.raises(RuntimeError) as exception:
        actual = class_under_test.select_product()

    # Assert
    assert exception is not None

def test_select_product_when_4q_payment_expect_product_dispensed_eq_1(class_under_test):
    # Arrange
    class_under_test.insert_quarters(4)

    # Act
    actual = class_under_test.select_product()

    # Assert
    assert actual == 1

def test_display_when_4q_and_product_dispensed_expect_shows_thank_you(class_under_test):
    # Arrange
    expected = 'THANK YOU'
    class_under_test.insert_quarters(4)
    class_under_test.select_product()

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected
