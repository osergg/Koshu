import discord, os
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=".k")
bot.remove_command('help')
status=cycle(['Maintenance','Maintenance.','Maintenance..','Maintenance...'])

@bot.event
async def on_ready():
    change_status.start()
    print('Online {0.user}'.format(bot))
    
@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game(next(status)))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		embed = discord.Embed(title='Error',
		description='Command tidak ditemukan.',
		colour=discord.Color.red())
		await ctx.send(embed=embed)

extensions = [
    'cogs.info',
    'cogs.mod',
    'cogs.miscellaneous',
    'cogs.music'
]

if __name__ == '__main__':
	for ext in extensions:
		bot.load_extension(ext)

keep_alive()
TOKEN = os.environ.get("TOKEN_BOT")
bot.run(TOKEN)