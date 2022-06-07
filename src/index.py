import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    TOKEN_BOT = os.getenv('DC_TOKEN')
    pathCogs = './src/cogs'
    bot = commands.Bot(
        command_prefix="!", 
        description="A bot for the Discord server.")
    bot.remove_command("help")

    try: 
        print("Cargando...")
        for folder in os.listdir(pathCogs):
            for cog in os.listdir(f'{pathCogs}/{folder}'):
                if cog.endswith('.py'):
                    print(f"Cog {cog}")
                    bot.load_extension(f'cogs.{folder}.{cog[:-3]}')
    except Exception as e:
        print(e)
        print("Error al cargar los comandos")
    
    try:
        @bot.event
        async def on_ready():
            print("El bot esta listo!")
        
        bot.run(TOKEN_BOT)
    except Exception as e:
        print(e)
        print("Error al iniciar el bot")