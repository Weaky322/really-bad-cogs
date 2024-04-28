from aperture import Aperture


async def setup(bot):
    await bot.add_cog(Aperture(bot))
