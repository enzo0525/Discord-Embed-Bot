import re
import io
from urllib.parse import urlparse
from nextcord.ext import commands
import nextcord

# Find http/https URLs in text
URL_RE = re.compile(r'https?://\S+', re.IGNORECASE)
TRAILING_PUNCT = '.,!?:;)]}\'"'

# Block common media extensions (you said no gifs/images/attachments)
MEDIA_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp",
              ".tiff", ".svg", ".mp4", ".mov", ".webm", ".mkv", ".avi", ".gifv")

# Optionally exclude well-known GIF providers entirely (comment out if not needed)
EXCLUDE_DOMAINS = {
    "tenor.com", "media.tenor.com",
    "giphy.com", "media.giphy.com",
    "discord.gg", "discord.com",
    "pbs.twimg.com"
}

def is_non_media_http_url(url: str) -> bool:
    p = urlparse(url)
    if p.scheme not in ("http", "https") or not p.netloc:
        return False
    # filter gif/image/video by extension (handles queryless paths)
    path_lower = p.path.lower()
    if any(path_lower.endswith(ext) for ext in MEDIA_EXTS):
        return False
    # also exclude some gif providers entirely
    host = p.netloc.lower()
    if host in EXCLUDE_DOMAINS:
        return False
    return True


class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def get_links(self, ctx: commands.Context):
        # Work silently in channel; notify via DM
        try:
            await ctx.author.send("Collecting message-only links…")
        except nextcord.Forbidden:
            return await ctx.reply("I can't DM you. Please enable DMs from server members and try again.", mention_author=False)

        links = set()

        async for message in ctx.channel.history(limit=None, oldest_first=True):
            if message.author == self.bot.user:
                continue

            text = message.content or ""
            if not text:
                continue

            for m in URL_RE.finditer(text):
                # Trim trailing punctuation Discord users often leave after links
                url = m.group(0).rstrip(TRAILING_PUNCT)
                if is_non_media_http_url(url):
                    links.add(url)

        if not links:
            try:
                return await ctx.author.send("No message-body links found.")
            except nextcord.Forbidden:
                return await ctx.reply("I can't DM you. Please enable DMs from server members and try again.", mention_author=False)

        output = "\n".join(sorted(links))

        if len(output) <= 1900:
            try:
                await ctx.author.send(output)
            except nextcord.Forbidden:
                return await ctx.reply("I can't DM you. Please enable DMs from server members and try again.", mention_author=False)
        else:
            buf = io.BytesIO(output.encode("utf-8"))
            file = nextcord.File(buf, filename="links.txt")
            try:
                await ctx.author.send("Too many links to display; here’s a file:", file=file)
            except nextcord.Forbidden:
                return await ctx.reply("I can't DM you. Please enable DMs from server members and try again.", mention_author=False)


def setup(bot):
    bot.add_cog(Commands(bot))