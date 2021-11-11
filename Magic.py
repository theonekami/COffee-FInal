import discord
from discord.ext import commands
import json
import aiohttp
import random

import difflib
import xml.etree.ElementTree as ET

file_lst = ["BER", "02.WOT", "BP1", "BP2", "BP3", "COG", "DOC", "FUR", "KAY", "MAD", "SET", "SVP", "TRI"]

# full name dict
card_dict = {}

# word pair dict
card_dict_pair = {}

# one word dict
card_dict_split = {}
 

def parse_xml(xml_file_name):
	tree = ET.parse(xml_file_name + ".xml")
	root, curr_index = tree.getroot(), 0
	while True:
		try:
			card_name_real = root[1][curr_index][0].text
			card_name = card_name_real.lower()
			card_name.replace(',', '')
			card_link = [card_name_real, root[1][curr_index][1].attrib['picURL']]
			card_dict[card_name] = card_link

			card_words = card_name.split()
			if len(card_words) > 1:
				card_pairs = [card_words[i] + " " + card_words[i + 1] for i in range(len(card_words) - 1)]
			else:
				card_pairs = card_words

			for word in card_words:
				if word not in card_dict_split:
					card_dict_split[word] = [card_link]
				else:
					if card_link not in card_dict_split[word]:
						card_dict_split[word].append(card_link)

			for pair in card_pairs:
				if pair not in card_dict_pair:
					card_dict_pair[pair] = [card_link]
				else:
					if card_link not in card_dict_pair[pair]:
						card_dict_pair[pair].append(card_link)


		except Exception as e:
			break
		curr_index += 1
	return

for file in file_lst:
	print(file)
	parse_xml(file)

def return_image(user_string):
	all_links_s, all_links, single = [], [], []

	try:
		all_links_s = card_dict_split[difflib.get_close_matches(user_string, card_dict_split.keys())[0]]
	except Exception:
		print()
	if len(all_links_s) == 1:
		return all_links_s[0]
	else:
		print("Single-word match failed - too ambiguous.")
		try:
			all_links = card_dict_pair[difflib.get_close_matches(user_string, card_dict_pair.keys())[0]]
		except Exception:
			print()
		if len(all_links) == 1:
			return all_links[0]
		else:
			print("Pair-word match failed - too ambiguous.")
			single = [card_dict[x] for x in difflib.get_close_matches(user_string, card_dict.keys())]
			try:
				return card_dict[difflib.get_close_matches(user_string, card_dict.keys())[0]]
			except Exception:
				print()
				print("No matches. Please try again!")

	print()

	to_suggest = []
	print("Did you mean: ")
	if len(all_links_s) <= 3:
		for elem in all_links_s:
			name = elem[0]
			if name not in to_suggest:
				to_suggest.append(name)
				print(name)

	if len(all_links) <= 3:
		for elem in all_links:
			name = elem[0]
			if name not in to_suggest:
				to_suggest.append(name)
				print(name)

	if len(single) <= 3:
		for elem in single:
			name = elem[0]
			if name not in to_suggest:
				to_suggest.append(name)
				print(name)



