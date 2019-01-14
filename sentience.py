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


class Sentience:
    def __init__(self, bot):
        self.bot=bot
        self.praise=["You are cute",
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
        self.seal="""What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo"""
        self.mia= """`:head_bandage:Hit :punch: or miss:flushed: I guess :thinking:they :point_right:never :x: miss, huh :confused::confused:? You :raised_hands:got a boyfriend:heart_eyes:, I bet :slot_machine::no_mouth:he :fearful:doesn't :thumbsdown:kiss :kissing_heart::kissing_heart: y mwah:sparkling_heart: :heart_eyes_cat:He gon' find :mag::mag: another girl :baby: and he :open_mouth:won't:triumph: miss:ok_hand: ya:scream_cat: He :drooling_face:gon' :astonished:skrrt and hit :punch::punch: the dab:sunglasses: like :smile::smile: Wiz :cowboy:Khalifa:money_mouth:"""
        self.shake="""To hit, or not to hit. Dost thou ever miss? I suppose it not. You have a male love interest, yet I would wager he does not kiss thee (Ye olde mwah). Furthermore; he will find another lass like he won't miss thee. And at the end of it all. He is going to skrrt, and he will hit that dab, as if he were the man known by the name of Wiz Khalifa"""
        self.yeet="""To yeet, or not to yeet--that is the question:
Whether 'tis danker in the mind to yeet
The slings and arrows of dank fortune
Or to yeet arms against a sea of troubles
And by yeeting end them. To yeet, to yeet--
No more--and by a sleep to say we yeet
The heartache, and the thousand dank shocks
That flesh yeets heir to. 'Tis a consummation
Devoutly to yeet yeeted. To yeet, to yeet--
To yeet--perchance to yeet: ay, there’s the rub,
For in that sleep of death what dreams may yeet
When we have yeeted off this dank coil,
Must yeet us pause. There yeets the respect
That yeets calamity of so dank life.
For who would yeet the whips and scorns of time,
Th' oppressor yeets wrong, the dank man's contumely
The pangs of dank love, the law's delay,
The insolence of office, and the spurns
That dank merit of th' dank takes,
When he himself might his quietus yeet
With a dank bodkin? Who would fardels yeet,
To yeet and yeet under a dank life,
But that the dread of something after death,
The dank country, from whose bourn
No traveller yeets, yeets the will,
And makes us rather yeet those ills we yeet
Than yeet to others that we yeet not of?
Thus conscience does yeet cowards of us all,
And thus the dank hue of resolution
Is yeeted o'er with the dank cast of thought,
And enterprise of dank pitch and moment
With this regard their currents yeet dank
And yeet the name of action. -- Soft you now,
The dank Ophelia! -- Nymph, in thy orisons
Yeet all my sins yeeted."""

        self.america="""Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. "What the devil?" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, "Tally ho lads" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended."""
    
    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.user)
    async def roast(self,ctx):
        for i in ctx.message.mentions:
            await i.send(random.choice(self.insults))
        await ctx.send(":fire:")

    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.user)
    async def cheer(self,ctx):
        for i in ctx.message.mentions:
            await i.send(random.choice(self.praise))
        await ctx.send("I have praised them")

    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.guild)
    async def mia(self,ctx):
        await ctx.send(self.mia)

        
    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.guild)
    async def shakespeare(self,ctx):
        await ctx.send(self.shake)

    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.guild)
    async def yeet(self,ctx):
        await ctx.send(self.yeet)

    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.guild)
    async def america(self,ctx):
        await ctx.send(self.america)
    

    @commands.command()
    @commands.cooldown(rate=1,per=2,type=commands.BucketType.guild)
    async def navy(self,ctx):
        await ctx.send(self.seal)
        
        
def setup(bot):
    bot.add_cog(Sentience(bot))
