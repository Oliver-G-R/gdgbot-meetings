import os
from services.firebaseServices import Countries
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    client = discord.Client()
    TOKEN_BOT = os.getenv('DC_TOKEN')
    countries = Countries()

    client = commands.Bot(command_prefix="!", description="A bot for the Discord server.")
    client.remove_command("help")

    @client.event
    async def on_ready():
        print("Bot is ready!")

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(
                "El comando no existe, intenta con !info para ver los comandos disponibles"
            )
    
    @client.command()
    @commands.has_permissions(administrator=True)
    async def clear(ctx):
        await ctx.channel.purge(limit=100)
        await ctx.send("Se han borrado los mensajes")
    
    
    @client.command()
    @commands.has_permissions(administrator=True)
    async def saveCountry(ctx, country):
        try:
            Countries.saveCountries(country)
            await ctx.send("Guardado!")
        except Exception as e:
            print(e)
            await ctx.send("Error al guardar")

    @client.command()
    @commands.has_permissions(administrator=True)
    async def getAllCtrys(ctx):
        try:
            
            embed = discord.Embed(
                title="Paises",
                description="Lista de paises",
                color=0x00ff00
            )

            for country in countries.getCountries:
                embed.add_field(name=country.id, value=country.to_dict()['country'])
    
            await ctx.send(embed=embed)
           
        except Exception as e:
            print(e)
            await ctx.send("Error al obtener")

    client.run(TOKEN_BOT)