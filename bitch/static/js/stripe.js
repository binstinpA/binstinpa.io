// /static/js/stripe.js

// Remplacez par votre clé publique Stripe
var stripePublicKey = 'pk_test_51OUppZBH1lzGBqqn18JXunbHDYaLRZKHtnR2l150eWfM1qJwTFxsKBwq6izYhUCU26s7038xkBrLPhJMF7LUqoNt00rPrH8HBC';

// Créez une instance de Stripe
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Créez une instance de l'élément de carte et montez-le dans le DOM
var card = elements.create('card');
card.mount('#card-element');

// Gérez la soumission du formulaire
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Créez une méthode de paiement et envoyez-la à votre serveur
    stripe.createPaymentMethod('card', card).then(function(result) {
        if (result.error) {
            // Affichez les erreurs dans votre formulaire ici
            console.error(result.error.message);
        } else {
            // Envoyez le paymentMethodId à votre serveur pour créer une intention de paiement
            fetch('/payment/create-payment-intent', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ paymentMethodId: result.paymentMethod.id, amount: 1000 }) // Assurez-vous de transmettre le montant correct
            }).then(function(response) {
                response.json().then(function(paymentIntentResponse) {
                    if (paymentIntentResponse.error) {
                        console.error(paymentIntentResponse.error);
                    } else {
                        console.log('Le paiement a été réussi:', paymentIntentResponse);
                        // Vous pouvez rediriger l'utilisateur vers une page de succès ou afficher un message de confirmation ici
                    }
                });
            });
        }
    });
});
