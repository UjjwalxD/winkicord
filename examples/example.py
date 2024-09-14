import discord
from discord.ext import commands
from winkicord import *

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await NodePoolCreds.set_creds(
        host="lavalink-legacy.jompo.cloud",
        port=2333,
        identifier="Example",
        password="jompo",
        inactive_timeout=14000,
        cache=130
    )
    await bot.load_extension('winkicord.music')

bot.run("")
