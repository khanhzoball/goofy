import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('goofy'):
        await message.channel.send('GOOFY HAS ARRIVED FOR THE RECKONING')

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel
    else:
        await ctx.send('GOOFY NEEDS VOICE CHANNEL')


print(os.getenv('TOKEN'))

client.run(os.getenv('TOKEN'))