from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/post', methods = ['POST'])
def post():
  try:
    up_data = json.loads(request.data)
    events = open('events.json', 'w')
    json.dump(up_data, events)
    return 'ok'
  except json.JSONDecodeError:
    return 'malformed'

@app.route('/', methods = ['GET'])
def get():
  return "<html><body><h1>Heimdall guards the gate.</h1></body></html>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8090, debug=True)