class Magic(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def card(self,ctx,*,args):
        x=str(args)
        x=x.replace(" ","%20")      
        y=None
        z='https://api.magicthegathering.io/v1/cards?name="'+x+'"'
        print(z)
        async with aiohttp.request("get","https://api.scryfall.com/cards/named?fuzzy="+x) as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        if(y['object']=="card"):
            em = discord.Embed(title=y['name'])
            if "card_faces" in y.keys() and not("image_uris" in y.keys()):
                for i in y["card_faces"]:
                    em.set_image(url=i["image_uris"]['border_crop'])
                    await ctx.send(embed= em)
            else:
                em.set_image(url=y["image_uris"]['border_crop'])
                await ctx.send(embed= em)
        elif(y['object']=="error"):
            await ctx.send(y["details"])
        print("done")

    @commands.command()
    async def custom(self,ctx,*,args):
        y=return_image(args)
        await ctx.send(y)
    
    
    @commands.group()
    async def mg(self,ctx):
        pass

    @mg.command(name="commander")
    async def magic_commn(self,ctx):
        async with aiohttp.request("get","https://api.scryfall.com/cards/random?q=is%3Acommander") as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        if(y['object']=="card"):
            em = discord.Embed(title=y['name'])
            if "card_faces" in y.keys():
                for i in y["card_faces"]:
                    em.set_image(url=i["image_uris"]['border_crop'])
                    await ctx.send(embed= em)
            else:
                em.set_image(url=y["image_uris"]['border_crop'])
                await ctx.send(embed= em)
        elif(y['object']=="error"):
            await ctx.send(y["details"])

    @mg.command(name="art")
    async def magic_art(self ,ctx, *,args):
        x=str(args)
        x=x.replace(" ","%20")      
        y=None
        z='https://api.magicthegathering.io/v1/cards?name="'+x+'"'
        print(z)
        async with aiohttp.request("get","https://api.scryfall.com/cards/named?fuzzy="+x) as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        if(y['object']=="card"):
            em = discord.Embed(title=y['name'])
            if "card_faces" in y.keys():
                for i in y["card_faces"]:
                    em.set_image(url=i["image_uris"]['art_crop'])
                    await ctx.send(embed= em)
            else:
                em.set_image(url=y["image_uris"]['art_crop'])
                await ctx.send(embed= em)
        elif(y['object']=="error"):
            await ctx.send(y["details"])
            
    @mg.command(name="swap")
    async def magic_swp(self ,ctx):
        x=["""How much would you pay , to rule the world. \n[Power for blood], a demon tribal list with Rakdos the Showstopper \n https://deckstats.net/deck-22298411-f8587d0b5bf631d05b2f77e8ba6012b8.html""",
           """Do you dare to ask what the Reaperking sows, for he shall reap havoc and DEATH.\n[c c c r a c k ] Scarecrow tribal featuring Reaper king \n https://deckstats.net/deck-22298442-5576b511cad4b5638fd936094907a3cd.html""",
           """Those who come from the skies might just [ascend from heaven]. \nAngels who protected you might be your undoing. Angel tribal with Bruna The faded light\n https://deckstats.net/deck-22294482-9ece70fdccf573091a8f5243897be4c7.html""",
           """The spirts call for you. Do not get lost upon crosing the bridge, or you might just be [Spirited away]\n https://deckstats.net/deck-22298489-953c8ee1f9ddd1d68288fdc6e3a44ce8.html""",
           """<The bargling>. \n YARRRRRGGGGGGGLLLLLEEEE. YARGLE YARGLE YARGLE. YARGLEEEEEEEEEEE\n https://deckstats.net/deck-22299373-2a4ca4f756bc370fb0d329a74bd8fe8f.html""",
           """It is said that the Qalasima has a beast. The beast hunts hearts and kills when you look back. <Gorey Death> with Gore claw The terror of Qalasima\n https://deckstats.net/deck-22299499-a6ec9b0decbbf063f310a7833beadaea.html""",
           """When emotionally drained zombies are bought back from the deck, they stay forever. <Brokken zombies> with Brokko Apex of Forever\n https://deckstats.net/deck-22299496-78941b8c8fa9588dd1e1ebfbe214d381.html""",
           """At the edge of day and night, those who crave for blood appear. <Twilight trouble> with Edgar markov \n https://deckstats.net/deck-22301535-ea93dff73a3c684a7948f7ebae49fe23.html""",
           """The tower. Representing disaster, and a calamity. Yet , at times like these, you <discard, and disregard>. If you don't , the haunt of  hightower might just take you over\n https://deckstats.net/deck-22301566-c181393f4afd469366cf8042cf2849a8.html""",
           """What you think is real, might not be. For she shall walk this plane, and ruin it all. <Eldr(itch)razi Horror> beckons to coming of Emrakul the Promised end\n https://deckstats.net/deck-22301583-e2e6ac7382dc28a45a106411918a5b7d.html"""]
        await ctx.send(random.choice(x))
    

        
class Yugi(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def ycard(self,ctx,*,args):
        x=str(args)
        x=x.replace(" ","%20")
        y=None
        z="https://db.ygoprodeck.com/api/v3/cardinfo.php?name="+x
        print(z)
        async with aiohttp.request("get",z) as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        try:
                
            em = discord.Embed(title=y[0][0]['name'])
            em.set_image(url=y[0][len(y[0])-1]["image_url"])
            await ctx.send(embed= em)
        except:
            await ctx.send("Card name " + str(args) + " not found")
##

##class HS:
##    def __init__(self, bot):
##        self.bot=bot
##
##    @commands.command()
##    async def hscard(self,ctx,args):
##        x=str(args)
##        x=x.replace(" ","%20")
##        y=None
##        h={"X-Mashape-Key": "nZsSdxxcN1mshskGiEd18AIpXDksp19XabQjsn8LotoIfnfv54","Accept": "application/json"}
##        async with aiohttp.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/"+x,headers=h)) as res:
##            print(res.status)
##            y=json.loads(await res.text())
##        res.close()
##        try:
##            em = discord.Embed(title=y[[0]['name'])
##            em.set_image(url=y[0]['img'])
##            await ctx.send(embed= em)
##        except:
##            await ctx.send("Card name " + str(args) + " not found")

def setup(bot):
    bot.add_cog(Magic(bot))
    bot.add_cog(Yugi(bot))
