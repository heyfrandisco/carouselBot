# Created by 2inthemorningg, atlasjx, FPort0
# Developed by 2inthemorningg
# Tested by atlasjx, FPort0

import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='{|}')
TOKEN = "OTYyNzkzODk2NDMyMjU0OTc2.YlMtsA.d0UMMzatRvR4hpFOjYEakqRs1F0"


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    print("Bot made by 2inthemorning(g)")
    print("Version 1.0.0")


@bot.command()
async def voltinha(ctx, member: discord.Member, channel1: discord.VoiceChannel, channel2: discord.VoiceChannel):

    while True:
        await member.move_to(channel1)

        time.sleep(0.75)

        await member.move_to(channel2)

        time.sleep(0.75)         


@bot.command()
async def xau(ctx):
    print("EXITING...")
    exit(0)

bot.run(TOKEN)
