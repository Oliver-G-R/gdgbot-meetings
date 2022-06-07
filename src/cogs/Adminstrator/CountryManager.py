from discord.ext import commands
from services.firebase.Countries import Countries
from utils.Embed import EmbedGenerator
from discord.utils import get
class CountryManager(Countries, commands.Cog, name="CountryManager"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    async def cog_check(self, ctx):
        admin = get(ctx.guild.roles, name="Admin")
        if not admin:
            await ctx.send("No se han encontrado permisos de administrador")

        
    @commands.command(
        name="save",
        description="Guarda un pais en la base de datos",
    )
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
    async def getAllCtrys(self, ctx):
        countryList = self.getCountries
        
        if type(countryList) is list and len(countryList) > 0:
            embed = EmbedGenerator("Paises", "Todos los paises guardados", "info").getEmbed

            for country in countryList:
                embed.add_field(name=country.id, value=country.to_dict()['country'])
            
            await ctx.send(embed=embed)
        else:
            await ctx.send(countryList)
    
    @commands.command(
        name="delCtry",
        description="Elimina un pais de la base de datos",
    )
    async def removeCountryByName(self, ctx, name):
        message = self.removeByName(name)
        await ctx.send(message)
    
    @commands.command(
        name="delAll",
        description="Elimina todos los paises de la base de datos",
    )
    @commands.has_permissions(administrator=True)
    async def removeAllCtrys(self, ctx):
        message = self.removeAll()
        await ctx.send(message)
        

def setup(bot: commands.Bot):
    bot.add_cog(CountryManager(bot))