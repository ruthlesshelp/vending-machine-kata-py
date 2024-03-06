# Vending Machine Kata

Practicing the Vending Machine Kata in Python

This Kata is by Guy Royse. You can find more info: [Vending Machine Kata](https://github.com/guyroyse/vending-machine-kata)

## Overview

In this exercise, you're asked to create the core functionality of a vending machine. This includes accepting and managing money, providing change, keeping track of inventory, and dispensing items. Essentially, it should perform all the typical operations one would anticipate from a vending machine.

The primary purpose of this kata is to offer a moderately complex challenge that serves as an opportunity to hone Test-Driven Development (TDD) skills. A considerable part of the challenge will involve deciding which tests to write and, crucially, determining the order in which they should be tackled.

### Setting Up

#### Just need the TL;DR?

1. Use Python >= 3.11 and a virtual environment:
    ```zsh
    $ python3 --version
    Python 3.11.7

    $ source venv/bin/activate
    (venv) $ 
    ```

2. Install `pytest` version >= 8
    ```zsh
    (venv) $ pip install pytest

    ... installation info

    (venv) $ pytest --version
    pytest 8.0.2
    ```

3. Running `pytest` like this:
    ```zsh
    (venv) $ pytest getting_started/test_vending_machine.py
    ```

4. Returns
    ```zsh
    ====================== test session starts ======================
    platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0
    rootdir: /Users/sdr/ ... /vending-machine-kata-py
    collected 1 item                                                                                                

    getting_started/test_vending_machine.py .                  [100%]

    ======================= 1 passed in 0.01s =======================
    ```

#### Need more info?

See this [Install pytest](https://docs.pytest.org/en/latest/getting-started.html) page.

### The Starting Point

Under the `getting_started` folder:
1. Create the `test_vending_machine.py` file

2. Write a failing test:
```python
from vending_machine import VendingMachine

def test_getting_started():
    # Arrange
    class_under_test = VendingMachine()

    # Act

    # Assert
    assert type(class_under_test) is VendingMachine
```

3. See the test fail.

Running:
```zsh
(venv) $ pytest getting_started/test_vending_machine.py
```

Returns:
```zsh
=================================== test session starts ====================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0
rootdir: /Users/sdr/training/ruthlesshelp/vending-machine-kata-py
collected 0 items / 1 error                                                                

========================================== ERRORS ==========================================
_________________ ERROR collecting getting_started/test_vending_machine.py _________________
ImportError while importing test module '/Users/sdr/training/ruthlesshelp/vending-machine-kata-py/getting_started/test_vending_machine.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Cellar/python@3.11/3.11.7_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
getting_started/test_vending_machine.py:1: in <module>
    from vending_machine import VendingMachine
E   ImportError: cannot import name 'VendingMachine' from 'vending_machine' (/Users/sdr/training/ruthlesshelp/vending-machine-kata-py/getting_started/vending_machine.py)
================================= short test summary info ==================================
ERROR getting_started/test_vending_machine.py
!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!
===================================== 1 error in 0.03s =====================================
```

4. Create the `VendingMachine` class in the `vending_machine.py` file with just enough code to pass the test.

Running:
```zsh
(venv) $ pytest getting_started/test_vending_machine.py
```

Returns:
```zsh
========================================= test session starts ==========================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0
rootdir: /Users/sdr/training/ruthlesshelp/vending-machine-kata-py
collected 1 item                                                                                       

getting_started/test_vending_machine.py .                                                        [100%]

========================================== 1 passed in 0.00s ===========================================
```

# Iterations

1. [Return Coins](iter01/README.md)
1. [Accept Coins](iter02/README.md)

## Iter03: Select Product

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

### Test 19

Test `select_cola` method
when payment 4 quarters
expect 1 cola is dispensed

### Test 20

Test `display` property
when payment 4 quarters and cola is pressed
expect display shows THANK YOU

### Test 21

Test `select_cola` method
when payment 3 quarters (not enough money)
expect cola is not dispensed

### Test 22

Test `display` property
when payment 4 quarters 
and cola is pressed
and display shows THANK YOU
expect display now shows $0.00

### Refactoring

- Move the THANK YOU message to a constant

### Defect Found!

Need to resolve incorrect behaviors:
- _If the display is checked again, it will display INSERT COIN_
- _and the current amount will be set to $0.00._

Observations:
* There are two relevant properties: `display` and `current_amount`
* It seems we didn't implement `current_amount`
* Also, Test 22 (and perhaps others) is wrong

### Test 22 (fix)

Test `display` property
when payment 4 quarters 
and cola is pressed
and display shows THANK YOU
expect display now shows INSERT COIN

### Test 23

Test `current_amount` property
when payment 4 quarters 
and cola is pressed
and display shows THANK YOU
and display shows INSERT COIN
expect current amount now shows $0.00

### Refactoring

- Use the `current_amount` to set the `display`, where appropriate

### Test 24

Test `display` property
when payment 3 quarters (not enough money)
and cola is pressed
expect display shows PRICE $1.00

### Test 25

Test `display` property
when payment 3 quarters (not enough money)
and cola is pressed
and display shows PRICE $1.00
expect subsequent check of the display shows INSERT COIN

### Test 26

Test `current_amount` property
when payment 3 quarters (not enough money)
and cola is pressed
and display shows PRICE $1.00
expect current amount is $0.75

### Test 27

_Let's implement the chips for $0.50_

Test `select_chips` method
when payment 2 quarters
expect 1 chips is dispensed

### Test 28

Test `display` property
when payment 2 quarters and chips is pressed
expect display shows THANK YOU

### Test 29

Test `select_chips` method
when payment 3 nickels (not enough money)
expect chips is not dispensed

### Test 30

Test `display` property
when payment 3 nickels (not enough money)
and chips is pressed
expect display doesn't show THANK YOU

### Test 31

Test `display` property
when payment 5 dimes 
and chips is pressed
and display shows THANK YOU
expect current amount now shows $0.00

### Refactoring

- introduced the Product enum with Cola and Chips
- introduced a dictionary of prices for each product
- changed code to use new elements
