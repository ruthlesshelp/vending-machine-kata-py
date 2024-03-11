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

### Test 02

Test `release_payment`
when there is money inserted
expect the proper number of quarters are returned

## Select Product

_As a vendor_
_I want customers to select products_
_So that I can give them an incentive to put money in the machine_

- There is one product, cola for $1.00
- If enough payment is inserted and product is selected, the product is dispensed and the machine displays THANK YOU.

## Test 03

Test `select_product`
when no payment
expect no product dispensed

## Test 04

Test `select_product`
when 4 quarters ($1.00) payment
expect product dispensed equals 1

## Change in requirement

~~Test `select_product` with no payment expect no product dispensed~~

## Test 03 - Revised

Test `select_product`
when no payment
expect raised error (RuntimeError)

## Test 05

Test `display`
when product dispensed
expect shows THANK YOU
