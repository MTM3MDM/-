from discord.ext import commands
import discord

class Admin(commands.Cog, name="Admin Department"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx: commands.Context):
        return ctx.author.guild_permissions.administrator

    @commands.command(name="create_role", help="Admin only: create a new role.")
    async def create_role(self, ctx: commands.Context, *, role_name: str):
        guild = ctx.guild
        if guild is None:
            await ctx.send("This command can only be used in a server.")
            return
        await guild.create_role(name=role_name)
        await ctx.send(f"Role `{role_name}` created.")

    @commands.command(name="shutdown", help="Admin only: shut down the bot.")
    async def shutdown(self, ctx: commands.Context):
        await ctx.send("Shutting down...")
        await ctx.bot.close()
