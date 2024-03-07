# Iter05: Sold Out

Change working directory to `iter05`

_As a customer,_
_I want to be told when the item I have selected is not available,_
_so that I can select another item_

When the item selected by the customer is out of stock, the machine displays SOLD OUT.

If the display is checked again, it will display the amount of money remaining in the machine or INSERT COIN if there is no money in the machine.

## Test 43

Test `display` property
when chips are out of stock
and insert 3 quarters
and select chips
expect display shows sold out

## Test 44

Test `display` property
when soda are out of stock
and insert 5 quarters
and select soda
expect display shows sold out

## Test 45

Test `display` property
when candy are out of stock
and insert 3 quarters
and select candy
expect display shows sold out

## Refactoring

- Move stock into a private dictionary
- Initialize stock by passing values in via the constructor

## Refactoring

- Change incorrect product name from "soda" to "cola"
- Use the Product enum values instead of the strings
- Remove the public accessors for the private stock dictionary

## Test 46

Test `display` property
when candy are out of stock
and insert 3 quarters
and select candy
and display shows sold out
expect display shows $0.75

## Fix defect

- The display is supposed to show SOLD OUT, not out of stock

## Test 47

Test `display` property
when candy are out of stock
and select candy
and display shows sold out
expect display now shows insert coin

## Refactoring

- Combined the display info for money and no money in the machine
- Remove the `current_amount` property, it was never needed
- Moved the SOLD OUT literal string into a constant

