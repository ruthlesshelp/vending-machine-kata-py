# Iter06: Exact Change Only

Change working directory to `iter06`

_As a customer,_
_I want to be told when exact change is required,_
_so that I can determine if I can buy something with the money I have before inserting it_

When the machine is not able to make change with the money in the machine for any of the items that it sells, it will display EXACT CHANGE ONLY instead of INSERT COIN.

## Test 48

Test display
when unable to make change
expect display shows exact change only

## Test 49

_How do you determine if exact change required?_

| Product |  Cola | Chips | Candy |
|:--------|------:|------:|------:|
| Price   | $1.00 | $0.50 | $0.65 |

**Valid coins:** nickels ($0.05), dimes ($0.10), and quarters ($0.25)

- **Cola:**
  - Change cannot be made if there are no nickels for change
  - Example: 3 quarters ($0.75) + 3 dimes ($0.10) = $1.05
  - Otherwise, change is can be made by returning excess coins

- **Chips:**
  - Change cannot be made if there are no nickels for change.
  - Example: 1 quarter ($0.25) + 3 dimes ($0.10) = $0.55

- **Candy:**
  - Change cannot be made if there are no dimes or no nickels for change.
  - Example 1: 7 dimes = $0.70
  - Example 2: 3 quarters = $0.75

So, if there are no nickels or dimes for change, then the machine cannot make change.

Test display
when no nickels to make change
expect display shows exact change only

## Test 50

Test display
when no dimes to make change
expect display shows exact change only

## Refactoring

- Move string to constant.
- Revamp the coins for change logic.
- Guard against missing change maker coins.
- Before each test restock and reset coins for change.
- Set the initial coins more precisely for the two tests
