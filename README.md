# Vending Machine Kata

Practicing the Vending Machine Kata in Python

This Kata is by Guy Royse. You can find more info: [Vending Machine Kata](https://github.com/guyroyse/vending-machine-kata)

## Overview

In this exercise, you're asked to create the core functionality of a vending machine. This includes accepting and managing money, providing change, keeping track of inventory, and dispensing items. Essentially, it should perform all the typical operations one would anticipate from a vending machine.

The primary purpose of this kata is to offer a moderately complex challenge that serves as an opportunity to hone Test-Driven Development (TDD) skills. A considerable part of the challenge will involve deciding which tests to write and, crucially, determining the order in which they should be tackled.

**Important explanation:** all the files in this repo are the _result_ of the coding I practiced here.

If you want to practice this Kata, I recommend that you begin with your own folder or repo, such as `my_vending_machine_kata`.

### Setting Up

#### Just need the TL;DR?

Set up in your own working folder with your favorite editor.

The TL;DR steps for `venv` and `pip` should work on macOS (and probably Linux)

They _should_ work on many versions of Python, including Python 3.7+

* What About Windows?
  - The `source venv/bin/activate` line won’t work for Windows.
  - For cmd.exe, use `venv\Scripts\activate.bat` instead
    ```bash
    C:\> python -m venv venv
    C:\> venv\Scripts\activate.bat
    C:\> pip install pytest
    ```
  - For PowerShell, use `venv\Scripts\Activate.ps1` instead:
    ```bash
    PS C:\> python -m venv venv
    PS C:\> venv\Scripts\Activate.ps1
    PS C:\> pip install pytest
    ```

#### TL;DR Steps

1. Use Python >= 3.11 and a virtual environment:
    ```zsh
    $ python3 --version
    Python 3.11.7

    $ python3 -m venv venv

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
    rootdir: /Users/ ... /vending-machine-kata-py
    collected 1 item                                                                                                

    getting_started/test_vending_machine.py .                  [100%]

    ======================= 1 passed in 0.01s =======================
    ```

#### Need more info?

* See this [Install pytest](https://docs.pytest.org/en/latest/getting-started.html) page.
* See this [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) page.

# Getting Started

Here are the steps that I undertook to get started.

Created the `getting_started` folder.

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

I ran `pytest` from the repo root directory and passed the subfolder path and filename. For the iterations, make/change directory to the working folder to limit the `pytest` discovery to that folder.

Running:
```zsh
(venv) $ pytest getting_started/test_vending_machine.py
```

Returns:
```zsh
=================================== test session starts ====================================
platform darwin -- Python 3.11.7, pytest-8.0.2, pluggy-1.4.0
rootdir: /Users/ ... /vending-machine-kata-py
collected 0 items / 1 error                                                                

========================================== ERRORS ==========================================
_________________ ERROR collecting getting_started/test_vending_machine.py _________________
ImportError while importing test module '/Users/ ... /vending-machine-kata-py/getting_started/test_vending_machine.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Cellar/python@3.11/3.11.7_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
getting_started/test_vending_machine.py:1: in <module>
    from vending_machine import VendingMachine
E   ImportError: cannot import name 'VendingMachine' from 'vending_machine' (/Users/ ... /vending-machine-kata-py/getting_started/vending_machine.py)
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
rootdir: /Users/ ... /vending-machine-kata-py
collected 1 item                                                                                       

getting_started/test_vending_machine.py .                                                        [100%]

========================================== 1 passed in 0.00s ===========================================
```

# Iterations

## Prior Iterations

1. [Return Coins](iter01/README.md)
1. [Accept Coins](iter02/README.md)
1. [Select Product](iter03/README.md)
1. [Make Change](iter04/README.md)

Below is the iteration I'm currently working on ...

## Iter05: Sold Out

Change working directory to `iter05`

_As a customer,_
_I want to be told when the item I have selected is not available,_
_so that I can select another item_

When the item selected by the customer is out of stock, the machine displays SOLD OUT.

If the display is checked again, it will display the amount of money remaining in the machine or INSERT COIN if there is no money in the machine.

### Test 43

Test `display` property
when chips are out of stock
and insert 3 quarters
and select chips
expect display shows out of stock

### Test 44

Test `display` property
when soda are out of stock
and insert 5 quarters
and select soda
expect display shows out of stock

### Test 45

Test `display` property
when candy are out of stock
and insert 3 quarters
and select candy
expect display shows out of stock

### Refactoring

- Move stock into a private dictionary
- Initialize stock by passing values in via the constructor

### Refactoring

- Change incorrect product name from "soda" to "cola"
- Use the Product enum values instead of the strings
- Remove the public accessors for the private stock dictionary

### Test 46

Test `display` property
when candy are out of stock
and insert 3 quarters
and select candy
and display shows out of stock
expect display shows $0.75

### Fix defect

- The display is supposed to show SOLD OUT, not out of stock
