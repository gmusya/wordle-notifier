from flask import Flask, request
import overall
app = Flask(__name__)

def parse(x):
    if len(x) == 5:
        return x
    return x[:5] + '\n' + parse(x[5:])

@app.route('/notify')
def notify():
    #id = request.args.get("server_id")
    text = request.args.get("user") + " completed puzzle!\n||" + parse(request.args.get("log")) + '||'
    print(text)
    id = 957947741135323159
    if id in overall.all_messages:
        overall.all_messages[id].append(text)
    else:
        overall.all_messages[id] = [text]
    print("in server ", overall.all_messages)
    return ""

@app.route('/a1')
def hello():
    all_messages.append("Hi!")
    print("got you")
    return "Hello"

@app.route('/a2')
def hello2():
    all_messages.append("Hi2!")
    return "Hello2"