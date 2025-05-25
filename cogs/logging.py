from discord.ext import commands
import discord
from utils.firebase import log_to_firebase

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            log_data = {
                'author': str(message.author),
                'content': message.content,
                'channel': str(message.channel),
                'timestamp': str(message.created_at)
            }
            log_to_firebase('messages', log_data)

def setup(bot):
    bot.add_cog(Logging(bot))
