from discord.ext import commands 

class MeetingManager(commands.Cog, name="MeetingManager"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(
        name="meeting",
        description="Crea una reunión",
    )
    @commands.has_permissions(administrator=True)
    async def createMeeting(self, ctx:commands.Context, name, date, time, place, creatorTimeZone):
        await ctx.send(f"{ctx.author.mention}, se ha creado la reunión")


def setup(bot: commands.Bot):
    bot.add_cog(MeetingManager(bot))