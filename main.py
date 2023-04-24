import requests
import flask
app = flask.Flask(__name__)
def ask(thing):
  headers = {
      'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
      'Accept': '*/*',
      'Accept-Language': 'en-US,en;q=0.5',
      'Content-Type': 'application/json',
      'Origin': 'https://www.useblackbox.ai',
      'Alt-Used': 'www.useblackbox.ai',
      'Connection': 'keep-alive',
      'Referer': 'https://www.useblackbox.ai/home-codesearch',
  }

  json_data = {
      'userId': '',
      'textInput': f'{thing}',
      'source': 'webapp',
  }

  response = requests.post('https://www.useblackbox.ai/autocompletev4', headers=headers, json=json_data)

  return (response.json())
@app.route('/api/ask')
def askk():
  thing = flask.request.args.get("q")
  return flask.jsonify(ask(thing))
app.run(port=1002)
