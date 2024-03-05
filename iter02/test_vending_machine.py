# test_vending_machine.py

from vending_machine import VendingMachine

def test_return_coins_when_no_payment_expect_0_returned():
    # Arrange
    class_under_test = VendingMachine()

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert 'quarters' not in actual

def test_return_coins_when_1_coin_payment_expect_1_coin_returned():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_quarters(1)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual['quarters'] == 1

def test_return_coins_when_7_coin_payment_expect_7_coin_returned():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_quarters(7)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual['quarters'] == 7

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
    class_under_test.insert_quarters(1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual != 'INSERT COIN'

def test_display_when_5_coin_payment_and_return_coins_expect_display_insert_coin():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_quarters(5)
    class_under_test.return_coins()

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == 'INSERT COIN'

def test_display_when_1_quarter_payment_expect_display_0_pt_25():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_quarters(1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.25'

def test_display_when_5_quarter_payment_expect_display_1_pt_25():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_quarters(5)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$1.25'

def test_display_when_1_nickel_payment_expect_display_0_pt_05():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_nickels(1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.05'

def test_display_when_13_nickels_payment_expect_display_0_pt_65():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_nickels(13)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.65'

def test_display_when_1_dime_payment_expect_display_0_pt_10():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_dimes(1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.10'

def test_display_when_43_dimes_payment_expect_display_4_pt_30():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_dimes(43)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$4.30'

def test_display_when_18_nickels_payment_expect_display_0_pt_65():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_nickels(18)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.90'

def test_display_when_4_quarter_payment_expect_display_1_pt_00():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_quarters(4)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$1.00'

def test_return_coins_when_3n_5d_7q_expect_3n_5d_7q_returned():
    # Arrange
    expected = {'nickels': 3, 'dimes': 5, 'quarters': 7}
    class_under_test = VendingMachine()
    class_under_test.insert_nickels(3)
    class_under_test.insert_dimes(5)
    class_under_test.insert_quarters(7)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual == expected

def test_return_coins_when_11_pennies_expect_11_rejects_returned():
    # Arrange
    expected = {'rejects': 11}
    class_under_test = VendingMachine()
    class_under_test.insert_coins('penny', 11)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual == expected