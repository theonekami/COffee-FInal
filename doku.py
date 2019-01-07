import discord
from discord.ext import commands
import json
import aiohttp
import sudotest

class Sudoku:
    def __init__(self, bot):
        self.bot=bot
        self.running=False

    @commands.group()
    async def doku(self,ctx):
        pass

    def write(self):
        y="```"
        u=0
        v=0
        r=65
        y+="________________________\n"
        y+="    "+chr(r) + "     " + chr(r+1) + "     " +chr(r+2)+"\n"
        y+="________________________\n"
        r=r+3
        for i in self.boardlist[0]:
            for j in i:
                y+=str(j)+" "
                u=u+1
                if(u==3):
                    y+="| "
                    u=0
            y+="\n"
            v=v+1
            if (v==3):
                v=0
                y+="________________________\n"
                y+="    "+chr(r) + "     " + chr(r+1) + "     " +chr(r+2)+"\n"
                y+="________________________"
                r=r+3              
        y+="```"
        return y

    
    @doku.command(name="start")
    async def doku_start(self,ctx):
        if(not (self.running)):
            self.running=True
        else:
            await ctx.send("Sorry, a game is already running")
            return
        self.boardlist=sudotest.set_board()
        self.board_img=self.boardlist[0]
        await ctx.send(self.write())

    @doku.command(name="show")
    async def doku_show(self,ctx):
        if(self.running):
            await ctx.send(self.write())
        else:
            await ctx.send("Sorry, no game is running.")

    @doku.command(name="sudoku")
    async def doku_end(self,ctx):
        if(self.running):
            await ctx.send("Comiited Sudoku")
            self.running=False
        else:
            await ctx.send("Sorry, no game is running.")

    
        
#[":arrow_upper_left::one::two::three:\n"],
#[":one:",self.blank,self.blank,self.blank,"\n"],
#[":two:",self.blank,self.blank,self.blank,"\n"],
#[":three:",self.blank,self.blank,self.blank,"\n"]

def setup(bot):
    bot.add_cog(Sudoku(bot)) 
