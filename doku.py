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
    async def doku(ctx):
        pass

    @doku.command(name="start")
    async def doku_start(ctx):
        if(not (self.running)):
            self.running=True
        else:
            ctx.send("Sorry, a game is already running")
            return
        self.boardlist=sudotest.set_board()
        self.board_img=
        """```
 ____________________
   A       B      C
 ____________________
 1 1 1 | 2 2 2 | 3 3 3
 1 1 1 | 2 2 2 | 3 3 3
 1 1 1 | 2 2 2 | 3 3 3
 ____________________
   D      E       F
 ____________________
 1 1 1 | 2 2 2 | 3 3 3
 1 1 1 | 2 2 2 | 3 3 3
 1 1 1 | 2 2 2 | 3 3 3
 ____________________
   G      H       I
 ____________________
 1 1 1 | 2 2 2 | 3 3 3
 1 1 1 | 2 2 2 | 3 3 3
 1 1 1 | 2 2 2 | 3 3 3
```"""
        ctx.send(self.board_img)

        
#[":arrow_upper_left::one::two::three:\n"],
#[":one:",self.blank,self.blank,self.blank,"\n"],
#[":two:",self.blank,self.blank,self.blank,"\n"],
#[":three:",self.blank,self.blank,self.blank,"\n"]

def setup(bot):
    bot.add_cog(Sudoku(bot)) 
