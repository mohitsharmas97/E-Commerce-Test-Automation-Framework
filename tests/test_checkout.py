from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(driver):

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    product_page.add_backpack()
    product_page.open_cart()

    checkout_page.checkout(
        "Mohit",
        "Sharma",
        "302001"
    )

    message = checkout_page.get_confirmation()

    assert message == "Thank you for your order!"