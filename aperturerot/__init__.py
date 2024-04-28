from .aperturerot import ApertureRot


async def setup(bot):
    await bot.add_cog(ApertureRot(bot))
