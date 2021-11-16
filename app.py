import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord')
    client.run(TOKEN)