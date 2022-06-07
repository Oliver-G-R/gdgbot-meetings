from discord.ext import commands 
from discord.utils import get
class MeetingManager(commands.Cog, name="MeetingManager"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    async def cog_check(self, ctx):
        admin = get(ctx.guild.roles, name="Admin")
        if not admin:
            await ctx.send("No se han encontrado permisos de administrador")

    @commands.command(
        name="meeting",
        description="Crea una reunión",
    )
    async def createMeeting(self, ctx:commands.Context, name, date, time, place, creatorTimeZone):
        await ctx.send(f"{ctx.author.mention}, se ha creado la reunión")


def setup(bot: commands.Bot):
    bot.add_cog(MeetingManager(bot))