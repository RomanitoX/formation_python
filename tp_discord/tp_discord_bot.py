import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot is ready !")

@bot.command(name="del")
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_messages in messages:
        await each_messages.delete()

bot.run(os.getenv("TOKEN"))