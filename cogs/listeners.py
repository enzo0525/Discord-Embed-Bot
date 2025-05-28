from nextcord.ext import commands

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mapping_links = {
            'https://x.com': 'https://fixupx.com',
            'https://twitter.com': 'https://fxtwitter.com',
            'https://www.tiktok.com': 'https://vxtiktok.com',
            'https://www.instagram.com': 'https://www.ddinstagram.com',
        }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        for prefix, fixed in self.mapping_links.items():
            if prefix in message.content and checkIfValid(message.content):
                temp = message.content.split(prefix)
                new_link = fixed + temp[1]
                new_message = f'{temp[0]}\n**Source:** {message.author.mention}\n{new_link}'
                await message.delete()
                sent_message = await message.channel.send(new_message)
                await sent_message.add_reaction('🗑️')
                return
            
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.bot.user:
            return
        
        if reaction.message.content.split('**Source:**')[1][3:21] == str(user.id):
            await reaction.message.delete()


def checkIfValid(link: str):
    return "/status/" in link or "/p/" in link or "/reel/" in link

def setup(bot):
    bot.add_cog(Listener(bot))