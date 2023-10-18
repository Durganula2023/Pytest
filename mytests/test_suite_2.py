import pytest


@pytest.mark.regression
class TestCheckout:
    def test_checkout_as_guest(self):
        print("")
        print("Checkout guest")

    def test_checkout_existing_user(self):
        print("Checkout existing user")