import discord
from discord.ext import commands
import json

# Load configuration
with open('config/config.json') as config_file:
    config = json.load(config_file)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

initial_extensions = ['cogs.moderation', 'cogs.logging']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(config["token"])  # Running NovaBot
