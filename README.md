# Vending Machine Kata

Practicing the Vending Machine Kata in Python

This Kata is by Guy Royse. You can find more info: [Vending Machine Kata](https://github.com/guyroyse/vending-machine-kata)

## Overview

In this exercise, you're asked to create the core functionality of a vending machine. This includes accepting and managing money, providing change, keeping track of inventory, and dispensing items. Essentially, it should perform all the typical operations one would anticipate from a vending machine.

The primary purpose of this kata is to offer a moderately complex challenge that serves as an opportunity to hone Test-Driven Development (TDD) skills. A considerable part of the challenge will involve deciding which tests to write and, crucially, determining the order in which they should be tackled.

## Getting Started

Within the `getting_started` folder:
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

3. Create the `VendingMachine` class in the `vending_machine.py` file with just enough code to pass the test.

# Iterations

[Iter  1: Return Coins](iter01/README.md)
[Iter  2: Accept Coins](iter02/README.md)

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
