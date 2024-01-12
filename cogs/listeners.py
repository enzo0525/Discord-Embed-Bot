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
            if prefix in message.content:
                temp = message.content.split(prefix)
                new_link = fixed + temp[1]
                await message.delete()
                await message.channel.send(f'{temp[0]}\n**Source:** {message.author.mention}\n{new_link}')
                return
            
    @commands.command()
    async def delete(self, ctx):
        async for message in ctx.channel.history(limit=50):
            if (f'@{ctx.author.id}') in message.content and message.author.id == self.bot.user.id:
                await message.delete()
                await ctx.send('>>> Message deleted.')
                return
        await ctx.send('>>> Could not find message or message is too old.')

def setup(bot):
    bot.add_cog(Listener(bot))