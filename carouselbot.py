# Created by heyfrandisco
# Developed by heyfrandisco

# Note: The sleep delay exists to prevent an "overload" that would cause the movement to glitch. 
# You can play with the time frame to find the optimum balance between being annoying and not destroying the app.
# Have fun :)

import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix={prefix})
TOKEN = {token}


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    print("Bot made by heyfrandisco")
    print("Version 1.0.0")


@bot.command()
async def ride(ctx, member: discord.Member, channel1: discord.VoiceChannel, channel2: discord.VoiceChannel):

    while True:
        await member.move_to(channel1)

        time.sleep(0.75)

        await member.move_to(channel2)

        time.sleep(0.75)         


@bot.command()
async def bye(ctx):
    print("EXITING...")
    exit(0)

bot.run(TOKEN)
