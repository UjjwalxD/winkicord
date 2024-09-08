# winkicord/music.py

import discord, wavelink
from discord.ext import commands
from winkicord.nodepool import NodePoolCreds

class Music(commands.Cog):
    """Music Cog."""
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.node_connect())

    async def node_connect(self):
        creds = await NodePoolCreds.get_creds() 
        node = wavelink.Node(uri=f"http://{creds['host']}:{creds['port']}", password=creds['password'])
        await wavelink.Pool.connect(nodes=[node], client=self.bot, cache_capacity=creds['cache'])
#
    @commands.command()
    async def play(self, ctx, *, query: str):
        """Play a song."""
        await ctx.send(f"Playing {song}!")

    @commands.command()
    async def stop(self, ctx):
        """Stop the music."""
        await ctx.send("Music stopped!")

async def setup(bot):
    await bot.add_cog(Music(bot))
