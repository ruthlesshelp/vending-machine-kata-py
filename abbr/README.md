# Vending Machine Kata - Abbreviated

Working folder `abbr`

For the commplete Vending Machine Kata, start here [Read Me](../README.md)

## Simplifications

- Only quarters accepted
- Only one product, cola
- Only one price, $1.00

## Release Payment

_As a customer_
_I want to have my payment returned_
_So that I can change my mind about buying stuff from the vending machine_

When the release payment button is pressed, the coins the customer placed in the machine are returned.

### Test 01

Test `release_payment`
when no payment
expect no coins returned
