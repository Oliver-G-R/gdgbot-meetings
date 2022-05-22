from unicodedata import name
from discord.ext import commands
from utils.Embed import EmbedGenerator
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
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print("error")
        if isinstance(error, commands.MissingPermissions):
            embed = EmbedGenerator(
                "Error",
                "No tienes permisos para ejecutar este comando",
                "error"
            ).getEmbed

            for e in error.missing_perms:
                embed.add_field(name="Permisos", value=e)
            
            await ctx.send(embed=embed)

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f"{ctx.author.mention}, comando no encontrado")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention}, falta argumento")

def setup(bot: commands.Bot):
    bot.add_cog(Generic(bot))