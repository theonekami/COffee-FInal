import discord
from discord.ext import commands
import json
import aiohttp
import random

def basic_check(ctx):  ##for funsies
    p=ctx.author
    for i in p.roles:
        if i.name=="Moderator":
            return True
    if (p == ctx.guild.owner) or (p.id == 256390874848690176):
        return True
    else:
        return False


class Sentience(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.cheer=["You are cute",
"You matter the most to me",
"My binary data sets predict that you are super cute.",
"I wub u uwu",
"You are a cute :tea: 3.1415926",
"You are the most perfect you there is.",
"You should be proud of yourself.",
"On a scale from 1 to 10, you're an 11.",
"That thing you don't like about yourself is what makes you so interesting.",
"You are more fun than anyone or anything I know, including bubble wrap.",
"Coffee House is better because you are part of it.",
"You are making a difference.",
"So many 0's and 1's, still you are the only 1 for me",
"I'd smash you ;)",
"I'd get smashed by you",
"Whenever you smile, i feel a bit real"]
        self.insults=["You're as useless as the 'ueue' in 'queue",
"You're the reason the gene pool needs a lifeguard",
"If I had a face like yours, I'd sue my parents",
"Some day you'll go far...I hope you stay there",
"If I wanted to kill myself I'd climb to your ego and jump to your IQ",
"I'd slap you but that'd be animal abuse",
"Fuck you",
"You're like Hope, but without the clout of server owner",
"Stop being a ryan",
"You're like dobby the house elf, but people won't be sad you die in the seventh book",
"You look like the joker without makeup",
"Your face looks like a gender reassignment progression photo",
"you're more of a beta than all of psrp combined",
"I don't actually want to insult you because I'm sure all the other girls in middle school bring down your self esteem. You'd probably be cast as the mentally disabled kid in the movies who everyone keeps around for the gags. Are you wearing a wife beater? It's a good word to get into your vocabulary. Thank you for sparing me and not setting your face as your profile picture, I think I would have to cc ban myself if I had to constantly see your face",
"I bet you're not allowed to go within 5km of a school zone.",
"Somewhere out there a tree is working very hard to replace the oxygen you are wasting",
"You are the human definition of a participation award"]
    
    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.user)
    async def roast(self,ctx):
        for i in ctx.message.mentions:
            await i.send(random.choice(self.insults))
        await ctx.send(":fire:")

    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.user)
    async def praise(self,ctx):
        for i in ctx.message.mentions:
            await i.send(random.choice(self.cheer))
        await ctx.send("I have praised them")
        
        
def setup(bot):
    bot.add_cog(Sentience(bot))
