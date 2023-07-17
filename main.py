
import discord
import random
from discord.ext import commands, tasks
#import youtube_dl
import yt_dlp as youtube_dl
from pytube import YouTube
import os
from dotenv import load_dotenv
import asyncio
import time
import warnings
#import keep_alive

intents = discord.Intents.all()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or('!',), intents=intents)
# youtube_dl.utils.bug_reports_message = lambda: ''

member = []

@bot.event
async def on_ready():
    print('想一起聊聊天嗎？', bot.user.name)
    game = discord.Game('努力闖禍中')
    await bot.change_presence(status=discord.Status.idle, activity=game)
@bot.event
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
        return
    if message.content.startswith('Hi'):
        channel = message.channel
        await channel.send('想一起聊聊天嗎？')

    if message.content.startswith('跟我打聲招呼吧'):
        channel = message.channel
        await channel.send('那你先跟我說你好')

        def checkmessage(m):
            return m.content == '你好' and m.channel == channel

        msg = await bot.wait_for('message', check=checkmessage)
        await channel.send(f'嗨, {msg.author.mention}!')

    if message.content.startswith('要不要自我介紹一下呢?'):
        channel = message.channel
        msg = random.choice(['不太想ㄟ，今天心情不太好', '你好我叫小R，是木馬的孩子，請多指教', '西風騎士團，「火花騎士」，可莉，前來報到！…呃——後面該說什麼詞來著？可莉背不下來啦…', '啦啦啦~噠噠噠~蹦蹦炸彈！'])
        await channel.send(msg)

    if message.content.startswith('說'):
        tmp = message.content.split(" ", 1)
        if len(tmp) == 1:
            await message.channel.send("你要我說什麼啦？")
        else:
            await message.channel.send(tmp[1])

    if message.content.startswith('更改狀態'):
        tmp = message.content.split(" ", 1)
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            await bot.change_presence(status=discord.Status.idle, activity=game)

    if message.content == '小R你喜歡誰':
        channel = message.channel
        member = [m for m in message.guild.members if not m.bot]
        mem = random.choice(member).mention
        await channel.send(f'今天{mem}是不是有點好看啊，我...我才沒有說喜歡他呢>////<')
    if message.content == '抽一個小孩':
        channel = message.channel
        member = [m for m in message.guild.members if not m.bot]
        mem = random.choice(member).mention
        await channel.send(f'就選{mem}啦')
    await bot.process_commands(message)
@bot.command(name="hello",help="用指令跟小R打招呼")
async def hello(ctx):
    await ctx.send('Hello!')
@bot.command(name="chat",help="當前聊天選項")
async def chat(ctx):
    await ctx.send('當前聊天選項\n1.Hi\n2.要不要自我介紹一下呢?\n3.說 \'msg\'\n4.更改狀態 \'msg\'\n5.抽一個小孩\n')

@bot.command(name="join",help="讓小R加入語音頻道")
async def join(ctx):
    # 這裡的指令會讓機器人進入call他的人所在的語音頻道
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if ctx.author.voice == None:
        await ctx.send("You are not connected to any voice channel")
    elif voice == None:
        voiceChannel = ctx.author.voice.channel
        await voiceChannel.connect()
    else:
        await ctx.send("Already connected to a voice channel")

@bot.command(name='leave', help='讓小R從語音頻道滾蛋')
async def leave(ctx):
    # 離開call他那個伺服器的所在頻道
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice == None:
        await ctx.send("The Bot is not connected to a voice channel")
    else:
        await voice.disconnect()

# warnings.filterwarnings("ignore")
# load_dotenv()
#
# ytdl_format_options = {
#     'format': 'bestaudio/best',
#     'restrictfilenames': True,
#     'noplaylist': True,
#     'nocheckcertificate': True,
#     'ignoreerrors': False,
#     'logtostderr': False,
#     'quiet': True,
#     'no_warnings': True,
#     'default_search': 'auto',
#     'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
# }
#
# ffmpeg_options = {
#     'options': '-vn'
# }
#
#
# ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
#
#
# str_music=[]
# str_url=[]
# song=[]
# class YTDLSource(discord.PCMVolumeTransformer):
#     def __init__(self, source, *, data, volume=0.5):
#         super().__init__(source, volume)
#         self.data = data
#         self.title = data.get('title')
#         self.url = ""
#待開發
# #keep_alive.keep_alive()
bot.run("MTEyODE1NjE0MTM2NTUwMTk1Mg.GmXAkG.Y5AUqfDYOARwZmFDsvKox6o7zQVL2WNBcEo8hU")  # TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
