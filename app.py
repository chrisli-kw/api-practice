from flask import Flask, request
from core.config import PORT
from core.utils import CheckData, ConvertData


app = Flask(__name__)


# Homepage
@app.route("/", methods=['GET'])
def hello():
    return 'Hello World'


@app.route('/api/orders', methods=['POST'])
def order():
    data = request.get_json()
    name = data.get('name', '')

    # Check data forms
    if not CheckData.isEnglish(name):
        return '400 - Name contains non-English characters'

    if not CheckData.isTitle(name):
        return '400 - Name is not capitalized'

    price = data.get('price', 0)
    if not CheckData.isPriceLow(price):
        return '400 - Price is over 2000'

    currency = data.get('currency', '')
    if not CheckData.currency_(currency):
        return '400 - Currency format is wrong'

    # Convert data
    data = ConvertData.currency(data)

    return data


if __name__ == "__main__":
    app.run('0.0.0.0', port=PORT)
