import os
import discord
from discord import app_commands
import re

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()

bot = discord.Client(intents=intents)
cmd = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    await cmd.sync()
    print(f"{bot.user} 로그인 완료")


@cmd.command(name="ㅇㄹ", description="자동 번호 매기기")
@app_commands.describe(내용="입력할 내용")
async def auto_number(interaction: discord.Interaction, 내용: str):

    last_num = 0


    async for msg in interaction.channel.history(limit=50):

  
        match = re.match(r"^(\d+)\.\s*", msg.content)

        if match:
            last_num = int(match.group(1))
            break

    await interaction.response.send_message(
        f"{last_num + 1}. {내용}"
    )


bot.run(TOKEN)