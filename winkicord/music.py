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
    @commands.hybrid_command()
    async def play(self, ctx: commands.Context, *, query: str) -> None:
        if not ctx.guild:return
        player: wavelink.Player = cast(wavelink.Player, ctx.voice_client)
        if player and ctx.author.voice.channel:
            if ctx.author.voice.channel.id != player.channel.id:
                return await ctx.send(f'You`re not connected same voice channel as me.')
        if not player:
            try:
                player : LavaMusic = await ctx.author.voice.channel.connect(cls=wavelink.Player , self_deaf=True)
            except AttributeError:
                return await ctx.send("Please join a voice channel first before using this command.")
            except discord.ClientException:
                return await ctx.send("I was unable to join this voice channel. Please try again.")
        if not hasattr(player, "home"):
            player.home = ctx.channel
        tracks: wavelink.Search = await wavelink.Playable.search(query)
        if not tracks:
            await ctx.send(f"{ctx.author.mention} - Could not find any tracks with that query. Please try again.")
            return
        if isinstance(tracks, wavelink.Playlist):
            for track in tracks.tracks:
                track.requestor = ctx.author
            added: int = await player.queue.put_wait(tracks)
            await ctx.reply(f"Added the playlist **`{tracks.name}`** ({added} songs) to the queue.")
        else:
            track: wavelink.Playable = tracks[0]
            track.requestor = ctx.author
            await player.queue.put_wait(track)
            await ctx.reply(f"Added **`{track}`** to the queue.")

        if not player.playing:
            await player.play(player.queue.get(), volume=90,add_history = True)


    @commands.command()
    async def stop(self, ctx):
        """Stop the music."""
        await ctx.send("Music stopped!")

async def setup(bot):
    await bot.add_cog(Music(bot))
