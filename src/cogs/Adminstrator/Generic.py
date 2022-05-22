from unicodedata import name
from discord.ext import commands

class Generic(commands.Cog, name="Generic"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(
        name="del",
        description="Elimina 100 mensajes del canal",
    )
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx):
        await ctx.channel.purge(limit=100)
        await ctx.send("Se han borrado los mensajes")

def setup(bot: commands.Bot):
    bot.add_cog(Generic(bot))