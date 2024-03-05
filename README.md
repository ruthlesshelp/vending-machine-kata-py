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

## Iter01: Return Coins

Working folder: `iter01`

_As a customer,_
_I want to have my money returned,_
_so that I can change my mind about buying stuff from the vending machine_

When the return coins button is pressed, the money the customer has placed in the machine is returned and the display shows INSERT COIN.

### Test 1

Test `return_coins` method
when no payment (i.e., no coins inserted)
expect 0 in coins returned

### Test 2

_Assume payment in coins (e.g. quarters)_

Test `return_coins` method
when payment of 1 coin
expect 1 coins returned

### Test 3

_Assume payment in coins (e.g. quarters)_

Test `return_coins` method
when payment of 7 coins
expect 7 coins returned

### Test 4

Test `display` property
when no payment (i.e., no coins inserted)
expect display shows INSERT COIN

### Test 5

Test `display` property
when payment of 1 coin
expect display does NOT show INSERT COIN

### Test 6

Test `display` property
when payment of 5 coins and `return_coins` pushed
expect display shows INSERT COIN

## Iter02: Accept Coins

_As a vendor,_
_I want a vending machine that accepts coins,_
_so that I can collect money from the customer_

The vending machine will accept valid coins (nickels, dimes, and quarters) and reject invalid ones (pennies).

Coin values:
- Penny = $0.01
- Nickel = $0.05
- Dime = $0.10
- Quarter = $0.25

When a valid coin is inserted the amount of the coin will be added to the current amount and the display will be updated.

When there are no coins inserted, the machine displays INSERT COIN. Rejected coins are placed in the coin return.

### Test 7

Test `display` property
when payment of 1 quarter
expect display shows $0.25

### Test 8

Test `display` property
when payment of 5 quarters
expect display shows $1.25

### Test 9

Test `display` property
when payment of 1 nickel
expect display shows $0.05

### Test 10

Test `display` property
when payment of 13 nickels
expect display shows $0.65

### Test 11

Test `display` property
when payment of 1 dime
expect display shows $0.10

### Test 12

Test `display` property
when payment of 43 dimes
expect display shows $4.30

### Test 13

Test `display` property
when payment of 18 nickels
expect display shows $0.90

### Test 14

Test `display` property
when payment of 4 quarters
expect display shows $1.00
