
import discord
from discord.ext import commands
import json
import aiohttp

import os

#items
#users

##class Item:
##    def __init__(self,name):
##        self.Name=name
##        self.
##Description
##Price
##Shop Presence
##        

code_dict = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 



class Converter(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def morse(self, ctx,*,args):
        msg=args
        msg=msg.upper()
        parse=[]
        await ctx.send("- == <:pandab:524980250170490892>\n . == <:dab:407026257969152031>")
        for i in msg:
            parse.append(i)
        x=""
        for i in parse:
            if i == ' ':
                x+=' '
                continue 
            for j in code_dict[i]:
                if j==".":
                    x+="<:dab:407026257969152031>"
                elif j=="-":
                    x+="<:pandab:524980250170490892>"
                else:
                    x+=j
        await ctx.send(x)

##    @commands,command()
##    async def search(self, ctx,args):
##        x="https://www.google.co.in/search?q="+str(args)+"&rlz=1C1CHBF_enIN799IN799&oq=meems&aqs=chrome..69i57j0l5.806j0j7&sourceid=chrome&ie=UTF-8"
##        
        
        
def setup(bot):
    bot.add_cog(Converter(bot))
