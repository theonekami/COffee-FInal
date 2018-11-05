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
import dat

#once upon a time a NErd said "Nah your include will not be hbig....Please kill him for me"

##to do:
##    message delete
##    discord stroage
bot_admin_discriminators = [256390874848690176,131205596732063744] # These users have access to the bot's admin functions on all servers

def value_in_list(ls, val): # ls: a list; val: a value
    for test_value in ls:
        if (test_value == val):
            return True
    return False

def gadmin_ck(ctx): # Check if user is a global bot admin
    return value_in_list(bot_admin_discriminators, ctx.author.id)

def Kami_check(ctx):  ##for funsies
    if (ctx.author.id == 256390874848690176) :
        return True
    else:
        return False

def basic_check(ctx):  ##for funsies
    return ((ctx.author == ctx.guild.owner) or (gadmin_ck(ctx)))

def show_check(ctx,args):
    return ((args=="Show" or args=="show" or args=="s")and(basic_check(ctx)))

##def room_check(ctx):
##    


client=commands.Bot( command_prefix=('?', '!','.', 'cc ', 'Cc ','CC ', 'Coffee ','Coffee Cat '),description='Alright a little something i did for both expertimentaion and Hapiness. This is Yuno')

races= ["Human", "Dwarf","Elf","Pixie","Arakora","Pureblood","Lycan","Triton","Tortle","Lizardfolk","Kobold","Kenku","Halfling","Goblin","Gensai","Elemental","aasimar","Tiefling,","Thrikeen","Void"]

patron= ["Warden","Maiden","Bard","BattleBorn","Satan","Leviathan","Beelzebub","Lillth","Gaia","Kronos","Prom","Atlas"]

home=client.get_channel(508811672970985475)


client.remove_command('help')


@client.event
async def on_ready():
    print('You are running BasicBot v2.1')
    print('Created by Kaminolucky')
    client.load_extension("Role_command")
    client.load_extension("Magic")
##    client.load_extension("Cool_Point")
    
    await home.send("I am REBORN")
##    await client.user.edit(username='Coffee Cat')
    return await client.change_presence(activity=discord.Game(name='Afraid and cold'))


@client.event
async def on_member_join(member):
    x = None  #Do not change this. This will really help us support you, if you need support.
    for i in member.guild.channels:
        if i.name == 'lobby':
            x = i
    y="Hello" + member.mention+"It's a wonderful chance to meet you, welcome to this Rp Server. I am Coffee. use !help to see commands"
    em = discord.Embed(title="New Face")
    em.set_image(url=member.avatar_url)
    await member.addrole("Locked")
    await x.send(y)
    await x.send(embed=em)

            
@client.command()
async def hi(ctx):
    await ctx.send("I'm... Scared")
    await home.send(ctx.author.name+ "Home")

@client.command()
async def age(ctx):
    x= ctx.guild.created_at
    y= datetime.datetime.now()
    z=y-x
    s= "This server was created at " + x.strftime(("%d %m %y")) + "\nThat makes the age " +str(z.days) + " days"
    await ctx.send(s)
    await home.send(ctx.author.name+ "Age")

@client.command()
async def pick(ctx, *, args):
    'A pick device. Uses a list so i think any number of arguments can work'
    y = str(args)
    x = random.choice(y.split(','))
    await ctx.send('Umm..I Picked: ' + x)
    await home.send(ctx.author.name+ "Pick")

@client.command()
@commands.check(Kami_check)
async def heal(ctx):
    x="Minions Victim "
    for i in range(0,40):
        for j in ctx.guild.members:
            if j.nick==x+" #"+str(i):
                await j.edit(nick=None)
    await ctx.send("Let the Mistakes of one god, never haunt you anymore")
    await home.send(ctx.author.name+ "Heal")


@client.command()
async def randrace(ctx,args=1):
    'A pick device. Uses a list so i think any number of arguments can work'
    x=""
    for i in range(0,args):
        x += random.choice(races)+ ","
    await ctx.send('Umm..I Picked: ' + x)
    await home.send(ctx.author.name+ "randrace")

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
@commands.check(Kami_check)
async def Exit(ctx):
    await ctx.guild.leave()

@client.command()
async def dab(ctx, *, args='1'):
    'Guess what this does'
    #em=discord.Emoji(id=498126660546068482, name="dab")
    print('dab')
    try:
        y = int(args)
        if y > 13:
            y = 13
    except discord.ext.commands.errors.MissingRequiredArgument:
        print('hey there')
        y = 1 
    for i in range(y):  ##@client.command(pass_context=True)
        await ctx.send(" <:dab:407026257969152031>")  ##async def quote(ctx):
        await asyncio.sleep(0.5)  ##        """The first command in the process of making it YUNo?"""

@client.command()
async def bad(ctx, *, args='1'):
    'Guess what this does'
    bad=["<:dab:407026257969152031>",
"<:hope:497948063973769256>",
         "<:hypereyes:407028550752010241>",
         "<:sleazybarry:407031302555172884>",
         "<:dpengu:465824541663559680>",
         "<:beegod:407031365725454336>",
         "<:ANIMEEDGE:415712134614220806>",
         "<:anime:407038478212399114>",
         "<:XD:407028977274978344>",
         "<:glass:417241088168820737>",
         ":thinking:"]
    try:
        y = int(args)
        if y > 5:
            y = 5
    except discord.ext.commands.errors.MissingRequiredArgument:
        print('hey there')
        y = 1 
    for i in range(y):  ##@client.command(pass_context=True)
        await ctx.send(random.choice(bad))  ##async def quote(ctx):
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
    world= "https://docs.google.com/document/d/1NHoizFrN5MFiqWZKv1g7aHSiVfZbbT-NJAppnBj9e14/edit"
    em.add_field(name="World Eaters" ,value = world)
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




