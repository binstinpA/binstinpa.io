from flask import Flask, render_template, jsonify, request
import stripe

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/boom')
def index():
    return render_template('boom.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/acheter')
def acheter():
    return render_template('acheter.html')


@app.route('/mesvideos')
def mesvideos():
    return render_template('multivideos.html')



    
@app.route('/create-payment-intent', methods=['POST'])
def create_payment():
    try:
        # Créer un objet de paiement intent
        intent = stripe.PaymentIntent.create(
            amount=1000,  # Le montant est en centimes
            currency='eur',
            payment_method_types=['card'],
        )

        # Envoyer le client secret au client pour utiliser dans le script stripe.js
        return jsonify({
            'clientSecret': intent['client_secret']
        })
    except Exception as e:
        return jsonify(error=str(e)), 403

    
    
    
    
    
# Configurez votre clé secrète Stripe
stripe.api_key = 'sk_test_51OUppZBH1lzGBqqnpI3oCVrUMeqzDpc8d2bjhb8W2GTvctYHUvTH7rj2HZaIbYFAl6nLRP0XpyjHOCftXFSKbruK00VYpL442p'


    
    
    



if __name__ == '__main__':
    app.run(debug=True)
