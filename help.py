import discord
from discord.ext import commands
import json
import aiohttp

class Helpe(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(name="help" , invoke_without_command=True)
    async def help(self,ctx):
        x= discord.Embed(title= "Help Subcommands")
        x.add_field(name="Utility",value="For your Rp , or just general life needs use !help utility", inline=False)
        x.add_field(name="Magic",value="For your Magic the gathering needs, use !help magic", inline=False)
        x.add_field(name="Image",value="For your cuteness needs, use !help img", inline=False)
        x.add_field(name="Meme",value="For some SUPER SECRET COMMANDS use !help meme", inline=False)
        await ctx.send(embed=x)

    
    @help.command(name="utility")
    async def utility(self,ctx):
        x= discord.Embed(title= "Utility")
        x.add_field(name="Roll",value="To roll x di(c)e of y sides use !roll xdy", inline=False)
        x.add_field(name="Pick",value="To pick from a set options use !pick a,b,c", inline=False)
        x.add_field(name="Calc",value="To calculate an equation use !calc 1+2*3/4-5", inline=False)
        x.add_field(name="Roles",value="For your cuteness needs, use !help img", inline=False)
        await ctx.send(embed=x)

##    @help.command(name="magic")
##    async def (self,ctx):
##        x= discord.Embed(title= "GAMER")
##        x.add_field(name="card",value="To roll x di(c)e of y sides use !roll xdy", inline=False)
##        x.add_field(name="Pick",value="To pick from a set options use !pick a,b,c", inline=False)
##        x.add_field(name="Calc",value="To calculate an equation use !calc 1+2*3/4-5", inline=False)
##        x.add_field(name="Roles",value="For your cuteness needs, use !help img", inline=False)
##        await ctx.send(embed=x)


    
def setup(bot):
    bot.add_cog(Helpe(bot))
