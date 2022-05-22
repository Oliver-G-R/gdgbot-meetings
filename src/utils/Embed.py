from discord import Embed
class EmbedGenerator: 
    def __init__(self, title, description, typeEmbed):
        self.title = title
        self.description = description
        self.typeEmbed = typeEmbed
    
    @property
    def getEmbed(self):
        embed = Embed(
            title=self.title,
            description=self.description,
            color=self.__getColorType
        )
        return embed

    @property
    def __getColorType(self):
        if self.typeEmbed == "success":
            return 0x00ff00
        elif self.typeEmbed == "error":
            return 0xff0000
        elif self.typeEmbed == "info":
            return 0x0000ff
        else:
            return 0xffffff