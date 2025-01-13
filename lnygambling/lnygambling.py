import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

# FUTURE 2DO: make a generalized version of this
class gamba(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command(aliases=['world','hi'])
    async def hello(self, ctx: commands.Context):
      await ctx.send("dud")

async def setup(bot):
    await bot.add_cog(gamba(bot))
