#code 


import os
import discord
from discord.ext import commands
from openai import OpenAI
import openai

# loading the variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# OpenAI setup

client = OpenAI(api_key=os.environ.get('OPENAI_KEY')
)
openai.api_key = os.getenv('OPENAI_KEY')
openai.organization = os.getenv('OPENAI_ORG')

# when the bot is ready
@bot.event
async def onready ():
    print(f'{bot.user.name} has connected')


# creating the message
@bot.event
async def onmessage (message):
    if message.author.bot:
        return
    
    params = {"model": "gpt-3.5-turbo", 
              "messages": [{"role": "user", "content": message.content}],
              "max_tokens": 30,
              "stop": ["Mantis Taboggen, M.D.", "ribone_", "BigDon(g)" ]
    }

    try:
        MantisResponse = openai.ChatCompletion.create(**params)

        print(message.content)
        print(MantisResponse["choices"][0]["message"]["content"])

        await message.reply(MantisResponse["choices"][0]["message"]["content"])

    except Exception as e:
        print(e)

    await bot.process_commands(message)



# starting the bot
bot.run(os.getenv('DISCORD_TOKEN'))
print("")