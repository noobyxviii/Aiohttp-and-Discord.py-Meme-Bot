import discord, random, aiohttp
from discord.ext import commands


client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Im Ready")

@client.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json") as r:
            memes = await r.json()
            embed = discord.Embed(
                color = discord.Color.purple()
            )
            embed.set_image(url = memes["data"]["children"][random.randint(0, 25)]["data]["url"])
            await ctx.send(embed = embed)

client.run(token)
