from nextcord.ext import commands
from dotenv import load_dotenv
import nextcord
import os

load_dotenv()

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

for fn in os.listdir('cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f'cogs.{fn[:-3]}')
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run(os.getenv('BOT_TOKEN'))
