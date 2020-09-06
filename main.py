import discord

bot = discord.Client()

@bot.event
async def on_ready():
    print("Ready set GO")
    await bot.change_presence(status=discord.Status.idle,
                              activity=discord.Game("Im the waifu of deuzil"))

token = "NzIzMTQyMjc3MzE2NDc2OTY4.XutUug.68PYYU6uQwTQCqUKR-R0xraEDlA"

print("lancement en court")

bot.run(token)