# test_vending_machine.py

from vending_machine import VendingMachine, Coin

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
    class_under_test.insert_coins(Coin.QUARTER, 1)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual['quarters'] == 1

def test_return_coins_when_7_coin_payment_expect_7_coin_returned():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 7)

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
    class_under_test.insert_coins(Coin.QUARTER, 1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual != 'INSERT COIN'

def test_display_when_5_coin_payment_and_return_coins_expect_display_insert_coin():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 5)
    class_under_test.return_coins()

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == 'INSERT COIN'

def test_display_when_1_quarter_payment_expect_display_0_pt_25():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.25'

def test_display_when_5_quarter_payment_expect_display_1_pt_25():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 5)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$1.25'

def test_display_when_1_nickel_payment_expect_display_0_pt_05():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.NICKEL, 1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.05'

def test_display_when_13_nickels_payment_expect_display_0_pt_65():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.NICKEL, 13)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.65'

def test_display_when_1_dime_payment_expect_display_0_pt_10():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.DIME, 1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.10'

def test_display_when_43_dimes_payment_expect_display_4_pt_30():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.DIME, 43)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$4.30'

def test_display_when_18_nickels_payment_expect_display_0_pt_65():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.NICKEL, 18)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.90'

def test_display_when_4_quarter_payment_expect_display_1_pt_00():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 4)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$1.00'

def test_return_coins_when_3n_5d_7q_expect_3n_5d_7q_returned():
    # Arrange
    expected = {'nickels': 3, 'dimes': 5, 'quarters': 7}
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.NICKEL, 3)
    class_under_test.insert_coins(Coin.DIME, 5)
    class_under_test.insert_coins(Coin.QUARTER, 7)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual == expected

def test_return_coins_when_11_pennies_expect_11_rejects_returned():
    # Arrange
    expected = {'rejects': 11}
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.PENNY, 11)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual == expected

def test_return_coins_when_17_slugs_expect_17_rejects_returned():
    # Arrange
    expected = {'rejects': 17}
    class_under_test = VendingMachine()
    class_under_test.insert_coins('plug nickel', 5)
    class_under_test.insert_coins('blank slug', 12)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual == expected

def test_display_coins_when_137n_83d_41q_expect_display_has_25_pt_40():
    # Arrange
    expected = '$25.40'
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.NICKEL, 137)
    class_under_test.insert_coins(Coin.DIME, 83)
    class_under_test.insert_coins(Coin.QUARTER, 41)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_select_cola_with_payment_4_quarters_expect_1_cola_is_dispensed():
    # Arrange
    expected = { 'cola': 1 }
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 4)

    # Act
    actual = class_under_test.select_cola()

    # Assert
    assert actual == expected

def test_display_when_4q_and_select_cola_expect_display_thank_you():
    # Arrange
    expected = 'THANK YOU'
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 4)
    class_under_test.select_cola()

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_select_cola_with_payment_4_quarters_expect_1_cola_is_dispensed():
    # Arrange
    expected = { }
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 3)

    # Act
    actual = class_under_test.select_cola()

    # Assert
    assert actual == expected

def test_display_when_4q_and_select_cola_and_check_display_expect_next_display_insert_coin():
    # Arrange
    expected = 'INSERT COIN'
    class_under_test = VendingMachine()
    class_under_test.insert_coins(Coin.QUARTER, 4)
    class_under_test.select_cola()
    current_display = class_under_test.display
    assert current_display == 'THANK YOU'

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected
