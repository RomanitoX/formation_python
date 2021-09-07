import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

class DiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur")


bot = DiscordBot()
bot.run(os.getenv("TOKEN"))