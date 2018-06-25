import discord  #stuff to include lolz
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import sys, os
import aiohttp
import datetime, json
import random
import math
import requests

##to do:
##    message delete
##    discord stroage


def basic_check(ctx):  ##for funsies
    if (ctx.author == ctx.guild.owner) or (ctx.author.id == 256390874848690176):
        return True
    else:
        return False

def show_check(ctx,args):
    if((args=="Show" or args=="show" or args=="s")and(basic_check(ctx))):
        return True
    else:
        return False


client=commands.Bot( command_prefix=('?', '!', 'cc ', 'Cc ','CC ', 'Coffee ','Coffee Cat '),description='Alright a little something i did for both expertimentaion and Hapiness. This is Yuno')

races= ["Human", "Dwarf","Elf","Pixie","Arakora","Pureblood","Lycan","Triton","Tortle","Lizardfolk","Kobold","Kenku","Halfling","Goblin","Gensai","Elemental","aasimar","Tiefling,","Thrikeen","Void"]

patron= ["Warden","Maiden","Bard","BattleBorn","Satan","Leviathan","Beelzebub","Lillth","Gaia","Kronos","Prom","Atlas"]

client.remove_command('help')


@client.event
async def on_ready():
    print('You are running BasicBot v2.1')
    print('Created by Kaminolucky')
        
##    await client.user.edit(username='Coffee Cat')
    return await client.change_presence(activity=discord.Game(name='Rolling the dice,picking the lovers'))


@client.event
async def on_member_join(member):
    x = None  #Do not change this. This will really help us support you, if you need support.
    for i in member.guild.channels:
        if i.name == 'lobby':
            x = i
    y="Hello" + member.mention+"It's a wonderful chance to meet you, welcome to this Rp Server. I am Coffee. use !help to see commands"
    await x.send(y)
            
@client.command()
async def hi(ctx):
    await ctx.send("I'm not crazy. My reality is just different than yours.")

@client.command()
async def age(ctx):
    x= ctx.guild.created_at
    da = datetime.timedelta(days=8)
    y= datetime.datetime.now()
    d=datetime.timedelta(days=y.day)
    z=x.month-y.month
    s= "This server was created at" + x.strftime(("%d %m %y")) + "\n that makes the age " +str(z)+" months and " +str(da.days +d.days)
    await ctx.send(s)

@client.command()
async def pick(ctx, *, args):
    'A pick device. Uses a list so i think any number of arguments can work'
    y = str(args)
    x = random.choice(y.split(','))
    await ctx.send('Umm..I Picked: ' + x)

@client.command()
async def randrace(ctx,args=1):
    'A pick device. Uses a list so i think any number of arguments can work'
    x=""
    for i in range(0,args):
        x += random.choice(races)+ ","
    await ctx.send('Umm..I Picked: ' + x)

@client.command()
async def randpatron(ctx,args=1):
    'A pick device. Uses a list so i think any number of arguments can work'
    x=""
    for i in range(0,args):
        x += random.choice(patron)+","
    await ctx.send('Umm..I Picked: ' + x)

    
@client.command()
async def roll(ctx, *, args):
    'Rolls a dice. Formatted as  <no od dice>d<no of sides> eg. 3d10'
    y = str(args).replace(' ', '')
    x = ''
    for i in y:
        if i in ('+', '-', '*', '/'):
            break
        x += i
    z = x.split('d')
    no = int(z[0])
    limit = int(z[1])
    rolls = list()
    for i in range(no):
        rolls.append(random.randint(1, limit))
    res = 'Roll(s):'
    for i in rolls:
        res += ' ' + str(i)
    res += ' || Sum='
    s = str(sum(rolls))
    y = y.replace(x, s)
    res += str(eval(y))
    await ctx.send(res)


@client.command()
async def dab(ctx, *, args='1'):
    'Guess what this does'
    print('dab')
    try:
        y = int(args)
        if y > 10:
            y = 10
    except discord.ext.commands.errors.MissingRequiredArgument:
        print('hey there')
        y = 1
    for i in range(y):  ##@client.command(pass_context=True)
        await ctx.send(':dab:')  ##async def quote(ctx):
        await asyncio.sleep(0.5)  ##        """The first command in the process of making it YUNo?"""


@client.command()
async def cat(ctx):
    em = discord.Embed(title="Cat Pix")
    async with aiohttp.get("http://thecatapi.com/api/images/get") as res:
        em.set_image(url=res.url)
    res.close()
    await ctx.send(embed= em)

@client.command()
async def dog(ctx):
    em = discord.Embed(title="Doggo Pix")
    async with aiohttp.get("https://dog.ceo/api/breeds/image/random") as res:
        x= json.loads(await res.text())
    res.close()
    em.set_image(url=x['message'])
    await ctx.send(embed= em)


@client.command() 
async def docs(ctx,args=None):
    em = discord.Embed(title="Docs")
    em.add_field(name="Starless" ,value="https://docs.google.com/document/d/1QM77dBRFlyKUdzJytyxbBh6osvd629B-QOyRDBm3Kiw/edit#'")
    cq="""
https://docs.google.com/document/d/14OTbOugCFiI0qwtVxo9eQsbRY1ogQ5hsN7IbWMVZ3TQ/edit#heading=h.wc2ek914tv85
"""
    em.add_field(name="Conquest" ,value = cq)
    if(show_check(ctx,args)):
        await ctx.send(embed=em)
    else:
        await ctx.author.send(embed=em)
        await ctx.send("Look into your dms....")

