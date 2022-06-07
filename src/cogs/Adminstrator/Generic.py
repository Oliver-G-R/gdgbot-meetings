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
    
    @commands.command(
        name="help",
        description="Muestra la lista de comandos",
    )
    async def help(self, ctx):
        commands = self.bot.commands
        embed = EmbedGenerator(
            "Lista de comandos",
            "Una lista de todos los comandos disponibles para el bot",
            "info"
        ).getEmbed

        for command in commands:
            embed.add_field(
                name=command.name,
                value=command.description,
                inline=False
            )

        await ctx.send(embed=embed)

    
    @commands.command(
        name="info",
        description="Muestra informacion sobre un comando",
    )
    async def info(self, ctx, command: str):
        command = self.bot.get_command(command)
        if(command):
            embed = EmbedGenerator(
                command.name,
                command.description,
                "info"
            ).getEmbed

            await ctx.send(embed=embed)
        else:
            await ctx.send("No se ha encontrado el comando")

    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
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
            await ctx.send(f"{ctx.author.mention}, faltan argumentos")

def setup(bot: commands.Bot):
    bot.add_cog(Generic(bot))