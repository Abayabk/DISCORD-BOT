import os
import discord
import asyncio
from discord.ext import commands
from keep_alive import keep_alive
bot = commands.Bot(command_prefix='`')
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hibot(ctx):
  await ctx.send("hello")

@bot.command()
async def hello(ctx):
  await ctx.send("hi bro")

@bot.command()
async def owner(ctx):
  await ctx.send("owner name")

@bot.command()
async def add(ctx, a: int, b : int):
   await ctx.send(a + b)

@bot.command()
async def sub(ctx, a: int, b : int):
   await ctx.send(a - b) 

@bot.command()
async def multiply(ctx, a: int, b : int):
   await ctx.send(a * b)

@bot.command()
async def divide (ctx, a: int, b : int):
   await ctx.send(a / b)   

keep_alive()

bot.run(os.getenv('TOKENop'))