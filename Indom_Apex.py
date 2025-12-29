#APPLICATION ID :- 1421736899768352778
#PUBLIC KEY FOR BOT :- 70791ed5da97f0bc7c3aeca478b2e3ef0d3f447ee2b996c7eee89949c23c2ca9
#DISCORD PROVIDED LINK :- https://discord.com/oauth2/authorize?client_id=1421736899768352778
import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from pytube import YouTube
import os

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='@', intents = intents)

#--------- welcoming and onboaring part -------------

@bot.event
async def on_members_join(member):
    channel = bot.get_channel(1143915202925043846) #remember to replace
    if channel:
        embed = discord.Embed(title =f"Welcome {member.name} beyotch!!" , description= f"Thanks for giving your unemployed time to {member.guild.name}!!" )
    if member.avatar:
        embed.set_thumbnail(url = member.avatar.url)
    await channel.send(embed = embed)

#--------- Meme generation --------------
@bot.command()
async def meme(ctx, top: str, bottom: str):
    try:
        img = Image.open('meme_templet.jpg') # need to provide a meme temp
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(impact.tff, 40)
        draw.text((10,10), top.upper(), font = font, fill = "white")
        draw.text((10, img.height - 60 ), bottom.upper(), font = font, fill = "white")
        img.save('meme_output.jpg')
        await ctx.send(file = discord.File('meme_output.jpg'))
        os.remove('output.jpg')
    except Exception as e:
        await ctx.send(f"Error generating the meme: {e}")

#--------- Youtube music player --------------
@bot.command()
async def play(ctx, url: str):
    voice = ctx.author.voice
    if not voice:
        await ctx.send("you need to be in a voice channel to use this command")
        return
    channel = voice.channel
    try:
        vc = ctx.voice_client
        if not vc:
            vc = await channel.connect()
        elif vc.channel != channel:
            await vc.move_to(channel)
            
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio = True).first()
        stream.download(filename= "song.mp3")
        if vc.is_playing():
            vc.stop()
        vc.play(discord.FFmpegPCMAudio("song.mp3"))
        await ctx.send(f"Now playing: {yt.title}")
    except Exception as e:
        await ctx.send(f"Error playing: {e}")

#--------- Clean up playback --------------
@bot.command()
async def stop(ctx):
    vc = ctx.voice_client
    if vc and vc.is_playing():
        vc.stop()
        await ctx.send("Stopped playing and disconnected.")
    else:
        await ctx.send("Not playing anything currently")
    
bot.run('MTQyMTczNjg5OTc2ODM1Mjc3OA.Gi1SVS.X7RSOT4hI1Jr468q6S1lpa_RM5UUimn0-qI1LM')


        
