import discord, os, time
from discord.ext import commands

class Misc(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
    
  @commands.command()
  async def ping(self, ctx):
    before = time.monotonic()
    ping = (time.monotonic() - before) * 1000
    await ctx.send("🏓 pong! {0:.2f}ms".format(self.bot.latency * 1000))

  @commands.command()
  async def on_message(message):
    if message.author == commands.User:
        return
    if message.content == "oser":
      await message.channel.send(f"turu")

  @commands.command(aliases=['echo'])
  async def say(self, ctx, *, msg):
    if ctx.author.id == 851721079407116398:
      await ctx.message.delete()
      await ctx.send(msg)

def setup(bot):
  bot.add_cog(Misc(bot))