from redbot.core import commands
import discord

class Isaac(commands.Cog):
    """"""

    def __init__(self, bot):
        self.bot = bot

        self.guild_channel_last_messages = {}


    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and "isaac" in message.content.lower():
            await message.channel.send("https://imgur.com/kM2BGHj")