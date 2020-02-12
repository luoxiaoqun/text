import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
   print(">> Bot is online <<") 

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(677054558186373141)
   await channel.send(f'{member}join')
   
   
@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(677054558186373141)
   await channel.send(f'{member}leave')


bot.run('Njc3MDExODM3OTU0MjkzODEx.XkOjPQ.4A8RuGtM1M6wbPquc2cTJOC3VLQ') 

