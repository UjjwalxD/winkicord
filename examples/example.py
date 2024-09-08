import discord
from discord.ext import commands
import winkicord

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await winkicord.NodePoolCreds.set_creds(
        host="localhost",
        port=2000,
        identifier="localhost",
        password="youshallnotpass",
        inactive_timeout=14000,
        cache=130
    )
    await bot.load_extension('winkicord.music')

bot.run("YOUR_BOT_TOKEN")
