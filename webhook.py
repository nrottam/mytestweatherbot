import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
        req = request.get_json(silent=True, force=True)
        print(json.dumps(req, indent=4))

#        res = makeResponse(req)
#        res = json.dumps(res, indent=4)
#        r = make_response(res)
         r.headers['Context-Type'] = 'application/json'
		 speech = "The forecast for London is Sunny"
         return {
		"speech": speech,
		"displayText": speech,
		"source": "apiai-weather-webhook"
		}

def makeResponse(req):
        result =req.get("result")
        parameters = result.get("parameters")
        city = parameters.get("geo-city")
        date = parameters.get("date")
        requests.get('http://api.openweathermap.org/data/2.5/forecast?q=London,uk&appid=40c66230d405b5a3797ec5497a397ff1')
        json_object = r.json
        for i in range(0,30):
                if date in weather[i]['dt_txt']:
                    condition = weather[i]['weather'][0]['description']
                break


        speech = "The forecast for " +city+"for"+date+"is"+condition
        return {
        "speech": speech,
        "displayText": speech,
        "source": "apiai-weather-webhook"
        }

if __name__ == '__main__':
        port = int(os.getenv('PORT', 5000))
        print("Starting app on port %d" % port)
        app.run(debug=False, port=port, host='0.0.0.0')
