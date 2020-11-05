import discord
import os
from discord.ext import commands, tasks
from pymongo import MongoClient
from util import get_environment_variable

TOKEN = get_environment_variable("TOKEN")
MONGO = get_environment_variable("MONGO_URI")
PREFIX = "!py"

intents = discord.Intents(messages= True, guilds= True)
bot = commands.Bot(command_prefix = PREFIX, intents=intents)

cog_list = ['cogs.config']




if __name__ == '__main__':
    for extension in ls_cog:
        bot.load_extension(extension)

bot.run(TOKEN)
