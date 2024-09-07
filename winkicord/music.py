import discord, wavelink
from discord.ext import commands




class Musicord(wavelink.Player):
    def __init__(self):
        super().__init__()
        self._volume = 90
        self._source ="ytsource"
        self.add_history=True
    async def tearup(self)->None:
        await self.disconnect()
    

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
