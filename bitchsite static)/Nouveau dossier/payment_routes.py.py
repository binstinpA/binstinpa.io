# payment_routes.py

from flask import Blueprint, jsonify, request
from .stripe_config import stripe

payment_routes = Blueprint('payment_routes', __name__)

@payment_routes.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    data = request.get_json()
    try:
        intent = stripe.PaymentIntent.create(
            amount=data['amount'],
            currency='eur',
            payment_method_types=['card'],
        )
        return jsonify({
            'clientSecret': intent.client_secret
        })
    except Exception as e:
        return jsonify(error=str(e)), 403
