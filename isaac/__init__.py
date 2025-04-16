from .isaac import Isaac


async def setup(bot):
    await bot.add_cog(Isaac(bot))