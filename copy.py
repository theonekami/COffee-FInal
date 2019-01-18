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


class Copypasta:
    def __init__(self, bot):
        self.bot=bot
        self.seal="""What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo"""
        self.mia= """`:head_bandage:Hit :punch: or miss:flushed: I guess :thinking:they :point_right:never :x: miss, huh :confused::confused:? You :raised_hands:got a boyfriend:heart_eyes:, I bet :slot_machine::no_mouth:he :fearful:doesn't :thumbsdown:kiss :kissing_heart::kissing_heart: y mwah:sparkling_heart: :heart_eyes_cat:He gon' find :mag::mag: another girl :baby: and he :open_mouth:won't:triumph: miss:ok_hand: ya:scream_cat: He :drooling_face:gon' :astonished:skrrt and hit :punch::punch: the dab:sunglasses: like :smile::smile: Wiz :cowboy:Khalifa:money_mouth:"""
        self.shake="""To hit, or not to hit. Dost thou ever miss? I suppose it not. You have a male love interest, yet I would wager he does not kiss thee (Ye olde mwah). Furthermore; he will find another lass like he won't miss thee. And at the end of it all. He is going to skrrt, and he will hit that dab, as if he were the man known by the name of Wiz Khalifa"""
        self.yeet="""To yeet, or not to yeet--that is the question:\nWhether 'tis danker in the mind to yeet\nThe slings and arrows of dank fortune\nOr to yeet arms against a sea of troubles\nAnd by yeeting end them. To yeet, to yeet--\nNo more--and by a sleep to say we yeet\nThe heartache, and the thousand dank shocks\nThat flesh yeets heir to. 'Tis a consummation\nDevoutly to yeet yeeted. To yeet, to yeet--\nTo yeet--perchance to yeet: ay, there’s the rub,\nFor in that sleep of death what dreams may yeet\nWhen we have yeeted off this dank coil,\nMust yeet us pause. There yeets the respect\nThat yeets calamity of so dank life.\nFor who would yeet the whips and scorns of time,\nTh' oppressor yeets wrong, the dank man's contumely\nThe pangs of dank love, the law's delay,\nThe insolence of office, and the spurns\nThat dank merit of th' dank takes,\nWhen he himself might his quietus yeet\nWith a dank bodkin? Who would fardels yeet,\nTo yeet and yeet under a dank life,\nBut that the dread of something after death,\nThe dank country, from whose bourn\nNo traveller yeets, yeets the will,\nAnd makes us rather yeet those ills we yeet\nThan yeet to others that we yeet not of?\nThus conscience does yeet cowards of us all,\nAnd thus the dank hue of resolution\nIs yeeted o'er with the dank cast of thought,\nAnd enterprise of dank pitch and moment\nWith this regard their currents yeet dank\nAnd yeet the name of action. -- Soft you now,\nThe dank Ophelia! -- Nymph, in thy orisons\nYeet all my sins yeeted."""
        self.america="""Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. "What the devil?" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, "Tally ho lads" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended."""
    

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
    bot.add_cog(Copypasta(bot))
