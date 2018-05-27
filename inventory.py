import discord,openpyxl
from discord.ext import commands

w=openpyxl.load_workbook("Playerdata.xlsx")
pl=7
info=w["info"]
BOSS = "Kami lucky#3952"

def basic_check(ctx):
    if ctx.message.author==ctx.message.server.author or ctx.message.author==BOSS:
        return True
    else:
        return False

class MoneySystem:
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def inv(self):
        pass

    @inv.command(name="show",pass_context=True)
    async def inv_show(self,ctx,*,args=None ):
        if (args==None):
            args=str(ctx.message.author)
        args= args.lower()
##        await self.bot.say(args)
        x="Not found"
        for i in range(2,2+pl):
            if (str(info["A"+str(i)].value).lower()==args):
                x="````\nOwner : " + str(info["A"+str(i)].value) + "\n\n"
                for j in range(ord('B'),ord('Z')+1):
                    cat= str(info[chr(j)+str(1)].value)
                    data=str(info[chr(j)+str(i)].value)
                    if(data == "False"):
                        break
                    elif(data=="True"):
                        x+="\n\n"
                        continue
                    x+=cat + " : " + data +" \n"
                x+="\n```"
                break
        await self.bot.say(x)
        
##    @inv.check(basic_check)
##    @inv.command(name="add item", pass_context=True)
##    async def inv_addItem(self, ctx, args=None):
##        if args == None:
##            await self.bot.say("command syntax: !/?/yuno inv add item <item info>")
##            
##        
        

def setup(bot):
    bot.add_cog(MoneySystem(bot))
