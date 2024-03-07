# test_vending_machine.py

import pytest

from vending_machine import VendingMachine, CoinName, Product

# This function runs once, at the start of this module
@pytest.fixture(scope="module")
def vending_machine_instance():
    # before all setup
    initial_stock = { 'cola': 103, 'chips': 157, 'candy': 59 }
    vending_machine = VendingMachine(stock=initial_stock)
    yield vending_machine
    # after all tear down

# This function runs before each test function
@pytest.fixture(scope="function")
def class_under_test(vending_machine_instance) -> VendingMachine:
    # before test setup
    vending_machine_instance._reset()
    return vending_machine_instance

def test_return_coins_when_no_payment_expect_0_returned(class_under_test):
    # Arrange
    class_under_test.return_coins()

    # Act
    actual = class_under_test.coin_return

    # Assert
    assert 'quarter' not in actual

def test_return_coins_when_1_coin_payment_expect_1_coin_returned(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.QUARTER, 1)
    class_under_test.return_coins()

    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual['quarter'] == 1

def test_return_coins_when_7_coin_payment_expect_7_coin_returned(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.QUARTER, 7)
    class_under_test.return_coins()

    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual['quarter'] == 7

def test_display_when_0_coin_payment_expect_display_shows_insert_coin(class_under_test):
    # Arrange

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == 'INSERT COIN'

