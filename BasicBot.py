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
import inspect

bot_admin_discriminators = [256390874848690176,131205596732063744] # These users have access to the bot's admin functions on all servers

ch_id=377790510582071299

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
    p=ctx.author
    for i in p.roles:
        if i.name=="Moderator":
            return True
    if (p == ctx.guild.owner) or (p.id == 256390874848690176):
        return True
    else:
        return False





client=commands.Bot( command_prefix=('?', '!','.', 'cc ', 'Cc ','CC ', 'Coffee ','Coffee Cat '),description='Alright a little something i did for both expertimentaion and Hapiness. This is Yuno')
client.remove_command('help')


@client.event
async def on_ready():
    print('You are running BasicBot v2.1')
    print('Created by Kaminolucky')
    client.load_extension("Role_command")
    client.load_extension("Magic")
    client.load_extension("Net_command")
    client.load_extension("Sl_command")
    client.load_extension("sentience")
    client.load_extension("test")
    client.load_extension("Cool_Point")
    client.load_extension("help")
    
    home=client.get_channel(id=522127036022521871)

    await home.send("I am REBORN")

    return await client.change_presence(activity=discord.Game(name='Am i Pretty yet?'))


@client.event
async def on_member_join(member):
    x = client.get_channel(id=570139651138912287)
    y="Hello" + member.mention+"I am Coffee Cat and it’s a pleasure to meet you. Welcome to this relaxed community server. Please read #rules-faq to get started and use !help for my commands."
    em = discord.Embed(title="New Face")
    em.set_image(url=member.avatar_url)
    if member.bot:
        return
    await x.send(y)
    await x.send(embed=em)


@client.event
async def on_raw_reaction_add(payload):
    if not(payload.message_id==753932030668046377):
        return
    if payload.member.bot:
        return
    t=client.get_guild(ch_id)
    z=t.get_channel(753742549574746113)
    e=payload.member
    y=await z.fetch_message(id=753932030668046377)
    r=None
    s=None
    if payload.emoji.id==753755414310420489: #mtg
        r=643733493968535552
        s="MTG"
    elif payload.emoji.id==670157311217762324:
        r=694695508576436334
        s="Event"
    elif payload.emoji.id==754390023750811670:
        r=682600245619982366
        s="DND"
    elif payload.emoji.id==754393996440371211:
        r=643743977727721495
        s="POkemon"
    elif payload.emoji.id==754395260192555068:
        r=643733562134102026
        s="Writer"

    
    else:
        await y.remove_reaction(payload.emoji,e)
        print("n")

    if r and s:
        await e.add_roles(t.get_role(r))
        await e.send("Given the "+s+" role")
        #bad idea
        print("y")

@client.event
async def on_raw_reaction_remove(payload):
    if not(payload.message_id==753932030668046377):
        return
    t=client.get_guild(ch_id)
    z=t.get_channel(753742549574746113)
    e=t.get_member(payload.user_id)
    y=await z.fetch_message(753932030668046377)
    r=None
    s=None
    
    if payload.emoji.id==753755414310420489: #mtg
        r=643733493968535552
        s="MTG"
    elif payload.emoji.id==670157311217762324:
        r=694695508576436334
        s="Event"
    elif payload.emoji.id==754390023750811670:
        r=682600245619982366
        s="DND"
    elif payload.emoji.id==754393996440371211:
        r=643743977727721495
        s="Pokemon"
    elif payload.emoji.id==754395260192555068:
        r=643733562134102026
        s="Writer"
    
    if r and s:
        await e.remove_roles(t.get_role(r))
        await e.send("Removed the "+s+" role")
        #bad idea
        print("y")


@client.command()
@commands.check(Kami_check)
async def roleload(ctx):
    z=client.get_channel(id=753742549574746113)
    y= await z.fetch_message_fast(753932030668046377)
    r="""For getting the MTG role react with <:mtg:753755414310420489>

For getting the EVENT role react with <:dice:670157311217762324>

For getting the DND  role react with <:dnd:754390023750811670>

For getting the Pokemon role react with <:poke:754393996440371211>

For getting the Writer role react with <:pen:754395260192555068>"""
    await y.edit(content=r)
    await y.add_reaction("<:mtg:753755414310420489>")
    await y.add_reaction("<:dice:670157311217762324>")
    await y.add_reaction("<:dnd:754390023750811670>")
    await y.add_reaction("<:poke:754393996440371211>")
    await y.add_reaction("<:pen:754395260192555068>")
    await ctx.send("Roles updated")
    print("k")
            
@client.command()
async def hi(ctx):
    await ctx.send("New pic new me. Credit to rei, and the gremlin i almost ate")

