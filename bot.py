import os
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord')

@bot.command(name="99", help="Command to invoke the nine-niner")
async def nine_niner(context):
    niner = [
        "Niner has been invoked by the lords",
        "Oracle Nine-niner will now come in",
        (
            "Let nine niner take over "
            "who called the niners?"
        )
    ]
    await context.send(random.choice(niner))

@bot.command(name="roll_dice", help="Ask bot to roll dice a number of times")
async def roll_dice(ctx, dice_faces: int, dice_rolls: int):
    dice_outcome = [
        random.choice(range(1, dice_faces + 1))
        for _ in range(dice_rolls)
    ]
    await ctx.send(dice_outcome)

bot.run(TOKEN)