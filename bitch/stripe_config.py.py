# stripe_config.py

import stripe
import os

# Votre clé secrète Stripe
stripe.api_key = os.getenv('STRIPE_SECRET_KEY', 'sk_test_...')
