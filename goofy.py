import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return  
    # if message.author.name == "":
    #     await message.channel.send('GOOFY SAYS STFU')
    elif message.content.startswith('goofy'):
        await message.channel.send('GOOFY HAS ARRIVED FOR THE RECKONING')
    await client.process_commands(message)

@client.command(pass_context=True)
async def goofy(ctx, *args):
    print(args[0])
    
    if args[0] == "summon":
        channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await channel.connect()
        else:
            await ctx.voice_client.move_to(channel)
    elif args[0] == "kill":
        await ctx.voice_client.disconnect()

print(os.getenv('TOKEN'))

client.run(os.getenv('TOKEN'))