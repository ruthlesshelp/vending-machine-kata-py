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
