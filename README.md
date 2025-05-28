# Discord Embed Bot

The Discord Embed Bot is designed to fix embed links from various platforms on Discord, including Twitter, Instagram, and TikTok.

Follow these simple steps to set up and use the bot:

### Requirements:

```
pip install -r requirements.txt
```


### Setup:

1. **Create a Discord Bot:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new Discord bot.
   - Copy the generated TOKEN.

2. **Configure Environment Variables:**
   - Create a `.env` file in the project root directory.
   - Add your bot token to the file like this:
```
BOT_TOKEN=your_token_here
```

### Usage:

- **Run the Bot:**
  - Execute the bot script (`discord_bot.py`) to make it operational.

- **Automatic Embedding:**
  - When anyone shares a link from supported platforms (listed below), the bot will automatically:
    - Delete the original message.
    - Embed a new message with the content of the shared link.
    - React to the embedded message with a 🗑️ (trash) emoji.
    - If the original sender clicks the trash emoji, the bot will delete the embedded message.

### Supported Platforms:
- Twitter / X
- Instagram
- TikTok