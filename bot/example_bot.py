import os.path
import json
import discord
from discord.ext import tasks



client = discord.Client()

channel_id = int(input("enter server id : "))

all_messages = ["test"]

@tasks.loop(minutes=0.1)
async def test():
    channel = client.get_channel(channel_id)
    print("I tried")
    while len(all_messages):
        mess = all_messages[-1]
        await channel.send(mess)
        all_messages.pop()
        


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    test.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
        channel = client.get_channel(channel_id)
        await channel.send("hello2")
        

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

import threading
def lmao():
    client.run(token)
t1 = threading.Thread(target=lmao)
t1.start()


from flask import Flask

app = Flask(__name__)

@app.route('/a1')
def hello():
    all_messages.append("Hi!")
    print("got you")
    print(all_messages)
    return "Hello"


@app.route('/a2')
def hello2():
    all_messages.append("Hi2!")
    return "Hello2"


if __name__ == "__main__":
    app.run()