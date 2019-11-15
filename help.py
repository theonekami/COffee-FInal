import discord
from discord.ext import commands
import json
import aiohttp

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(name="help" , invoke_without_command=True)
    async def help(self,ctx):
        x= discord.Embed(title= "Help Subcommands")
        x.add_field(name="Utility",value="For your Rp , or just general life needs use !help utility", inline=False)
        x.add_field(name="Gaming",value="Syntax: !hi \nUse: To test if the bot is on or not", inline=False)
        x.add_field(name="Magic",value="Syntax: !pick choice a, choice b....,choice n \nUse: To pick out of the given choices", inline=False)
        x.add_field(name="Picture",value="Syntax: !roll <no of dice>d<no of sides> \nUse: To roll dice. \nEg !roll 1d20", inline=False)
        x.add_field(name="Copypasta",value="Syntax: !dab \nUse: GUESS YOU BLOODY BISHES", inline=False)
        await ctx.send(embed=x)
    

    
def setup(bot):
    bot.add_cog(Help(bot))
