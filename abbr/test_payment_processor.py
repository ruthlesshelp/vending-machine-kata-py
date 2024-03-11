from unittest.mock import patch
from payment_processor import PaymentProcessor

@patch("data_access.PaymentDao.retrieve")
def test_make_payment_when_no_payment_expect_payment_eq_0(mock_retrieve):
    # Arrange
    mock_retrieve.return_value = 0
    class_under_test = PaymentProcessor()

    # Act
    actual = class_under_test.get_payment()

    # Assert
    assert actual == 0

@patch("data_access.PaymentDao.save")     # mock arg 2
@patch("data_access.PaymentDao.retrieve") # mock arg 1
def test_make_payment_when_payment_100_expect_payment_eq_100(mock_retrieve, mock_save):
    # Arrange
    mock_save.return_value = None
    mock_retrieve.return_value = 100
    class_under_test = PaymentProcessor()
    class_under_test.make_payment(100)

    # Act
    actual = class_under_test.get_payment()

    # Assert
    assert actual == 100

@patch("data_access.PaymentDao.retrieve")
def test_is_payment_made_when_no_payment_expect_false(mock_retrieve):
    # Arrange
    mock_retrieve.return_value = 0
    class_under_test = PaymentProcessor()

    # Act
    actual = class_under_test.is_payment_made()

    # Assert
    assert actual == False

@patch("data_access.PaymentDao.save")     # mock arg 2
@patch("data_access.PaymentDao.retrieve") # mock arg 1
def test_is_payment_made_when_payment_of_100_expect_true(mock_retrieve, mock_save):
    # Arrange
    mock_save.return_value = None
    mock_retrieve.return_value = 100
    class_under_test = PaymentProcessor()
    class_under_test.make_payment(100)

    # Act
    actual = class_under_test.is_payment_made()

    # Assert
    assert actual == True
