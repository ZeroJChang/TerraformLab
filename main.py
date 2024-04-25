from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def get_datetime():
    now = datetime.now(pytz.timezone('America/Guatemala'))
    return jsonify({
        'date': now.strftime("%Y-%m-%d"),
        'time': now.strftime("%H:%M:%S"),
        'timeZone' : now.tzinfo.zone
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
