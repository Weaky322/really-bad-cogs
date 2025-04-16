from redbot.core import commands
import discord

class Isaac(commands.Cog):
    """"""

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and message.content.lower() == "isaac"
            await message.channel.send("https://imgur.com/kM2BGHj")