@client.command()
async def pick(ctx, *, args):
    'A pick device. Uses a list so i think any number of arguments can work'
    y = str(args)
    x = random.choice(y.split(','))
    await ctx.send('Umm..I Picked: ' + x)

@client.command()
async def roles(ctx):
    x= discord.Embed(title= "Role List")
    x.add_field(name="Roleplays",value="!rps - lets you view all documents for current hosted RP's", inline=False)
    x.add_field(name="Gamenight",value="!gamenight - be notified when people run party games", inline=False)
    x.add_field(name="Health and Fitness",value="!hnf If your hobbies include health and fitness, assign this role for discussions in the relevant room.", inline=False)
    x.add_field(name="Gaming Roles",value="!lol, !mtg and !pokemon assign the roles specific to those games.", inline=False)
    x.add_field(name="Writing",value="!writing - be notified of writing discussions and workshops.", inline=False)
    await ctx.send(embed=x)

@client.command()
async def rps(ctx):
    x= discord.Embed(title= "Role List")
    x.add_field(name="Cryosis",value="!cry, !pmd: A post apocalyptic Pokemon Mystery Dungeon styled RP with grimdark elements.", inline=False)
    x.add_field(name="Heroes of legend",value="!hol,!reader: A world in turmoil, you join a rag tag group of people who try to fix it", inline=False)
    await ctx.send(embed=x)

    
@client.command()
async def roll(ctx, *, args):
    'Rolls a dice. Formatted as  <no of dice>d<no of sides> eg. 3d10'
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

def roll_single(msg):
	dice = msg.split("d")

	# checking for d usage
	if len(dice) > 2:
		return "Illegal dice roll, the 'd' term has been used improperly."

	# checking for correct numbers
	try:
		nums_dice = [int(elem) for elem in dice]
	except Exception:
		return "Illegal dice roll, the numbers used are invalid."

	# checking for static number
	if len(nums_dice) == 1:
		return nums_dice[0], nums_dice

	curr_sum, all_rolls = 0, []
	for _ in range(nums_dice[0]):
		rolled_dice = randint(1, nums_dice[1])
		curr_sum += rolled_dice
		all_rolls.append(rolled_dice)

	return curr_sum, all_rolls

@client.command()
async def rollm(ctx, *, args):
    details = [elem.strip() for elem in args.split("+")]
    total_res, all_dice = 0, []
    for dice in details:
        curr_details = roll_single(dice)
        total_res += curr_details[0]
        all_dice.append(curr_details[1])
    await ctx.send(total_res, all_dice)


@client.command()
async def ask(ctx, *,args=None):
    if(args==None):
        await ctx.send("The answer is. FUCK you for not asking a question.")
        await ctx.send("Was that rude?")
        return
    args=args.lower()
    x=""
    if ("kms" in args or "kill" in args):
        x+="Killing is bad, yet... "
    y=["Sure",
       "It checks out",
       "Without a doubt",
       "Yes - definitely",
       "T R U S T",
       "i can't see the future, but it's a yes",
       "probabilty says..something, But you should TAKE THE CHANCE" ,
       "Looks fair",
       "Yes.",
       "Sure.",
       "I'd rather not answer it.",
       "Ask again later.",
       "Better not tell you now.",
       "Cannot predict now.",
       "50/50...wait no 49/51",
       "50/50...wait no 51/49",
       "No",
       "Why tf?",
       "I wouldn't do that",
       "I have run many calcs, they all say no....So..."]
    x+= random.choice(y)
    await ctx.send(x)



@client.command()
async def dab(ctx, *, args='1'):
    y = int(args)
    t=0
    if y > 14 and not(basic_check(ctx)):
        y = 14
    dab=["<:dab:407026257969152031>","<:pandab:524980250170490892>"]
    for i in range(y):
        await ctx.send(dab[t])
        t=not(t)
        await asyncio.sleep(0.5)

@client.command() 
async def calc(ctx, *, args):  
    'Calcs a given expression, someone needs to see how far this goes tho'
    try:            
        x = eval(args) 
    except ZeroDivisionError :  
        x = 'Bish , you just divided by zero'  
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


###
### TIME COMMAND> MAKE IT...LOGICAL.. E W W W WITS UGLY I NEED HELP
###

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
    utc=dt-datetime.timedelta(hours=8)

    em.add_field(name="GMT",value=dt.strftime("%T || %D"),inline=False)
    em.add_field(name="EST",value=est.strftime("%T || %D"),inline=False)
    em.add_field(name="BRITAIN",value=b_time.strftime("%T || %D"),inline=False)
    em.add_field(name="INDIA",value=i_time.strftime("%T || %D"),inline=False)
    em.add_field(name="SINGAPORE AND PHILIPPINES",value=singa_time.strftime("%T || %D"),inline=False)
    em.add_field(name="AUSTRALIA",value=a_time.strftime("%T || %D"),inline=False)
    em.add_field(name="TEXAS",value=x_time.strftime("%T || %D"),inline=False)
    em.add_field(name="PST",value=utc.strftime("%T || %D"),inline=False)

    await ctx.send(embed=em)

