from flask import Flask, send_file

app = Flask(__name__)

TYPES = [
    'bullet',
    'blitz',
    'rapid',
    'classical',
    'correspondence',
    'antichess',
    'atomic',
    'chess960',
    'crazyhouse',
    'horde',
    'kingOfTheHill',
    'racingKings',
    'threeCheck'
]


@app.route('/')
@app.route('/home')
def welcome_page():
    return send_file('html/Home.html')


@app.route('/bot')
def bot():
    return send_file('html/Bot.html')


@app.route('/originals')
def originals():
    return send_file('html/Originals.html')


@app.route('/bot/<type_name>')
def bot_type(type_name):
    if type_name in TYPES:
        return send_file(f'bot_leaderboard/{type_name}.html')
    else:
        return "Invalid type", 404


@app.route('/originals/<type_name>')
def originals_type(type_name):
    if type_name in TYPES:
        return send_file(f'originals/{type_name}.html')
    else:
        return "Invalid type", 404


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
