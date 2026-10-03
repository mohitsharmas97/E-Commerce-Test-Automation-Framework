# E-Commerce Test Automation Framework

A UI test automation framework built using **Python, Selenium, and PyTest** to automate and validate important e-commerce workflows such as login, product selection, cart, and checkout.
<img width="1467" height="333" alt="image" src="https://github.com/user-attachments/assets/a6bdad75-114f-4b3e-9c34-06bcf6141de7" />


## 🚀 Features

- Automated browser testing using Selenium WebDriver
- PyTest-based test execution
- Page Object Model (POM)
- Reusable page classes
- PyTest fixtures for browser setup and teardown
- Positive and negative login test cases
- Product and cart testing
- End-to-end checkout testing
- Assertions for test validation
- Explicit waits for dynamic web elements

## 🛠️ Tech Stack

- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Git & GitHub

## 📂 Project Structure

```text
E-Commerce-Test-Automation-Framework/
│
├── pages/
│   ├── login_page.py
│   ├── product_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## 🧪 Test Cases

### 🔐 Login Testing
- Test login with valid credentials
- Test login with invalid credentials
- Verify error messages

### 🛒 Product & Cart Testing
- Login to the application
- Add product to cart
- Open shopping cart
- Verify product added to cart

### 💳 Checkout Testing
- Add product to cart
- Proceed to checkout
- Enter customer information
- Complete the order
- Verify order confirmation

## 🏗️ Framework Architecture

This project follows the Page Object Model (POM) design pattern.

```text
Test Cases
    │
    ▼
Page Objects
    │
    ├── Login Page
    ├── Product Page
    └── Checkout Page
    │
    ▼
Selenium WebDriver
    │
    ▼
SauceDemo Application
```

Page-specific locators and actions are maintained separately from test cases, making the framework more reusable and maintainable.

## 🔄 Test Flow

```text
Open SauceDemo
      ↓
    Login
      ↓
Select Product
      ↓
Add Product to Cart
      ↓
  Open Cart
      ↓
  Checkout
      ↓
Enter Customer Details
      ↓
   Place Order
      ↓
Verify Order Confirmation
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd E-Commerce-Test-Automation-Framework
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running Tests

- Run all tests:
  ```bash
  pytest -v
  ```

- Run login tests:
  ```bash
  pytest tests/test_login.py -v
  ```

- Run cart tests:
  ```bash
  pytest tests/test_cart.py -v
  ```

- Run checkout tests:
  ```bash
  pytest tests/test_checkout.py -v
  ```

## 🌐 Application Under Test

**SauceDemo:** [https://www.saucedemo.com/](https://www.saucedemo.com/)  
The application is used for practicing automated testing of an e-commerce workflow.

## 📌 Key Concepts Demonstrated

- Selenium WebDriver & Web element locators
- Explicit waits for dynamic elements
- PyTest fixtures for setup and teardown
- Assertions for verification
- Page Object Model (POM) design pattern
- Positive and Negative testing
- End-to-end (E2E) workflow testing
- Clean test automation framework structure

## 👨‍💻 Author

**Mohit **
