import os.path
import json
import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

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

client.run(token)
