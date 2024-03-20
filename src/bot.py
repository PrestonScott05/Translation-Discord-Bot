import discord
from googletrans import Translator, LANGUAGES
import os
from dotenv import load_dotenv

# load env vars
load_dotenv()

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)
translator = Translator()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!translate'):
        args = message.content.split()
        if len(args) < 3:
            await message.channel.send("Usage: !translate <language_code> <user_id>")
            return
        
        _, lang_code, user_id = args[:3]

        if lang_code not in LANGUAGES.keys():
            await message.channel.send(f'Language code {lang_code} is not supported.')
            return

        async for msg in message.channel.history(limit=50):
            if str(msg.author.id) == user_id:
                translated_text = translator.translate(msg.content, dest=lang_code).text
                await message.channel.send(translated_text)
                break
        else:
            await message.channel.send(f"No recent message found for user ID {user_id}.")

client.run(os.getenv('DISCORD_BOT_TOKEN'))
