from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_add_product_to_cart(driver):

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    product_page.add_backpack()
    product_page.open_cart()

    product_name = driver.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text

    assert product_name == "Sauce Labs Backpack"