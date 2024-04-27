import os
import discord
from discord.ext import commands
from openai import OpenAI

# loading the variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# OpenAI setup
client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY"),
)

# when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected')


# creating the message
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    prompt = message.content
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        
        print(prompt)
        response = chat_completion.choices[0].message.content
        print(response)

        await message.channel.send(response)  # Sending the response to the same channel where the message was received

    except Exception as e:
        print(e)

    await bot.process_commands(message)

# starting the bot
bot.run(os.getenv('DISCORD_TOKEN'))
print("Yoo, Suuuuup")
