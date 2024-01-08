from nextcord.ext import commands
import nextcord
import creds
import os

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(intents=intents)

for fn in os.listdir('cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f'cogs.{fn[:-3]}')
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run(creds.BOT_TOKEN)