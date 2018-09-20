import discord
from discord.ext import commands
import json
import aiohttp
import discord
from discord.ext import commands
import json
import aiohttp

import motor.motor_asyncio as amotor
import asyncio
class coolDb:
    def __init__(self):
        self.client=amotor.AsyncIOMotorClient("mongodb+srv://KaminoLucky:Ayikudi@cluster0-qxzeb.mongodb.net/test?retryWrites=true") #insert your own link here
        self.db=self.client['COOLPOINTS']
        self.collections=[]
        self.collection=""
    async def add_collection(self,name:str):
        print("Collection Added")
        self.collections+=[name]
        self.collection=name
        if name not in (await self.db.list_collection_names()):
            await self.db.create_collection(name=name)
    async def remove_collection(self,name:str):
        self.collections.remove(name)
        await self.db.drop_collection(name)
    def set_collection(self,name:str):
        self.collection=name
    async def insert(self,**kwargs):
        print("inserted")
        await self.db[self.collection].insert_one(kwargs)
    async def insert_many(self,*items):
        for i in items:
            await self.insert(**i)
    async def delete(self,**kwargs):
        await self.db[self.collection].delete_many(kwargs)
    async def find(self,length=1000,**kwargs):
        cursor=self.db[self.collection].find(kwargs)
        res=[]
        for doc in await cursor.to_list(length=length):
            doc.setdefault("")
            res.append(doc)
        return cursor
    async def print_db(self):
        res=[]
        for i in (await self.find()):
            temp=[]
            for x in i.keys():
                if i!="_id":
                    temp+=[x+":"+str(i[x])]
            res+=[",".join(temp)]
        return "\n".join(res)
