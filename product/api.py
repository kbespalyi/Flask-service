# Product service

from flask import Flask
from flask_restful import Resource, Api

import os

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': [
                'Ice cream',
                'Chocolate',
                'Fruit',
                'Eggs'
            ]
        }

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True)
