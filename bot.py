import discord
from discord import Option
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

TOKEN = os.getenv("TOKEN")
GUILD_IDS = [956778581160247366]  # ← BOTのいるサーバーのIDを入れます


@bot.event
async def on_ready():
    print(f"Bot名:{bot.user} On ready!!")


@bot.slash_command(description="あなたの名前か入力した名前に挨拶します", guild_ids=GUILD_IDS)
async def hello(
    ctx: discord.ApplicationContext,
    name: Option(str, required=False, description="名前を入力してね", )
):
    if not name:
        name = ctx.author
    await ctx.respond(f"こんにちは！ {name} さん！")

bot.run(TOKEN)
