import discord
from discord.ext import commands
import random
from random import choice

responses = "Cara", "Escudo"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def Tira_moneda(ctx):
    await ctx.send(f"{random.choice(responses)}")

@bot.command()
async def sumas(ctx):
    await ctx.send("La adición o suma es la operación matemática de composición que consiste en combinar o añadir dos números o más para obtener una cantidad final o total.")

@bot.command()
async def restas(ctx):
    await ctx.send("La resta o la sustracción es una operación aritmética que se representa con el signo; representa la operación de eliminación de objetos de una colección.")

@bot.command()
async def multiplicacion(ctx):
    await ctx.send("la multiplicación es una operación binaria y derivada de la suma que se establece en un conjunto numérico.​")

@bot.command()
async def division(ctx):
    await ctx.send("En la matemática, la división es una operación parcialmente definida en el conjunto de los números enteros.​")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run("Bot Token")
