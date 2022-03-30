import discord
import overall
from discord.ext import tasks

client = discord.Client()


@tasks.loop(minutes=0.1)
async def send_delayed_messages():
    print("I tried")
    print("in __main__ ", overall.all_messages)
    to_wait = []
    for channel_id, messages in overall.all_messages.items():
        print(" -> ", channel_id, messages)
        channel = client.get_channel(channel_id)
        for mess in messages:
            to_wait.append(channel.send(mess))
    overall.all_messages = dict()
    for process in to_wait:
        await process
        
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    send_delayed_messages.start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('stop spaming useless commands, please. You are annoying 2 different people in chat by sending them notifications')
    
        #channel = client.get_channel(channel_id)
        #await channel.send("hello2")
        

