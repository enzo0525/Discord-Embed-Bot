from nextcord.ext import commands

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mapping_links = {
            'https://x.com': 'https://fixupx.com',
            'https://twitter.com': 'https://fxtwitter.com',
            'https://www.tiktok.com': 'https://vxtiktok.com',
            'https://www.instagram.com': 'https://www.ddinstagram.com',
            'https://www.reddit.com': 'https://www.vxreddit.com'
        }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        for prefix, fixed in self.mapping_links.items():
            if message.content.startswith(prefix):
                temp = message.content.split(prefix)
                new_link = fixed + temp[1]
                await message.delete()
                await message.channel.send(new_link)
                return

def setup(bot):
    bot.add_cog(Listener(bot))