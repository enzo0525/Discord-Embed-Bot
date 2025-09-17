from nextcord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def get_links(self, ctx):
        await ctx.send('Getting links...')

        links = []
        channel = ctx.channel
        async for message in channel.history():
            if message.author == self.bot.user:
                continue
            elif message.content.startswith('https://'):
                links.append(message.content)

        links_str = '\n'.join(links)
        await ctx.send(f'```{links_str}```')

def setup(bot):
    bot.add_cog(Commands(bot))