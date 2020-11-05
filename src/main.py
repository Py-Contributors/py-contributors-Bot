import discord
import os
from discord.ext import commands, tasks
from pymongo import MongoClient
from util import get_environment_variable

TOKEN = get_environment_variable("TOKEN")
MONGO = get_environment_variable("MONGO_URI")
