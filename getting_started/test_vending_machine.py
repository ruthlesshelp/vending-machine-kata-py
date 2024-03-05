from vending_machine import VendingMachine

def test_getting_started():
    # Arrange
    class_under_test = VendingMachine()

    # Act

    # Assert
    assert type(class_under_test) is VendingMachine