def test_display_when_1_coin_payment_expect_display_not_insert_coin(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.QUARTER, 1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual != 'INSERT COIN'

def test_display_when_5_coin_payment_and_return_coins_expect_display_insert_coin(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.QUARTER, 5)
    class_under_test.return_coins()

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == 'INSERT COIN'

def test_display_when_1_quarter_payment_expect_display_0_pt_25(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.QUARTER, 1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.25'

def test_display_when_5_quarter_payment_expect_display_1_pt_25(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.QUARTER, 5)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$1.25'

def test_display_when_1_nickel_payment_expect_display_0_pt_05(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.NICKEL, 1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.05'

def test_display_when_13_nickels_payment_expect_display_0_pt_65(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.NICKEL, 13)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.65'

def test_display_when_1_dime_payment_expect_display_0_pt_10(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.DIME, 1)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.10'

def test_display_when_43_dimes_payment_expect_display_4_pt_30(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.DIME, 43)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$4.30'

def test_display_when_18_nickels_payment_expect_display_0_pt_65(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.NICKEL, 18)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$0.90'

def test_display_when_4_quarter_payment_expect_display_1_pt_00(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.QUARTER, 4)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == '$1.00'

def test_return_coins_when_3n_5d_7q_expect_3n_5d_7q_returned(class_under_test):
    # Arrange
    expected = {'nickel': 3, 'dime': 5, 'quarter': 7}
    class_under_test.insert_coins(CoinName.NICKEL, 3)
    class_under_test.insert_coins(CoinName.DIME, 5)
    class_under_test.insert_coins(CoinName.QUARTER, 7)
    class_under_test.return_coins()

    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual == expected

def test_return_coins_when_11_pennies_expect_11_rejects_returned(class_under_test):
    # Arrange
    expected = {'reject': 11}
    class_under_test.insert_coins(CoinName.PENNY, 11)
    class_under_test.return_coins()

    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual == expected

def test_return_coins_when_17_slugs_expect_17_rejects_returned(class_under_test):
    # Arrange
    expected = {'reject': 17}
    class_under_test.insert_coins('plug nickel', 5)
    class_under_test.insert_coins('blank slug', 12)
    class_under_test.return_coins()

    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual == expected

def test_display_coins_when_137n_83d_41q_expect_display_has_25_pt_40(class_under_test):
    # Arrange
    expected = '$25.40'
    class_under_test.insert_coins(CoinName.NICKEL, 137)
    class_under_test.insert_coins(CoinName.DIME, 83)
    class_under_test.insert_coins(CoinName.QUARTER, 41)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_select_cola_with_payment_4_quarters_expect_1_cola_is_dispensed(class_under_test):
    # Arrange
    expected = { 'cola': 1 }
    class_under_test.insert_coins(CoinName.QUARTER, 4)
    class_under_test.select_product(Product.COLA)

    # Act
    actual = class_under_test.output_box

    # Assert
    assert actual == expected

def test_display_when_4q_and_select_cola_expect_display_thank_you(class_under_test):
    # Arrange
    expected = 'THANK YOU'
    class_under_test.insert_coins(CoinName.QUARTER, 4)
    class_under_test.select_product(Product.COLA)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_select_cola_with_payment_3_quarters_expect_nothing_is_dispensed(class_under_test):
    # Arrange
    expected = { }
    class_under_test.insert_coins(CoinName.QUARTER, 3)
    class_under_test.select_product(Product.COLA)

    # Act
    actual = class_under_test.output_box

    # Assert
    assert actual == expected

def test_display_when_4q_and_select_cola_and_check_display_expect_next_display_insert_coin(class_under_test):
    # Arrange
    expected = 'INSERT COIN'
    class_under_test.insert_coins(CoinName.QUARTER, 4)
    class_under_test.select_product(Product.COLA)
    current_display = class_under_test.display
    assert current_display == 'THANK YOU'

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_current_amount_when_4q_and_select_cola_and_check_display_twice_expect_current_amount_0_pt_00(class_under_test):
    # Arrange
    expected = '$0.00'
    class_under_test.insert_coins(CoinName.QUARTER, 4)
    class_under_test.select_product(Product.COLA)
    current_display = class_under_test.display
    assert current_display == 'THANK YOU'
    current_display = class_under_test.display
    assert current_display == 'INSERT COIN'

    # Act
    actual = class_under_test.current_amount

    # Assert
    assert actual == expected

def test_display_when_3q_and_select_cola_expect_display_shows_price_1_pt_00(class_under_test):
    # Arrange
    expected = 'PRICE $1.00'
    class_under_test.insert_coins(CoinName.QUARTER, 3)
    assert class_under_test.current_amount == '$0.75'
    class_under_test.select_product(Product.COLA)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_display_when_payment_3q_select_cola_and_check_display_expect_next_display_is_insert_coin(class_under_test):
    # Arrange
    expected = 'INSERT COIN'
    class_under_test.insert_coins(CoinName.QUARTER, 3)
    class_under_test.select_product(Product.COLA)
    current_display = class_under_test.display
    assert current_display == 'PRICE $1.00'

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_current_amount_when_payment_3q_select_cola_and_check_display_expect_current_amount_shows_0_pt_75(class_under_test):
    # Arrange
    expected = '$0.75'
    class_under_test.insert_coins(CoinName.QUARTER, 3)
    class_under_test.select_product(Product.COLA)
    current_display = class_under_test.display
    assert current_display == 'PRICE $1.00'

    # Act
    actual = class_under_test.current_amount

    # Assert
    assert actual == expected

def test_select_chips_when_payment_2q_select_chips_expect_1_chips_dispensed(class_under_test):
    # Arrange
    expected = { 'chips': 1 }
    class_under_test.insert_coins(CoinName.QUARTER, 2)
    class_under_test.select_product(Product.CHIPS)
    
    # Act
    actual = class_under_test.output_box

    # Assert
    assert actual == expected

def test_display_when_payment_2q_and_chips_expect_display_shows_thank_you(class_under_test):
    # Arrange
    expected = 'THANK YOU'
    class_under_test.insert_coins(CoinName.QUARTER, 2)
    class_under_test.select_product(Product.CHIPS)
    output = class_under_test.output_box
    assert output == { 'chips': 1 }

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_select_chips_when_payment_3n_and_select_chips_expect_no_chips_dispensed(class_under_test):
    # Arrange
    expected = {}
    class_under_test.insert_coins(CoinName.NICKEL, 3)
    class_under_test.select_product(Product.CHIPS)

    # Act
    actual = class_under_test.output_box

    # Assert
    assert actual == expected

def test_display_when_payment_3n_and_select_chips_expect_display_not_thank_you(class_under_test):
    # Arrange
    class_under_test.insert_coins(CoinName.NICKEL, 3)
    class_under_test.select_product(Product.CHIPS)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual != 'THANK YOU'

def test_current_amount_when_payment_5d_and_select_chips_expect_current_amount_is_0_pt_00(class_under_test):
    # Arrange
    expected = '$0.00'
    class_under_test.insert_coins(CoinName.DIME, 5)
    class_under_test.select_product(Product.CHIPS)

    # Act
    actual = class_under_test.current_amount

    # Assert
    assert actual == expected

def test_display_when_payment_2q_1d_1n_and_select_candy_expect_1_candy_dispensed(class_under_test):
    # Arrange
    expected = { 'candy': 1 }
    class_under_test.insert_coins(CoinName.QUARTER, 2)
    class_under_test.insert_coins(CoinName.DIME, 1)
    class_under_test.insert_coins(CoinName.NICKEL, 1)
    class_under_test.select_product(Product.CANDY)
    
    # Act
    actual = class_under_test.output_box

    # Assert
    assert actual == expected

def test_display_when_payment_2q_1d_1n_and_select_candy_expect_display_shows_thank_you(class_under_test):
    # Arrange
    expected = 'THANK YOU'
    class_under_test.insert_coins(CoinName.QUARTER, 2)
    class_under_test.insert_coins(CoinName.DIME, 1)
    class_under_test.insert_coins(CoinName.NICKEL, 1)
    class_under_test.select_product(Product.CANDY)    

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_select_candy_when_payment_1q_1d_expect_no_candy_dispensed(class_under_test):
    # Arrange
    expected = {}
    class_under_test.insert_coins(CoinName.QUARTER, 1)
    class_under_test.insert_coins(CoinName.DIME, 1)
    class_under_test.select_product(Product.CANDY)

    # Act
    actual = class_under_test.output_box

    # Assert
    assert actual == expected

def test_current_amount_when_payment_2q_1d_1n_and_select_candy_and_display_ty_expect_display_0_pt_00(class_under_test):
    # Arrange
    expected = '$0.00'
    class_under_test.insert_coins(CoinName.QUARTER, 2)
    class_under_test.insert_coins(CoinName.DIME, 1)
    class_under_test.insert_coins(CoinName.NICKEL, 1)
    class_under_test.select_product(Product.CANDY)
    output = class_under_test.output_box
    assert output == { 'candy': 1 }
    message = class_under_test.display
    assert message == 'THANK YOU'

    # Act
    actual = class_under_test.current_amount

    # Assert
    assert actual == expected

def test_display_when_payment_2q_and_select_candy_expect_display_is_price_0_pt_65(class_under_test):
    # Arrange
    expected = "PRICE $0.65"
    class_under_test.insert_coins(CoinName.QUARTER, 2)
    class_under_test.select_product(Product.CANDY)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_display_when_payment_3d_and_select_chips_expect_display_is_price_0_pt_50(class_under_test):
    # Arrange
    expected = "PRICE $0.50"
    class_under_test.insert_coins(CoinName.DIME, 3)
    class_under_test.select_product(Product.CHIPS)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_coin_return_when_payment_7q_and_select_chips_expect_coin_return_has_5q(class_under_test):
    # Arrange
    expected = { 'quarter': 5 }
    class_under_test.insert_coins(CoinName.QUARTER, 7)
    class_under_test.select_product(Product.CHIPS)

    # Act
    actual = class_under_test.coin_return

    # Arrange
    assert actual == expected

def test_coin_return_when_payment_9d_and_select_chips_expect_coin_return_has_1q_1d_1n(class_under_test):
    # Arrange
    expected = { 'quarter': 1, 'dime': 1, 'nickel': 1 }
    class_under_test.insert_coins(CoinName.DIME, 9)
    class_under_test.select_product(Product.CHIPS)

    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual == expected

def test_coin_return_when_payment_1q_and_select_chips_and_display_shows_0_pt_50_expect_coin_return_is_empty(class_under_test):
    # Arrange
    expected = {}
    class_under_test.insert_coins(CoinName.QUARTER, 1)
    class_under_test.select_product(Product.CHIPS)
    display = class_under_test.display
    assert display == 'PRICE $0.50'

    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual == expected

def test_coin_return_when_payment_3q_1d_select_candy_expect_coin_return_has_2d(class_under_test):
    # Arrange
    expected = { 'dime': 2 }
    class_under_test.insert_coins(CoinName.QUARTER, 3)
    class_under_test.insert_coins(CoinName.DIME, 1)
    class_under_test.select_product(Product.CANDY)
    
    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual == expected

def test_coin_return_when_payment_7919q_7829d_7723n_select_candy_expect_coin_return_has_12592q_1d_1n(class_under_test):
    # Arrange
    expected = { 'quarter': 12592, 'dime': 1, 'nickel': 1 } # used Excel to determine this expected return
    class_under_test.insert_coins(CoinName.QUARTER, 7919)
    class_under_test.insert_coins(CoinName.DIME, 7829)
    class_under_test.insert_coins(CoinName.NICKEL, 7723)
    class_under_test.select_product(Product.CANDY)
    
    # Act
    actual = class_under_test.coin_return

    # Assert
    assert actual == expected

def test_display_when_chips_qty_0_and_payment_3q_and_select_chips_expect_display_shows_out_of_stock(class_under_test):
    # Arrange
    expected = 'OUT OF STOCK'
    class_under_test._stock['chips'] = 0
    class_under_test.insert_coins(CoinName.QUARTER, 1)
    class_under_test.select_product(Product.CHIPS)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_display_when_soda_qty_0_and_pay_5q_and_select_soda_expect_display_shows_out_of_stock(class_under_test):
    # Arrange
    expected = 'OUT OF STOCK'
    class_under_test._stock['cola'] = 0
    class_under_test.insert_coins(CoinName.QUARTER, 5)
    class_under_test.select_product(Product.COLA)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected

def test_display_when_candy_qty_0_and_pay_3q_and_select_candy_expect_display_shows_out_of_stock(class_under_test):
    # Arrange
    expected = 'OUT OF STOCK'
    class_under_test._stock['candy'] = 0
    class_under_test.insert_coins(CoinName.QUARTER, 3)
    class_under_test.select_product(Product.CANDY)

    # Act
    actual = class_under_test.display

    # Assert
    assert actual == expected
