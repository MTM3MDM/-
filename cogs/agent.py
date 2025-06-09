from discord.ext import commands
import discord
import random

class Agent(commands.Cog, name="Agent Department"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.quantum_responses = [
            "Analyzing multiverse fluctuations...",
            "Calculating quantum paths...",
            "Observing superposed states...",
            "Channeling quantum brain waves...",
            "Tuning into the cosmic classroom..."
        ]
        self.predictions = [
            "Quantum future is bright!",
            "Uncertainty is certain.",
            "Your wave function will collapse in your favor.",
            "Prepare for quantum excellence!"
        ]
        self.brainwaves = [
            "~..~..~..~..~ quantum ripple detected ~..~..~..~",
            "~~~∞~~~ observing brainwave interference ~~~∞~~~",
            "--<>-- syncing to neural frequencies --<>--",
        ]

    @commands.command(name="quantum", help="Get a quantum thought from the bot.")
    async def quantum(self, ctx: commands.Context):
        await ctx.send(random.choice(self.quantum_responses))

    @commands.command(name="echo", help="Echo the provided message.")
    async def echo(self, ctx: commands.Context, *, message: str):
        await ctx.send(message)

    @commands.command(name="predict", help="Receive a quantum prediction.")
    async def predict(self, ctx: commands.Context):
        await ctx.send(random.choice(self.predictions))

    @commands.command(name="brainwave", help="Display a random brainwave pattern.")
    async def brainwave(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Quantum Brainwave",
            description=random.choice(self.brainwaves),
            color=0xAA00FF,
        )
        await ctx.send(embed=embed)

    @commands.command(name="about", help="Information about the bot.")
    async def about(self, ctx: commands.Context):
        embed = discord.Embed(
            title="엄채희 중학교 3학년",
            description="초고급 Quantum Brain Bot",
            color=0x00FFAA,
        )
        await ctx.send(embed=embed)
