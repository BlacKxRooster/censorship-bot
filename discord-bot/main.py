import random
import discord
import os
from asyncio.tasks import wait_for

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    """ some on_message command """
    if message.author.id == client.user.id:
        return
    msg_content = message.content.lower()


# its the bad words..
    badWord = ['nigger', 'nigga', 'nigguh']

# these are for brian.
    propGram = ['right quick', 'rite quick', 'rite quik', 'ryte quic']

    if any(word in msg_content for word in propGram):
        await message.channel.send("Use correct Grammar :smile:")
        await message.delete()


 # deletes message if match and bot posts
    if any(word in msg_content for word in badWord):
        await message.channel.send("That's not okay")
        await message.delete()

# the token DO NOT SHARE!!!!
client.run('TOKEN')