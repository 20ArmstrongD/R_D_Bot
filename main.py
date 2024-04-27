#code 


import os
import discord
from discord.ext import commands
import openai

# loading the variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# OpenAI setup
openai.api_key = os.getenv('OPENAI_KEY')
openai.organization = os.getenv('OPENAI_ORG')

# when the bot is ready



# creating the message




# starting the bot
bot.run(os.getenv('DISCORD_TOKEN'))
print("")