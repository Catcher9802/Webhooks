import requests
import random
import threading
import discord
from discord.ext import commands

token = "ใส่โทเค็นบอท"
# ใส่โทเค็นบอทแล้วรันเมื่อบอทออนไลน์ใช้คำสั่ง !help ในดิสคอร์ดที่มีบอทอยู่

b = commands.Bot(command_prefix="!",help_command=None)
@b.event
async def on_ready():
	print(b.user)
	
@b.command()
async def help(ctx):
	await ctx.channel.send("""
	**คำสั่งสร้างเว็บฮุก !create
	คำสั่งสแปมเว็บฮุก !run [จำนวน]
	คำสั่งลบเว็บฮุกทั้งหมด !delete
	**""")
	
@b.command()
async def create(ctx):
	for i in range(10):
		a = str(random.randint(1000000,9999999))
		await ctx.channel.create_webhook(name=a)
	
@b.command()
async def run(ctx,jam:int):
	for w in await ctx.guild.webhooks():
		def a():
			requests.post(f'{w.url}',json={"content" : "@everyone hello"},params={'wait' : True})
		for i in range(jam):
			threading.Thread(target=a).start()
		
@b.command()
async def delete(ctx):
	for x in await ctx.guild.webhooks():
		try:
			await x.delete()
		except:
			pass
	
		
b.run(token)