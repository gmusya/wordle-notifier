import os.path
import json

if not os.path.isfile("token.json"):
    print("Write your token: ", end='')
    token = input()
    token_object = {
        "token": token
    }
    json_token = json.dumps(token_object)
    with open('token.json', 'w') as file:
        file.write(json_token)

with open('token.json', 'r') as file:
    all = json.loads(file.read())
token = all['token']


import server, bot

import threading

t1 = threading.Thread(target=lambda:bot.client.run(token))
t1.start()

if __name__ == "__main__":
    server.app.run()