##
## WHAT IS THIS TRASH HELP
## R E E E E
##





@client.command()
async def in_guilds(ctx):
    for i in client.guilds:
        await ctx.send(i.name)





@client.command()
@commands.check(Kami_check)
async def test(ctx):
    for i in client.guilds:
        await ctx.send(i.name)
    await ctx.send("Leaving"+ str(client.guilds[3].name))
    await client.guilds[3].leave()
    
  # y=await z.send("For getting to magic react with <:mtg:753755414310420489>")

    

    
    
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
##    for i in ctx.message.mentions:
##        await ctx.guild.ban(i)
    await ctx.send(x)

@client.command()
async def timer(ctx, *, args):
    await ctx.send("Setting timer for " + str(args)+ " min(s)")
    if( not (args.isnumeric())):
        await ctx.send("Stfu and put an actual number u skrub")
        return
    await asyncio.sleep(float(args)*60)
    await ctx.send("Timer over"+ ctx.message.author.mention) 

@client.command()
async def reminder(ctx, *, args):
    args=args.split(',')
    x=args[1]
    await ctx.send("Setting timer for " + str(args[0])+ " min(s) to remind you of '" + x + "'")
    if( not (args[0].isnumeric())):
        await ctx.send("Stfu and put an actual number u skrub")
        return
    await asyncio.sleep(float(args[0])*60)
    await ctx.send("Timer over"+ ctx.message.author.mention + "\n" + x) 



@client.command()
async def cc(ctx, *, args):
    x="on the wall"
    a="alpha"
    args=args.lower()
    if(x in args and a in args):
        await ctx.send("Hope is most alpha of them all")
        await ctx.send("https://cdn.discordapp.com/attachments/404266499516268554/561082612819558400/image0.jpg")

    


@client.command()
async def alpha(ctx):
    await ctx.send("Hope is most alpha of them all")
    await ctx.send("https://cdn.discordapp.com/attachments/404266499516268554/561082612819558400/image0.jpg")

@client.command()
async def god(ctx):
    await ctx.send("Llama is our actual god")



@client.command()
async def git(ctx):
    await ctx.send("https://github.com/theonekami/COffee-FInal")

@client.command()
@commands.check(basic_check)
async def rickroll(ctx):
    await ctx.message.mentions[0].send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    await ctx.message.delete()

@client.command()
async def cog(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/377790511353692162/646215280967680020/maxresdefault.png")

@client.command()
async def jean(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/377790511353692162/641145071357657129/wack_funeral_1.gif")


@client.command()
async def kami(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/377790511353692162/646219857645273098/image0.jpg")



@client.command()
async def age(ctx):
    x= ctx.guild.created_at
    y= datetime.datetime.now()
    z=y-x
    s= "This server was created at " + x.strftime(("%d %m %y")) + "\nThat makes the age " +str(int(str(z.days))-365) + " days"
    await ctx.send(s)

@client.command()
async def react(ctx):
    s="https://cdn.discordapp.com/attachments/377790511353692162/611193675690541086/20190814_083856.jpg\n"
    t="https://cdn.discordapp.com/attachments/377790511353692162/611193675690541090/20190814_083828.jpg\n"
    u="https://cdn.discordapp.com/attachments/377790511353692162/611193676286394368/20190814_083841.jpg"
    await ctx.send(s)
    await asyncio.sleep(0.5)
    await ctx.send(t)
    await asyncio.sleep(0.5)
    await ctx.send(u)
 
@client.command()
@commands.check(basic_check)
async def exec(ctx,*,args):
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = await asyncpg.connect(DATABASE_URL)
    x= await conn.fetch(args)
    await ctx.send(x)
    await conn.close()

    
client.run(os.environ["TOKEN"])



##################################################################################
##                                              NO ENTRY BEYOND THIS POINT
################################################################################

    
##@client.command()
##async def ships(ctx):
##        x="""
##    \nsilly mortals and thier fantasies. *throw doc* here
##
##    \nhttps://docs.google.com/document/d/1ZRUoxHeY8bKjp0eCOvo6ilu-7O03CwTd2ikRv2iUs9I/edit
##        """
##        await ctx.send(x)

##@client.command()
##async def age(ctx):
##    x= ctx.guild.created_at
##    y= datetime.datetime.now()
##    z=y-x
##    s= "This server was created at " + x.strftime(("%d %m %y")) + "\nThat makes the age " +str(z.days) + " days"
##    await ctx.send(s)


    
##@client.command()
##async def Exit(ctx):
##    await ctx.guild.leave()

