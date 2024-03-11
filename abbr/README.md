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

### Test 03

Test `select_product`
when no payment
expect no product dispensed

### Test 04

Test `select_product`
when 4 quarters ($1.00) payment
expect product dispensed equals 1

### Change in requirement

~~Test `select_product` with no payment expect no product dispensed~~

### Test 03 - Revised

Test `select_product`
when no payment
expect raised error (RuntimeError)

### Test 05

Test `display`
when product dispensed
expect shows THANK YOU

## Refactoring

### Test Fixture: Before Test

Remove repetitive class-under-test instantiation.

### Single Responsibility Principle (SRP)

Reasons to change:
- Product (select and dispense)
- Payment (accept, pay, release)
- Display

Separate out the payment processor from the vending machine.

Payment Processor
- `make_payment` accepts coins as payment
- `is_payment_made` determines if payment is made

## Unit Test Payment Processor

New `test_payment_processor.py` file.

### Test 06

Test `make_payment`
When no payment
Expect payment is 0

### Test 07

Test `make_payment`
When payment of four quarters
Expect payment is 4

### Test 08

Test `is_payment_made`
When no payment
Expect false

### Test 09

Test `is_payment_made`
When payment of four quarters
Expect True

## Payment Storage

Let's introduce a way to save the running total of payments.

_As a vendor,_
_I want the total of payments collected saved to a database,_
_So that I can account for the payments_

- Payment DAO
  * `retrieve` method returns money (int)
  * `save` method takes money (int) returns void

## Refactoring

- Vending machine handles coins (quarters)
- Payment processor handles money (cents)
