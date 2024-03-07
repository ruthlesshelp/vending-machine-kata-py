# Iter04: Make Change

Change working directory to `iter04`

_As a vendor_  
_I want customers to receive correct change,_  
_so that they will use the vending machine again_  

When a product is selected that costs less than the amount of money in the machine, then the remaining amount is placed
in the coin return.

## Test 38

Test `coin_return` property
when payment 7 quarters
and chips is pressed
expect coin return has 5 quarters

## Test 39

Test `coin_return` property
when payment 9 dimes
and chips is pressed
expect coin return has 1 quarter, 1 dime, and 1 nickel

## Test 40

Test `coin_return` property
when payment 1 quarter
and chips is pressed
display shows PRICE $0.50
expect coin return is empty

## Test 41

Test `coin_return` property
when payment 3 quarters and 1 dime
and candy is pressed
expect coin return has 2 dimes

## Test 42

_Let's try some relatively large numbers of coins as input and use Excel to get the `expected` return_

**NOTE:** this probably isn't the desired behavior, but we are _checking that the code works as it's intend to work by the developer_.

Test `coin_return` property
and insert 7919 quarters
and insert 7829 dimes
and insert 7723 nickels
and candy is pressed
expect coin return has 12592 quarters, 1 dime, 1 nickel

## Refactoring

- Change the behavior of the `return_coins` method
- Have it put the coins in the `coin_return` property and return None
- Change the tests to look in the `coin_return` for the returned change

## Refactoring

- Change the behavior of the `select_product` method
- Have it put the dispensed product in the `output_box` property and return None
- Change the tests to look in the `output_box` for the dispensed product
