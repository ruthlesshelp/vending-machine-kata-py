from payment_processor import PaymentProcessor

def test_make_payment_when_no_payment_expect_payment_eq_0():
    # Arrange
    class_under_test = PaymentProcessor()

    # Act
    actual = class_under_test.payment

    # Assert
    assert actual == 0

def test_make_payment_when_payment_4q_expect_payment_eq_4():
    # Arrange
    class_under_test = PaymentProcessor()
    class_under_test.make_payment(4)

    # Act
    actual = class_under_test.payment

    # Assert
    assert actual == 4

def test_is_payment_made_when_no_payment_expect_false():
    # Arrange
    class_under_test = PaymentProcessor()

    # Act
    actual = class_under_test.is_payment_made()

    # Assert
    assert actual == False

def test_is_payment_made_when_payment_of_4q_expect_true():
    # Arrange
    class_under_test = PaymentProcessor()
    class_under_test.make_payment(4)

    # Act
    actual = class_under_test.is_payment_made()

    # Assert
    assert actual == True
