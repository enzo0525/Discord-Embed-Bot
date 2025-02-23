from nextcord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def delete(self, ctx):
        async for message in ctx.channel.history(limit=50):
            if (f'@{ctx.author.id}') in message.content and message.author.id == self.bot.user.id:
                await message.delete()
                await ctx.send('>>> Message deleted.')
                return
        await ctx.send('>>> Could not find message or message is too old.')

def setup(bot):
    bot.add_cog(Commands(bot))