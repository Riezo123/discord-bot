import os
import discord
from discord.ext import commands

# التوكن سيُقرأ من إعدادات Railway (وليس من الكود لحمايته)
TOKEN = os.environ.get(discord-Token")

# تفعيل الصلاحيات (ضرورية لقراءة الملفات والرسائل)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"تم تسجيل الدخول كـ {bot.user}")

# أمر لإرسال صورة من رابط (URL) مع كلام
@bot.command()
async def sendurl(ctx, url: str, *, text: str):
    embed = discord.Embed(
        title="رسالة",
        description=text,
        color=discord.Color.blue()
    )
    embed.set_image(url=url)
    await ctx.send(embed=embed)

# أمر لإرسال صورة من جهازك مع كلام
@bot.command()
async def sendfile(ctx, *, text: str):
    # التحقق من وجود مرفق (صورة) في رسالتك
    if not ctx.message.attachments:
        await ctx.send("الرجاء إرفاق صورة مع الأمر.")
        return
    
    # جلب الصورة المرفقة
    image_url = ctx.message.attachments[0].url
    
    embed = discord.Embed(
        title="رسالة",
        description=text,
        color=discord.Color.green()
    )
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

# تشغيل البوت
if TOKEN:
    bot.run(TOKEN)
else:
    print("خطأ: لم يتم العثور على التوكن. تأكد من إضافته في إعدادات Railway.")
