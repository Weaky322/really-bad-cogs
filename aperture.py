from redbot.core import commands
import random

from .quotes import cave_quotes


class Aperture(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send(cave_quotes[1])
