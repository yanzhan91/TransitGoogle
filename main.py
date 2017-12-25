from flask import Flask, request as flask_request

import Google

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    city = flask_request.args.get('city')
    return Google.webhook(flask_request, city)

if __name__ == '__main__':
    app.run()
