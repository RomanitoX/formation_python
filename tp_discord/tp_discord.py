import os

import discord
from discord.client import Client
from dotenv import load_dotenv

load_dotenv()

default_intents = discord.Intents.default()
default_intents.members = True

client: Client = discord.Client(intents=default_intents)


@client.event
async def on_ready():
    print("Le bot est prêt")


@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(
        884479856736342039)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name}")


@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number+1).flatten()

        for each_message in messages:
            await each_message.delete()

client.run(os.getenv("TOKEN"))
