import discord
from discord.ext import commands 
import random 
import requests
from datetime import date 

client = commands.Bot(command_prefix= '.')

# Put your discord API key here.
discord_api_key = ""


@client.event
async def on_ready():
    """
    Tells the status of bot
    """
    print("Bot is ready")


@client.command()
async def ping(ctx):
    """
    measures the client latency
    """
    await ctx.send(f'Pong! Latency = {client.latency * 1000} ms')






@client.command(aliases=['8ball','play'])
async def _8ball(ctx, *, question):
    """
    simple 8ball question command
    """
    responses =['Yes','No','Maybe']    
    await ctx.send(f'Question : {question} \n Answer: {random.choice(responses)}')




@client.command(aliases=['work','tasks'])
async def standup(ctx,tasks):
    """
    function to send a task model to the site to display it publicly
    """
    title = f'{ctx.message.author.name} on {date.today()} '
    l=tasks.split(',')
    s = '\n'
    s = s.join(l)
    url = 'http://127.0.0.1:8000/api/seeOthers/'
    postDict = {'title':title,'content':s}
    req = requests.post(url,json=postDict)
    await ctx.send(f'Standup by {ctx.message.author.mention} \n \n \n {s} \n \n \n Do check out {url}')



client.run(discord_api_key)
