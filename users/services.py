import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name):
    """ Создание продукта в Stripe"""
    product = stripe.Product.create(name=name)
    return product


def create_stripe_price(amount, product_id):
    """ Создание цены в Stripe"""
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product_data={"name": "purchased"},
        product=product_id,
    )


def create_stripe_session(price):
    """ Создание сессии на оплату в Stripe"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/success",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
