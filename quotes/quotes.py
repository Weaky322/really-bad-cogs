from redbot.core import commands
import random

quote_list = []


class Quotes(commands.Cog):
    """Store user created quotes and display them"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_quote(self, ctx, quote: str):
        """Add a quote to the quote list"""
        if not quote:
            return

        elif quote:
            quote_list.append(quote)

    @commands.command()
    async def quote(self, ctx, number: int):
        """Display a quote from the quote list"""
        if not number:
            await ctx.send(quote_list[random.randint(0, len(quote_list) - 1)])

        elif number:
            await ctx.send(quote_list[number - 1])
