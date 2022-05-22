import discord
from discord.ext import commands
from services.firebaseServices import Countries

class CountryManager(Countries, commands.Cog, name="CountryManager"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(
        name="save",
        description="Guarda un pais en la base de datos",
    )
    @commands.has_permissions(administrator=True)
    async def saveCountry(self, ctx, country):
        try:
            self.saveCountries(country)
            await ctx.send("Guardado!")
        except Exception as e:
            print(e)
            await ctx.send("Error al guardar")

    @commands.command(
        name="lc",
        description="Lista los paises guardados",
    )
    @commands.has_permissions(administrator=True)
    async def getAllCtrys(self, ctx):
        try:
            
            embed = discord.Embed(
                title="Paises",
                description="Lista de paises",
                color=0x00ff00
            )

            for country in self.getCountries:
                embed.add_field(name=country.id, value=country.to_dict()['country'])
    
            await ctx.send(embed=embed)
           
        except Exception as e:
            print(e)
            await ctx.send("Error al obtener")


def setup(bot: commands.Bot):
    bot.add_cog(CountryManager(bot))