import os

import stripe
from dotenv import load_dotenv
from forex_python.converter import CurrencyRates

load_dotenv()


stripe.api_key = os.getenv("API_KEY_PK")


def convert_rub_to_dollars(amount):
    """Конвертация рублей в доллары"""

    c = CurrencyRates()
    rate = c.get_rate("RUB", "USD")
    return int(amount * rate)


def create_stripe_product(product_name):
    """Stripe продукт"""

    stripe_product = stripe.Product.create(name=product_name)
    return stripe_product


def create_stripe_price(product, price):
    """Цена в страйпе"""

    return stripe.Price.create(product=product.get("id"), currency="usd", unit_amount=price * 100)


def create_stripe_session(price):
    """Сессия для оплаты в Stripe."""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
