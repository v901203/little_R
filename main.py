# 導入Discord.py
import discord
import random
import keep_alive
import time

# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


member=[]

# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('想一起聊聊天嗎？', client.user)
    game = discord.Game('努力學習py中')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)



@client.event
# 當有訊息時
async def on_message(message):
    if message.content.startswith('D'):
        await message.delete()
    if message.content.startswith('Hi'):
        channel = message.channel
        await channel.send('想一起聊聊天嗎？')
    if message.content.startswith('跟我打聲招呼吧'):
        channel = message.channel
        # 機器人叫你先跟他說你好
        await channel.send('那你先跟我說你好')

        # 檢查函式，確認使用者是否在相同頻道打上「你好」
        def checkmessage(m):
            return m.content == '你好' and m.channel == channel

        # 獲取傳訊息的資訊(message是類型，也可以用reaction_add等等動作)
        msg = await client.wait_for('message', check=checkmessage)
        await channel.send('嗨, {.author}!'.format(msg))

    if message.content.startswith('要不要自我介紹一下呢?'):
        channel = message.channel
        msg=['不太想ㄟ，今天心情不太好','你好我叫小R，是木馬的孩子，請多指教','西風騎士團，「火花騎士」，可莉，前來報到！…呃——後面該說什麼詞來著？可莉背不下來啦…','啦啦啦~噠噠噠~蹦蹦炸彈！']
        await channel.send(random.choice(msg))

    if message.author == client.user:
        return
        # 如果以「說」開頭
    if message.content.startswith('說'):
        # 分割訊息成兩份
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要我說什麼啦？")
        else:
            await message.channel.send(tmp[1])
    if message.content.startswith('更改狀態'):
        # 切兩刀訊息
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
            await client.change_presence(status=discord.Status.idle, activity=game)

    if message.content == '喜歡誰':
        #member=[]
        channel = message.channel
        for m in message.guild.members:
            if(m.bot!=1):
                member.append(m)
        mem=random.choice(member).id
        await channel.send(f'今天<@{mem}>是不是有點好看阿,我...我才沒有說喜歡他勒>////<')


keep_alive.keep_alive()
client.run("MTEyODE1NjE0MTM2NTUwMTk1Mg.GJc87X.yoaB1DbM96GJnoN8yPVB6Uk3yTg2dESGxFKJhw")  # TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面