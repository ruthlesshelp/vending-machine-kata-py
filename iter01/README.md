# Iter01: Return Coins

Working folder: `iter01`

_As a customer,_
_I want to have my money returned,_
_so that I can change my mind about buying stuff from the vending machine_

When the return coins button is pressed, the money the customer has placed in the machine is returned and the display shows INSERT COIN.

## Test 1

Test `return_coins` method
when no payment (i.e., no coins inserted)
expect 0 in coins returned

## Test 2

_Assume payment in coins (e.g. quarters)_

Test `return_coins` method
when payment of 1 coin
expect 1 coins returned

## Test 3

_Assume payment in coins (e.g. quarters)_

Test `return_coins` method
when payment of 7 coins
expect 7 coins returned

## Test 4

Test `display` property
when no payment (i.e., no coins inserted)
expect display shows INSERT COIN

## Test 5

Test `display` property
when payment of 1 coin
expect display does NOT show INSERT COIN

## Test 6

Test `display` property
when payment of 5 coins and `return_coins` pushed
expect display shows INSERT COIN

