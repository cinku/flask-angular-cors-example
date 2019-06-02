from flask import Flask, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/items')
def api_articles():
    items = ['item1', 'item2', 'item3', 'item4']
    return Response(json.dumps(items),  mimetype='application/json')

if __name__ == '__main__':
    app.run()