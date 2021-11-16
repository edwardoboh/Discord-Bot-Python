# An alternate way to create event handlers for Discord events
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

class CustumClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord APIs')
        pass
    pass

client = CustumClient()
client.run(TOKEN)