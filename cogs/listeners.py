from nextcord.ext import commands

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mapping_links = {
            'https://x.com': 'https://fixupx.com',
            'https://twitter.com': 'https://fxtwitter.com',
            'https://instagram.com': 'https://ddinstagram.com',
            'https://www.instagram.com': 'https://ddinstagram.com',
            'https://www.twitter.com': 'https://fxtwitter.com',
            'https://www.x.com': 'https://fixupx.com',
        }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        for prefix, fixed in self.mapping_links.items():
            if prefix in message.content and checkIfValid(message.content):
                temp = message.content.split(prefix)
                new_link = parseLink(fixed, temp[1])
                new_message = f'{temp[0]}\n**Source:** {message.author.mention}\n{new_link}'
                await message.delete()
                sent_message = await message.channel.send(new_message)
                await sent_message.add_reaction('🗑️')

                if 'fixupx.com' in new_link or 'fxtwitter.com' in new_link or 'ddinstagram.com' in new_link:
                    await sent_message.add_reaction('🔍')
                return
            
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.bot.user:
            return
        
        if reaction.message.author == self.bot.user:
            message_content = reaction.message.content
            user_id_from_message = message_content.split('**Source:**')[1][3:21]
            source_message = message_content.split('\n')[0]

            if user_id_from_message == str(user.id) and reaction.emoji == '🔍':
                link = message_content.split('\n')[-1]
                await reaction.message.delete()
                separated_link = link.split('//', 1)
                new_link = await reaction.message.channel.send(f'{source_message}\n{separated_link[0]}//d.{separated_link[1]}')
                await new_link.add_reaction('🗑️')

            if user_id_from_message == str(user.id) and reaction.emoji == '🗑️':
                await reaction.message.delete()
        

def checkIfValid(link: str):
    return "/status/" in link or "/p/" in link or "/reel/" in link

def parseLink(new_link: str, rest_of_link: str):
    return new_link + rest_of_link.split('?')[0]

def setup(bot):
    bot.add_cog(Listener(bot))