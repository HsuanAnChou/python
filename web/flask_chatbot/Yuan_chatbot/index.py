import requests
import json
from flask import Flask, request
import apiai

# FB messenger credentials
ACCESS_TOKEN = "EAABolBTyfwYBAOdAu5rlv0bxVHKKYbLKdstJaRqbmqXoIZAAy7qtYtH9iYdeuW3FhZAfZAQqeZC4N3oG2QYittXfc5lBx0HNXcdLBAHSJMytcSXpesVxUxwZA7P8VY8ofjhsivZB53taxPfZAT6QZCL5yvsymNTtG5VtonOFIvwcPuHvtmRZCC7mO"

# api.ai credentials
CLIENT_ACCESS_TOKEN = "0d504a6368ee4afcb63990ecbb21e45e"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # our endpoint echos back the 'hub.challenge' value specified when we setup the webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == 'annetestchatbot':
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return 'Hello World (from Flask!)', 200

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']

    # prepare API.ai request
    req = ai.text_request()
    req.lang = 'en'  # optional, default value equal 'en'
    req.query = message

    # get response from API.ai
    api_response = req.getresponse()
    responsestr = api_response.read().decode('utf-8')
    print(responsestr)
    response_obj = json.loads(responsestr)
    if 'result' in response_obj:
        response = response_obj["result"]["fulfillment"]["messages"][0]["speech"]
        reply(sender, response)
    return "ok"

if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000)
