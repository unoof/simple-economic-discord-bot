import discord, os, aiohttp

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
CHAT_CHANNEL_ID = int(os.getenv("CHAT_CHANNEL_ID"))

class Chat_bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session: aiohttp.ClientSession | None = None
        
    async def cog_load(self):
        self.session = aiohttp.ClientSession()

    async def cog_unload(self):
        if self.session:
            await self.session.close()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user or message.reference is not None:
            return
        
        if message.content.startswith("e."):
            return

        if CHAT_CHANNEL_ID and message.channel.id != CHAT_CHANNEL_ID:
            return

        async with self.session.get(
            "https://api.some-random-api.com/chatbot",
            params={
                "message": message.content,
                "key": os.getenv("SRA_TOKEN")
            }
        ) as reply:
            data = await reply.json()

        if data.get("response"):
            await message.reply(
                data["response"],
                mention_author=False
            )

async def setup(bot: commands.Bot):
    await bot.add_cog(Chat_bot(bot))