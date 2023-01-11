from flask import Flask
from flask_sse import sse
from flask_cors import CORS
import datetime

from helper import get_data

app = Flask(__name__)
CORS(app)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/sse-events-stream')
def server_side_event():
    """ Function to publish server side event """
    with app.app_context():
        sse.publish(get_data(), type='message')
        print("Event Scheduled at ", datetime.datetime.now())

@app.route('/start')
def index():
    server_side_event()
    return {'message': 'Ok'}


if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0',port=5000)