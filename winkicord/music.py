import discord
from discord.ext import commands

class Music(commands.Cog):
    """Music Cog."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, song: str):
        """Play a song."""
        await ctx.send(f"Playing {song}!")

    @commands.command()
    async def stop(self, ctx):
        """Stop the music."""
        await ctx.send("Music stopped!")

async def setup(bot)->None:
    await bot.add_cog(Music(bot))
