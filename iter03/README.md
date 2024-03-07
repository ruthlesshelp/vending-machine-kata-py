
# Iter03: Select Product

Change working folder to `iter03`

_As a vendor,_ 
_I want customers to select products,_ 
_so that I can give them an incentive to put money in the machine_ 

There are three products:
- cola for $1.00
- chips for $0.50
- candy for $0.65

When the respective button is pressed and enough money has been inserted, the product is dispensed and the machine displays THANK YOU.

If the display is checked again, it will display INSERT COIN and the current amount will be set to $0.00.

If there is not enough money inserted then the machine displays PRICE and the price of the item and subsequent checks of the display will display
either INSERT COIN or the current amount as appropriate.

## Test 19

Test `select_cola` method
when payment 4 quarters
expect 1 cola is dispensed

## Test 20

Test `display` property
when payment 4 quarters and cola is pressed
expect display shows THANK YOU

## Test 21

Test `select_cola` method
when payment 3 quarters (not enough money)
expect cola is not dispensed

## Test 22

Test `current_amount` property
when payment 4 quarters 
and cola is pressed
and display shows THANK YOU
expect current amount now shows $0.00

## Refactoring

- Move the THANK YOU message to a constant

## Defect Found!

Need to resolve incorrect behaviors:
- _If the display is checked again, it will display INSERT COIN_
- _and the current amount will be set to $0.00._

Observations:
* There are two relevant properties: `display` and `current_amount`
* It seems we didn't implement `current_amount`
* Also, Test 22 (and perhaps others) is wrong

## Test 22 (fix)

Test `display` property
when payment 4 quarters 
and cola is pressed
and display shows THANK YOU
expect display now shows INSERT COIN

## Test 23

Test `current_amount` property
when payment 4 quarters 
and cola is pressed
and display shows THANK YOU
and display shows INSERT COIN
expect current amount now shows $0.00

## Refactoring

- Use the `current_amount` to set the `display`, where appropriate

## Test 24

Test `display` property
when payment 3 quarters (not enough money)
and cola is pressed
expect display shows PRICE $1.00

## Test 25

Test `display` property
when payment 3 quarters (not enough money)
and cola is pressed
and display shows PRICE $1.00
expect subsequent check of the display shows INSERT COIN

## Test 26

Test `current_amount` property
when payment 3 quarters (not enough money)
and cola is pressed
and display shows PRICE $1.00
expect current amount is $0.75

## Test 27

_Let's implement the chips for $0.50_

Test `select_chips` method
when payment 2 quarters
expect 1 chips is dispensed

## Test 28

Test `display` property
when payment 2 quarters and chips is pressed
expect display shows THANK YOU

## Test 29

Test `select_chips` method
when payment 3 nickels (not enough money)
expect chips is not dispensed

## Test 30

Test `display` property
when payment 3 nickels (not enough money)
and chips is pressed
expect display doesn't show THANK YOU

## Test 31

Test `current_amount` property
when payment 5 dimes 
and chips is pressed
and display shows THANK YOU
expect current amount now shows $0.00

## Refactoring

- introduced the Product enum with Cola and Chips
- introduced a dictionary of prices for each product
- changed code to use new elements

## Test 32

_It's time for some Candy!_

Test `select_candy` method
when payment 2 quarters, 1 dime, and 1 nickel
expect 1 candy is dispensed

## Test 33

Test `display` property
when payment 2 quarters, 1 dime, and 1 nickel
and candy is pressed
expect display shows THANK YOU

## Test 34

Test `select_candy` method
when payment 1 quarter and 1 dime (not enough money)
expect candy is not dispensed

## Test 35

Test `current_amount` property
when payment 2 quarters, 1 dime, and 1 nickel
and candy is pressed
and display shows THANK YOU
expect current amount now shows $0.00

## Refactoring

- added Candy to the Product enum
- added Candy price to dictionary of prices
- changed code to use new item

## Test 36

Test `display` property
when payment 2 quarters (not enough money)
and candy is pressed
expect display shows PRICE $0.65

## Test 37

_Add missing Chips test_

Test `display` property
when payment 3 dimes (not enough money)
and chips is pressed
expect display shows PRICE $0.50

## Refactoring

- Combine `select_cola`, `select_chips`, and `select_candy` into one `select_product` method
- Update tests to use this new method

## Using Fixture for Setup

This is not in the requirements, but it would be instructive to add a wrinkle to this Kata.

Imagine there's something we need to know about the Vending Machine's physical properties:
1. The VM takes 2 seconds to initialize (power up and run self diagnostics)
2. The initialization only happens once when the VM is instantiated

Let's make that change to VendingMachine(), as follows:
```python
# Much of the class def is omitted for brevity 
import time

class VendingMachine:

    def __init__(self):
        time.sleep(2)
```

Now, the 37 passing tests slow down: going from under 0.01 second to a _terrifyingly_ slow 74.25 seconds. These automated tests are essentially useless.

Fortunately, `pytest` offers fixtures to help with the Vending Machine initialization problem. More info is in the `pytest` doc [How to use fixtures](https://docs.pytest.org/en/latest/how-to/fixtures.html)

Let's introduce a "module" fixture, like this:
```python
# test_vending_machine.py

import pytest

from vending_machine import VendingMachine, Coin, Product

@pytest.fixture(scope="module")
def vending_machine_instance():
    vending_machine = VendingMachine()
    yield vending_machine
```

And rewrite all the tests so they fit this pattern:
```python
def test_when_XYZ_expect_ABC(vending_machine_instance):
    # Arrange
    vending_machine_instance.insert_coins(Coin.QUARTER, 1)

    # Act
    actual = vending_machine_instance.return_coins()

    # Assert
    assert actual['quarters'] == 1
```

Running all the tests ... results in 25 failed, 12 passed in 2.13s
- the good news is that 72.12 seconds faster (a 97% increase in performance)
- the bad news is that 25 tests failed

Looking into the failures, it's obvious that the state of our Vending Machine is carrying over from test to test.

Let's add a _testability enhancement_ that allows us to "reset" the state of the Vending Machine. Like this:
```python
# Much of the class def is omitted for brevity 
class VendingMachine:

    def __init__(self):
        time.sleep(2)
        self._reset()

    def _reset(self):
        self._total_amount = 0
        self.nickels = 0
        self.dimes = 0
        self.quarters = 0
        self.rejects = 0
        self._display = INSERT_COIN
```

This allows us to add a second fixture with the "function" scope, like this:
```python
@pytest.fixture(scope="function")
def class_under_test(vending_machine_instance):
    vending_machine_instance._reset()
    yield vending_machine_instance
```

And change all the tests so they fit this pattern:
```python
def test_when_XYZ_expect_ABC(class_under_test):
    # Arrange
    class_under_test.insert_coins(Coin.QUARTER, 1)

    # Act
    actual = class_under_test.return_coins()

    # Assert
    assert actual['quarters'] == 1
```

Running all the tests ... results in 37 passed in 2.04s! An average of 0.055 seconds per test.

One important advantage of using fixtures, you can reduce the amount of redundant Arrange code that's found across tests.
