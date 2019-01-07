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

    @doku.command(name="start")
    async def doku_start(self,ctx):
        if(not (self.running)):
            self.running=True
        else:
            await ctx.send("Sorry, a game is already running")
            return
        self.boardlist=sudotest.set_board()
        y="```"
        u=0
        v=0
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
                y+="____________________\n\n"
                y+="____________________\n\n"
                
        y+="```"
        self.board_img=self.boardlist[0]
        
##        self.board_img="""```
## ____________________
##   A       B      C
## ____________________
## 1 1 1 | 2 2 2 | 3 3 3
## 1 1 1 | 2 2 2 | 3 3 3
## 1 1 1 | 2 2 2 | 3 3 3
## ____________________
##   D      E       F
## ____________________
## 1 1 1 | 2 2 2 | 3 3 3
## 1 1 1 | 2 2 2 | 3 3 3
## 1 1 1 | 2 2 2 | 3 3 3
## ____________________
##   G      H       I
## ____________________
## 1 1 1 | 2 2 2 | 3 3 3
## 1 1 1 | 2 2 2 | 3 3 3
## 1 1 1 | 2 2 2 | 3 3 3
##```"""
        await ctx.send(y)

        
#[":arrow_upper_left::one::two::three:\n"],
#[":one:",self.blank,self.blank,self.blank,"\n"],
#[":two:",self.blank,self.blank,self.blank,"\n"],
#[":three:",self.blank,self.blank,self.blank,"\n"]

def setup(bot):
    bot.add_cog(Sudoku(bot)) 
