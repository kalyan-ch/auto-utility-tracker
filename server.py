from flask import Flask, redirect, request
from splitwise import Splitwise

app = Flask(__name__)
session = {}

consumer_key = '85II34WnFVbML5RNNdabV0qgcH0zUfPUoPiTJ8rT'
consumer_secret = 'DBTBYa6MQj5lRiGy3eWpA8FLcvIQxAVtCPkg1Uvf'

@app.route('/')
def welcome_page():
    return "Hey dude!"

@app.route('/authorize1')
def authorize_step1():
    spltwse = Splitwise(consumer_key, consumer_secret)
    url, secret = spltwse.getAuthorizeURL()
    session['secret'] = secret

    return redirect(url)

@app.route('/authorize2')
def authorize_step2():
    oauth_token    = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    spltwse = Splitwise(consumer_key, consumer_secret)
    access_token = spltwse.getAccessToken(oauth_token, session['secret'], oauth_verifier)

    session['access_token'] = access_token
    return "Authorization successful"

@app.route('/getFriends')
def getFriends():

    access_token = session.get('access_token', '')

    if access_token == '':
        return authorize_step1()

    spltwse = Splitwise(consumer_key, consumer_secret)
    spltwse.setAccessToken(access_token)

    frnds = ''

    for frnd in spltwse.getFriends():
        frnds += frnd.getFirstName()
        frnds += '\n'

    return frnds

if __name__ == '__main__':
    app.run()

