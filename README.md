# Discord Embed Bot

The Discord Embed Bot is designed to fix embed links from various platforms on Discord, including Twitter, Instagram, Reddit, and TikTok. Follow these simple steps to set up and use the bot:

### Requirements:
```
python3 -m pip install -r requirements.txt
```

### Setup:

1. **Create a Discord Bot:**
   - Go to the Discord Developer Portal and create a new Discord bot.
   - Copy the generated TOKEN.

2. **Update Token in 'creds.py':**
   - Open the 'creds.py' file.
   - Replace the placeholder between the quotation marks with your bot's TOKEN.

### Usage:

- **Run the Bot:**
  - Execute the bot script (discord_bot.py) to make it operational. 

- **Automatic Embedding:**
  - When anyone shares a link from supported platforms (listed at the top of the page), the bot will automatically:
    - Delete the original message.
    - Embed a new message with the content of the shared link.

### Supported Platforms:
- Twitter / X
- Instagram
- Reddit
- TikTok