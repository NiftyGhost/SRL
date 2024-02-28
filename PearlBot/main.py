import discord 
import os
import random
import string
import requests
from PIL import Image

client = discord.Client()
 

weapons = ['.52 Gal Deco','.96 Gal','.96 Gal Deco','Aerospray MG (Curling-Bomb Launcher)','Aerospray PG (Booyah Bomb)','Aerospray RG (Baller)','Ballpoint Splatling','Ballpoint Splatling Nouveau','Bamboozler 14 Mk I (Tenta Missles)','Bamboozler 14 Mk II (Burst-Bomb Launcher)','Bamboozler 14 Mk III (Bubble Blower)','Blaster','Bloblobber','Bloblobber Deco','Carbon Roller','Carbon Roller Deco','Cherry H-3 Nozzlenose','Clash Blaster','Clash Blaster Neo','Classic Squiffer','Clear Dapple Dualies','Custom Blaster','Custom Dualie Squelchers','Custom E-liter 4K','Custom E-liter 4K Scope','Custom Explosher','Custom Goo Tuber','Custom Hydra Splatling','Custom Jet Squelcher','Custom Range Blaster','Custom Splattershot Jr.','Dapple Dualies','Dapple Dualies Nouveau','Dark Tetra Dualies','Dualie Squelchers','Dynamo Roller','E-liter 4K','E-liter 4K Scope','Enperry Splat Dualies','Explosher','Firefin Splat Charger','Firefin Splatterscope','Flingza Roller','Foil Flingza Roller','Foil Squeezer','Forge Splattershot Pro','Fresh Squiffer','Glooga Dualies','Glooga Dualies Deco','Gold Dynamo Roller', 'Heavy Splatling','Heavy Splatling Deco','Heavy Splatling Remix','Hero Blaster Replica','Hero Brella Replica','Hero Charger Replica','Hero Dualie Replicas','Hero Roller Replica','Hero Shot Replica','Hero Slosher Replica','Hero Splatling Replica','Herobrush Replica','Hydra Splatling','Inkbrush','Inkbrush Nouveau','Jet Squelcher','Kensa .52 Gal','Kensa Charger','Kensa Dynamo Roller','Kensa Glooga Dualies','Kensa L-3 Nozzlenose','Kensa Luna Blaster','Kensa Mini Splatling','Kensa Octobrush','Kensa Rapid Blaster','Kensa Sloshing Machine','Kensa Splat Dualies','Kensa Splat Roller','Kensa Splatterscope','Kensa Splattershot','Kensa Splattershot Jr.','Kensa Splattershot Pro','Kensa Undercover Brella','Krak-On Splat Roller','L-3 Nozzlenose','L-3 Nozzlenose D','Light Tetra Dualies','Luna Blaster','Luna Blaster Neo','Mini Splatling',"N-ZAP '83 (Ink Storm)","N-ZAP '85 (Ink Armor)","N-ZAP '89 (Tenta Missles)",'Nautilus 47 (Baller)','Nautilus 79 (Inkjet)','Neo Splash-o-matic','Neo Sploosh-o-matic','New Squiffer','Octobrush','Octobrush Nouveau','Octo Shot Replica','Permanent Inkbrush','Range Blaster','Rapid Blaster','Rapid Blaster Deco','Rapid Blaster Pro','Rapid Blaster Pro Deco','Slosher','Slosher Deco','Sloshing Machine','Sloshing Machine Neo','Soda Slosher','Sorella Brella','Splash-o-matic','Splat Brella','Splat Charger','Splat Dualies','Splat Roller','Splatterscope','Splattershot','Splattershot Jr.','Splattershot Pro','Sploosh-o-matic','Sploosh-o-matic 7 (Ultra Stamp)','Squeezer','Tenta Brella','Tenta Camo Brella (Ultra Stamp)','Tenta Sorella Brella','Tentatek Splattershot','Tri-Slosher','Tri-Slosher Nouveau','Undercover Brella','Undercover Sorella Brella','Zink Mini Splatling']

mayo = ["Pshh. Ketchup is BOOOOOOOOO-RING! It's like the Sheldon of condiments.", 'But at least mayo is true to itself. Ketchup is just wannabe jam.', 'You basically just take some fruit and mix it with sugar. Boom. Tomato Jam.']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hey, Agent 4!')

    if message.content.startswith('$info'):
        await message.channel.send('This bot was created by **Nifty#6240** in the server **Squid Research Lab #2!**\n**Join here:** https://discord.gg/Z2aZvU7p2f') 

    if message.content.startswith('$help'):
      await message.channel.send('These are my commands!\n`$hello: Greeting.`\n`$info: Description of the bot.`\n`$help: Gives commands and actions.`\n`$random: Gives a random weapon.`\n`$mayo: I talk about mayo and roast you for loving ketchup.`')

    if message.content.startswith('$random'):
      weaponChosen = random.choice(weapons)
      await message.channel.send('Your random weapon is: ' '**'+weaponChosen+'**')

    if message.content.startswith('$mayo'):
      mayonaise = random.choice(mayo)
      await message.channel.send(mayonaise)

    if message.content.startswith('$pic'):
     weaponChosen = random.choice(weapons)

     await message.channel.send('Your random weapon is: ' '**'+weaponChosen+'**')
     # How to show a picture
     await message.channel.send(file=discord.File('52_Gal.png'))

# To check if the rate limit is overloaded and we are banned (cooldown)
r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print("No rate limit")

client.run(os.getenv('TOKEN'))