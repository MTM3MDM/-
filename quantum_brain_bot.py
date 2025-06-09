import os
import asyncio
import logging

import discord
from discord.ext import commands

from cogs.agent import Agent
from cogs.admin import Admin

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="채희야 ",
    description="엄채희 중학교 3학년 Quantum Brain Bot",
    intents=intents,
)

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

async def main():
    async with bot:
        await bot.add_cog(Agent(bot))
        await bot.add_cog(Admin(bot))
        await bot.start(TOKEN)

if __name__ == "__main__":
    if TOKEN is None:
        raise EnvironmentError("DISCORD_TOKEN environment variable not set.")
    asyncio.run(main())
