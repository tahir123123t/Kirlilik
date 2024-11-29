import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olaraq giriş yaptık!')

@bot.command()
async def başla(ctx):
    print("Başla komutu alındı")  # Log mesajı eklendi
    try:
        mesaj = await ctx.send('''Merhaba sıkıntın ne\n
1️⃣ Hedef Kitle 1\n
Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen gençler\n
2️⃣ Hedef Kitle 2\n
Evde ürettikleri atık miktarını azaltmak isteyen ancak nereden başlayacaklarını bilmeyen yetişkinler.\n
3️⃣ Hedef Kitle 3\n
Çevreye önem veren ve çevre dostu uygulamalar və atıkları azaltmanın yolları hakkında daha fazla bilgi edinmek isteyen kişiler.''')
        print("Mesaj gönderildi")  # Log mesajı eklendi
    except Exception as e:
        print(f"Mesaj gönderilemiyor: {e}")  # Xəta mesajı eklendi

    reactions = ['1️⃣', '2️⃣', '3️⃣']
    for emoji in reactions:
        try:
            await mesaj.add_reaction(emoji)
            print(f"{emoji} tepkisi eklendi")  # Log mesajı eklendi
        except Exception as e:
            print(f"tepki ilave edilemedi: {e}")  # hata mesajı eklendi

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    print(f"Tepki eklendi: {reaction.emoji} kullanıcı: {user}")  # Log mesajı eklendi

    try:
        if str(reaction.emoji) == '1️⃣':
            await reaction.message.channel.send(f'{user.mention}, Bişi ekle')
            print("1️⃣ tepkisine yanıt gönderildi")  # Log mesajı eklendi
        elif str(reaction.emoji) == '2️⃣':
            await reaction.message.channel.send(f'{user.mention}, Bişi ekle')
            print("2️⃣ tepkisine yanıt gönderildi")  # Log mesajı eklendi
        elif str(reaction.emoji) == '3️⃣':
            await reaction.message.channel.send(f'{user.mention}, Bişi ekle')
            print("3️⃣ tepkisine yanıt gönderildi")  # Log mesajı eklendi
    except Exception as e:
        print(f"Yanıt gönderilemiyor: {e}")  # hata mesajı eklendi

bot.run('UR TOKEN HERE')
