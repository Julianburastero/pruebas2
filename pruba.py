from flask import Flask,redirect,request

import stripe

stripe.api_key = 'sk_test_51NPePNB3zf8eVaNELfYtCcV6PkFiMxCwjhCd348Y00kYTHugW46EQOWVu7TbYSVW8G7GTElOZCFTzFu7HYtlmVQS00JirpR5lj'

app = Flask (__name__,
            static_url_path='/checkout.html',    
            static_folder='')

YOUR_DOMAIN = 'http://127.0.0.1:5500/checkout.html'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1NPp2QB3zf8eVaNEpBD2yEUH',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)
    
    return redirect(checkout_session.url, code =303)


if __name__ == "__main__":
    app.run(port=5500,debug=True)
