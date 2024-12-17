import discord
from googletrans import Translator, LANGUAGES
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Translator Setup
translator = Translator()

# Discord Client Setup
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# On Ready Event
@client.event
async def on_ready():
    logging.info(f'Bot logged in as {client.user}')

# On Message Event
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!translate'):
        try:
            args = message.content.split()
            if len(args) < 3:
                await message.channel.send("Usage: !translate <language_code> <user_id>")
                return

            lang_code, user_id = args[1], args[2]

            # Language Support Check
            if lang_code not in LANGUAGES.keys():
                await message.channel.send(f'Unsupported language code: `{lang_code}`.')
                return

            # Fetch Recent User Message
            user_message = await fetch_user_message(message.channel, user_id)
            if not user_message:
                await message.channel.send(f"No recent message found for user ID `{user_id}`.")
                return

            # Translate Message
            translated_text = translator.translate(user_message.content, dest=lang_code).text
            await message.channel.send(f"**Translated Message:**\n{translated_text}")

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            await message.channel.send("An error occurred. Please try again later.")

# Helper Function to Fetch Recent Message
async def fetch_user_message(channel, user_id):
    async for msg in channel.history(limit=100):
        if str(msg.author.id) == user_id:
            return msg
    return None

# Run Bot
def run_discord_bot():
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if TOKEN:
        client.run(TOKEN)
    else:
        logging.error("Discord bot token is missing!")
