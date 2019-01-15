from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Miguel',
    }
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/products')
def list_products():

    products = [
        {
            "title": "Red Ball",
            "price": 4.99,
            "url": "https://cdn-s3.touchofmodern.com/sales/000/059/310/4e635b0e9697758d5199b0899b581de1_medium_half.jpg?1547248627",
        },
        {
            "title": "Swiss Timepiece",
            "price": 249.00,
            "url": "https://cdn-s3.touchofmodern.com/sales/000/059/324/e5cb4f58bb90b760db2e590ba611c9a0_medium_half.jpg?1547254748",
        },
        {
            "title": "La Grande Dame Rose",
            "price": 79.00,
            "url": "https://cdn-s3.touchofmodern.com/sales/000/059/240/0aa17b5034aaea2f31c9758e2a09d414_medium_half.jpg?1547149967",
        },
        {
            "title": "Underwater Scooter",
            "price": 500.00,
            "url": "https://cdn-s3.touchofmodern.com/sales/000/059/118/30173ba90525baffdd011cb2be989cc6_medium_half.jpg?1546986799",
        },
        {
            "title": "Underwater Scooter",
            "price": 500.00,
            "url": "https://cdn-s3.touchofmodern.com/sales/000/059/118/30173ba90525baffdd011cb2be989cc6_medium_half.jpg?1546986799",
        },
        {
            "title": "Underwater Scooter",
            "price": 500.00,
            "url": "https://cdn-s3.touchofmodern.com/sales/000/059/118/30173ba90525baffdd011cb2be989cc6_medium_half.jpg?1546986799",
        },
        {
            "title": "Underwater Scooter",
            "price": 500.00,
            "url": "https://cdn-s3.touchofmodern.com/sales/000/059/118/30173ba90525baffdd011cb2be989cc6_medium_half.jpg?1546986799",
        },
        {
            "title": "Underwater Scooter",
            "price": 500.00,
            "url": "https://cdn-s3.touchofmodern.com/sales/000/059/118/30173ba90525baffdd011cb2be989cc6_medium_half.jpg?1546986799",
        },
    ]

    return render_template('list_products.html', title='Products', products=products)
