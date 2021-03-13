import discord
from discord.ext import commands 
import random 
import requests
from datetime import date 

client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency = {client.latency * 1000} ms')

@client.command(aliases=['8ball','play'])
async def _8ball(ctx, *, question):
    responses =['Yes','No','Maybe']    
    await ctx.send(f'Question : {question} \n Answer: {random.choice(responses)}')

@client.command(aliases=['work','tasks'])
async def standup(ctx,tasks):
    title = f'{ctx.message.author.name} on {date.today()} '
    l=tasks.split(',')
    s = '\n'
    s = s.join(l)
    url = 'http://127.0.0.1:8000/api/'
    postDict = {'title':title,'content':s}
    req = requests.post(url,json=postDict)
    await ctx.send(f'Standup by {ctx.message.author.mention} \n \n \n {s} \n \n \n Do check out {url}')



client.run('ODE4NDAyODExOTA5MTExODA4.YEXjAw.xom7miqiXUIhm3C4rY2hQ3SrPTw')