@client.command() 
async def sl(ctx):
    em = discord.Embed(title="Docs")
    s="""
Main doc:\n https://docs.google.com/document/d/1QM77dBRFlyKUdzJytyxbBh6osvd629B-QOyRDBm3Kiw/edit# 

Inventory: \nhttps://docs.google.com/document/d/1ULrJfzj9rd7Pd7SHX_0pgcrXLLR77q5qvGk04OSZteQ/edit 


Shops:\nhttps://docs.google.com/document/d/1k6ivv_ljadAuKqQ2st1kDrIt9x2-vHogqU5Q8S6n0yA/edit
\n https://docs.google.com/document/d/1IieJwLf7mGsBjMlmEYO2A4J3lYNcHEEm7aZ-NQEscJY/edit 
"""
    em.add_field(name="Starless", value = s)
    await ctx.author.send(embed=em)
    await ctx.send("Look into your dms....")



##async def sendmsg(ctx,*,args):
@client.command()  ##        x=args.split(',')
async def calc(ctx, *, args):  ##        y=""
    'Calcs a given expression, someone needs to see how far this goes tho'  ##        for i in ctx.server.members:
    try:  ##            if(i.mentioned_in(args)):
        x = eval(args)  ##                y=i
    except ZeroDivisionError:  ##        await client.send_message(y,x[0])
        x = 'Bish , you just divided by zero'  ##
    await ctx.send('Result: ' + str(x))


@client.command()
async def draw(ctx, args=None):
    if (args == 'Face') or (args == 'face') or (args == 'f'):
        x = 18
    else:
        x = 54
    y = random.randint(1, x)
    if (y == 17) and ((args == 'Face') or (args == 'face') or (args == 'f')):
        y = 53
    elif (y == 18) and ((args == 'Face') or (args == 'face') or (args == 'f')):
        y = 54
    deck = ('https://www.random.org/playing-cards/' + str(y)) + '.png'
    em = discord.Embed(title='The Card Has been Drawn')
    em.set_image(url=deck)
    await ctx.send(embed=em)


@client.command()
async def time(ctx):
    dt=datetime.datetime.now()
    
    i_time=dt+datetime.timedelta(hours=5,minutes=30)
    singa_time=dt+datetime.timedelta(hours=8)
    b_time=dt+datetime.timedelta(hours=1)
    a_time=dt+datetime.timedelta(hours=10)
    est=dt-datetime.timedelta(hours=8)
    x="\n"+"GMT: "+dt.strftime("%H:%M")+"\nEST: "+est.strftime("%H:%M")+"\nBritish Time: "+b_time.strftime("%H:%M")+"\nIndian Time: " +i_time.strftime("%H:%M")+"\nSingapore and Phillpines Time: "+singa_time.strftime("%H:%M")+"\nAustralia Time: "+a_time.strftime("%H:%M")   
    await ctx.send(x)

@client.command()
async def help(ctx):
    x= discord.Embed(title= "HELP")
    x.add_field(name="Help",value="Syntax: !help \nUse: Displays this message", inline=False)
    x.add_field(name="Hi",value="Syntax: !hi \nUse: To test if the bot is on or not", inline=False)
    x.add_field(name="Pick",value="Syntax: !pick choice a, choice b....,choice n \nUse: To pick out of the given choices", inline=False)
    x.add_field(name="Roll",value="Syntax: !roll <no of dice>d<no of sides> \nUse: To roll dice. \nEg !roll 1d20", inline=False)
    x.add_field(name="Dab",value="Syntax: !dab \nUse: GUESS YOU BLOODY BISHES", inline=False)
    x.add_field(name="Cat",value="Syntax: !cat \nUse: Cat Pix ^-^", inline=False)
    x.add_field(name="Dog",value="Syntax: !dog \nUse: DOGGO", inline=False)
    x.add_field(name="Docs",value="Syntax:!docs \nUse: Shows the docs of all the rps in this server", inline=False)
    x.add_field(name="Starless",value="Syntax: !sl \nUse: Shows docs relavent to sl", inline=False)
    x.add_field(name="Calc",value="Syntax: !calc <expresion> \nUse: Calculates yoru expression, us +, -, *, / \n Eg !calc 3+2*3", inline=False)
    x.add_field(name="Time",value="Syntax: !time \nUse: tells time in diffrent regions, if you region is not there pm kami", inline=False)
    await ctx.send(embed=x)



@client.command()
async def test(ctx, *,args):
    await ctx.guild.create_text_channel(args)

@client.command()
async def ships(ctx):
        x="""
    \nsilly mortals and thier fantasies. *throw doc* here

    \nhttps://docs.google.com/document/d/1ZRUoxHeY8bKjp0eCOvo6ilu-7O03CwTd2ikRv2iUs9I/edit
        """
        await ctx.send(x)

##@client.command()
##@commands.check(basic_check)
##async def mute(ctx,args):
##    for i in ctx.guild.members:
##        if(i.mentioned_in(ctx.message)):
##            await i.add_roles()
##    await ctx.send("Muted Get REKT")

@client.command()
@commands.check(basic_check)
async def kick(ctx,args):
    for i in ctx.guild.members:
        if(i.mentioned_in(ctx.message)):
            await i.ban()
    await ctx.send("Banned")

    

client.run('NDA3MDY0OTIyMTU4MjY4NDE2.DdwY-w.l_CjW6tratHXia6MUJ-xll3Ti5Q')
