from flask import Flask, request
import overall
app = Flask(__name__)

def parse(x):
    if len(x) == 5:
        return x
    return x[:5] + '\n' + parse(x[5:])

def send_message(id, text):
    if id in overall.all_messages:
        overall.all_messages[id].append(text)
    else:
        overall.all_messages[id] = [text]

@app.route('/notify')
def notify():
    #id = request.args.get("server_id")
    text = request.args.get("user") + " completed puzzle!\n||" + parse(request.args.get("log")) + '||'
    print(text)
    send_message(957947741135323159, text)
    print("in server ", overall.all_messages)
    return ""

@app.route('/a1')
def hello():
    id = 957947741135323159
    send_message(957947741135323159, "Hi!")
    print("got you")
    return "Hello"

@app.route('/a2')
def hello2():
    id = 957947741135323159
    send_message(957947741135323159, "Hi2!")
    return "Hello2"