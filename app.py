import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    # guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
        )
    # members = "\n - ".join([member.name for member in guild.members])
    # print(f'Guild members in {guild.name}:: \n {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, Welcome to my discord server')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    random_messages = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool ',
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    if(message.content == "99!"):
        response = random.choice(random_messages)
        await message.channel.send(response)
    pass

client.run(TOKEN)