@client.command()  ##        x=args.split(',')
async def calc(ctx, *, args):  ##        y=""
    'Calcs a given expression, someone needs to see how far this goes tho'  ##        for i in ctx.server.members:
    try:  ##            if(i.mentioned_in(args)):
        x = eval(args)  ##                y=i
    except ZeroDivisionError :  ##        await client.send_message(y,x[0])
        x = 'Bish , you just divided by zero'  ##
    await ctx.send('Result: ' + str(x))


@client.command()
@commands.check(basic_check)
async def rproom(ctx):
    y=None
    for i in ctx.guild.categories:
        if( i.id==377792065192460289):
            y=i
    await ctx.guild.create_text_channel("room_2",category=y)
    await ctx.send("Channel created. Have fun")

@client.command()
@commands.check(basic_check)
async def deleterproom(ctx):
    y=None
    for i in ctx.guild.text_channels:
        if( i.name=="room_2"):
            y=i
    await y.delete()
    await ctx.author.send("Channel Killed!")

@client.command()
async def time(ctx):
    em=discord.Embed(title="Time")
    dt=datetime.datetime.now()
    i_time=dt+datetime.timedelta(hours=5,minutes=30)
    x_time=dt-datetime.timedelta(hours=5)    
    singa_time=dt+datetime.timedelta(hours=8)
    b_time=dt+datetime.timedelta(hours=1)
    a_time=dt+datetime.timedelta(hours=11)
    est=dt-datetime.timedelta(hours=6)

    em.add_field(name="GMT",value=dt.strftime("%T || %D"),inline=False)
    em.add_field(name="EST",value=est.strftime("%T || %D"),inline=False)
    em.add_field(name="BRITAIN",value=b_time.strftime("%T || %D"),inline=False)
    em.add_field(name="INDIA",value=i_time.strftime("%T || %D"),inline=False)
    em.add_field(name="SINGAPORE AND PHILPPINES",value=singa_time.strftime("%T || %D"),inline=False)
    em.add_field(name="AUSTRALIA",value=a_time.strftime("%T || %D"),inline=False)
    em.add_field(name="TEXAS",value=x_time.strftime("%T || %D"),inline=False)


    await ctx.send(embed=em)




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
    x.add_field(name="role",value="Syntax: !<> \nUse: Assigns the said role. use !rolename to geet the role", inline=False)
    await ctx.send(embed=x)



@client.command()
async def in_guilds(ctx):
    for i in client.guilds:
        await ctx.send(i.name)


@client.command()
@commands.check(Kami_check)
async def test(ctx):
##    await ctx.send("Input meem me")
##    x= await client.wait_for("message",timeout=60.0, check=room)
##    await ctx.send(x.content)
        for i in ctx.guild.roles:
            if( i.name=="Moderator"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("ok")

@client.command()
async def rtfm(ctx):
    await ctx.send("https://discordpy.readthedocs.org/en/rewrite")


@client.command()
@commands.check(basic_check)
async def pfp(ctx):
    x= ctx.message.mentions[0]
    em = discord.Embed(title="Old Face")
    em.set_image(url=x.avatar_url)
    await ctx.send(embed=em)

@client.command()
async def avatar(ctx):
    em = discord.Embed(title="Old Face")
    em.set_image(url=ctx.message.author.avatar_url)
    await ctx.send(embed=em)

@client.command()
@commands.check(basic_check)
async def ban(ctx):
    x= "BeGONe THOT!!!!"
    await ctx.send(x)

@client.command()
@commands.check(basic_check)
async def unban(ctx):
    x= "BeGONe THOT!!!!"
    await ctx.send("!!!!TOHT eNOGeB")

##@client.command()
##async def ask(ctx,*,args):
##    picks= ["Yes","No","Maybe","Definte Maybe"]
    
@client.command()
async def ships(ctx):
        x="""
    \nsilly mortals and thier fantasies. *throw doc* here

    \nhttps://docs.google.com/document/d/1ZRUoxHeY8bKjp0eCOvo6ilu-7O03CwTd2ikRv2iUs9I/edit
        """
        await ctx.send(x)

@client.command()
async def status(ctx):
        x="""
SO a quicke from me since i know most of you are sleeping. 
In the 11 months i've been here there have been sad times, happy times, Angry times, laughing times,

Gay times ,straight times, Meem times, Serious times, 

Times which made you Go all "FUCK THIS FUCK THAT FUCK EveRYTHING" and times which made you go "I will give you my BLOOOD"

Times when you said stuff like "KAmi YOU B" or "Everyone Agree that hope is GOd" 

All These times, i've cherished with you all

So in that Note i wanna say



WE ARE LESS THAN A MONTH TOWARDS OUR 1 YEAR ANNVERSARY. I SWEAR TO GODS IF YOU ARE NOT THERE ON THE 8TH OF NOVEMEBER i HAVE FULL LEGAL RIGHTS TO SPAM PING YOU TILL YOU ARE HERE AM I CLEAR

In other News. We are still looking for a bot __slave__. Emphasis on Slave.

If you have any cool commands Cc should have tell kami. Actually don't tell him, Pester HIm. He's a B and he's gonna be too lazy to do it

So In conclusion
我希望你的父母死亡
你的奶奶吐血
放屁
<:dab:407026257969152031>
"""
        await ctx.send(x)


    

client.run(os.environ["TOKEN"])
