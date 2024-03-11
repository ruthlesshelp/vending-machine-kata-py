from payment_processor import PaymentProcessor

def test_make_payment_when_no_payment_expect_payment_eq_0():
    # Arrange
    class_under_test = PaymentProcessor()

    # Act
    actual = class_under_test.get_payment()

    # Assert
    assert actual == 0

def test_make_payment_when_payment_100_expect_payment_eq_100():
    # Arrange
    class_under_test = PaymentProcessor()
    class_under_test.make_payment(100)

    # Act
    actual = class_under_test.get_payment()

    # Assert
    assert actual == 100

def test_is_payment_made_when_no_payment_expect_false():
    # Arrange
    class_under_test = PaymentProcessor()

    # Act
    actual = class_under_test.is_payment_made()

    # Assert
    assert actual == False

def test_is_payment_made_when_payment_of_100_expect_true():
    # Arrange
    class_under_test = PaymentProcessor()
    class_under_test.make_payment(100)

    # Act
    actual = class_under_test.is_payment_made()

    # Assert
    assert actual == True
