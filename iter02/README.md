# Iter02: Accept Coins

Change working folder to `iter02`

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

## Test 7

Test `display` property
when payment of 1 quarter
expect display shows $0.25

## Test 8

Test `display` property
when payment of 5 quarters
expect display shows $1.25

## Test 9

Test `display` property
when payment of 1 nickel
expect display shows $0.05

## Test 10

Test `display` property
when payment of 13 nickels
expect display shows $0.65

## Test 11

Test `display` property
when payment of 1 dime
expect display shows $0.10

## Test 12

Test `display` property
when payment of 43 dimes
expect display shows $4.30

## Test 13

Test `display` property
when payment of 18 nickels
expect display shows $0.90

## Test 14

Test `display` property
when payment of 4 quarters
expect display shows $1.00

## Refactoring

- changed property `coins` to `quarters`
- changed `insert_coins` to `insert_quarters`
- added `total_amount` property to track total
- created private `_handle_coins` to consolidate:
  * total calculation
  * display format
- added `INSERT_COIN` constant when no coins
- added constants for the four types of coins

NOTE: All tests continue to pass, but `coin_return` needs test scenarios.

## Test 15

Test `return_coins` method
when payment 3 nickels, 5 dimes, and 7 quarters
expect 3 nickels, 5 dimes, and 7 quarters returned

## Test 16

Test `return_coins` method
when payment 11 pennies
expect 11 rejects returned

## Refactoring

- Introduce the Coin enum
- Reintroduce `insert_coins` that takes the enum as parameter
- Combine the `insert_*` methods into the one method.

## Test 17

Test `return_coins` method
when payment 17 slugs
expect 17 rejects returned

## Test 18

Test `display' property
when payment 137 nickels, 83 dimes, and 41 quarters
expect display shows $25.40
