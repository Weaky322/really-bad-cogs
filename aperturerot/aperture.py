from redbot.core import commands
import random

from aperturerot.quotes import glados_quotes
from aperturerot.quotes import cave_quotes
from aperturerot.quotes import wheatley_quotes


class ApertureRot(commands.Cog):
    """My custom cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def glados(self, ctx):
        """Get a random GLaDOS quotes"""
        await ctx.send("**GLaDOS:** " + glados_quotes[random.randint(0, len(glados_quotes) - 1)])

    @commands.command()
    async def cave(self, ctx):
        """Get a random Cave Johnson quotes"""
        await ctx.send("**Cave Johnson:** " + cave_quotes[random.randint(0, len(cave_quotes) - 1)])

    @commands.command()
    async def wheatley(self, ctx):
        """Get a random Wheatley quotes"""
        await ctx.send("**Wheatley:** " + wheatley_quotes[random.randint(0, len(wheatley_quotes) - 1)])
