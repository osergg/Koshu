import discord, os
from discord.ext import commands

class Info(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def help(self, ctx):
    embed=discord.Embed(title="Koshu Commands", description=f"Prefix: `.k`\nGunakan `.kabout` untuk melihat informasi saya!\nDevelop by: `Oser#5825`", colour=discord.Color.blue())
    embed.add_field(name="😁 __Invite me to your server!__", value="[Click here](https://discord.com/api/oauth2/authorize?client_id=920703102766678147&permissions=1632590363766&scope=bot)\n*as Administrator*\n\n***List of Commands:***", inline=False)
    embed.add_field(name='📢 __Informations:__', value=" ‎ ‎ ‎ ・*Userinfo:* Menampilkan informasi tentang pengguna\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kuserinfo` / `.kuserinfo @user`\n‎ ‎ ‎ ‎ ・*Serverinfo:* Menampilkan informasi tentang Server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kserverinfo`\n‎ ‎ ‎ ‎ ・*Avatar:* Menampilkan informasi tentang gambar profile penguna\n ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kavatar` / `.kavatar @user`\n‎ ‎ ‎ ‎ ・*Servericon:* Menampilkan Icon server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kservericon`\n‎ ‎ ‎ ‎ ・*Permissions:* Menampikan izin pengguna di server\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kperms` / `.kpermissions`", inline=False)
    embed.add_field(name=' 🎨 __Miscellaneous:__', value="‎ ‎ ‎ ‎ ・*Help:* Menampilkan Help perintah\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.khelp`\n‎ ‎ ‎ ‎ ・*Invite:* Menampilkan undang link Bot Koshu\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kinvite`\n‎ ‎ ‎ ‎ ・*Ping:* Test latency\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kping`", inline=False)
    embed.add_field(name='🔈 __Voice Activity:__', value="‎ ‎ ‎ ‎ ・*Connect to a voice channel:* \n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kjoin`\n‎‎ ‎ ‎ ‎ ・*Playing to a voice channel:* \n‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kplay`/`.kp`\n‎ ‎ ‎ ‎ ・*Paused from a voice channel:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kpause`\n‎‎ ‎ ‎ ‎ ・*Resumed from a voice channel:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kresume`\n‎ ‎ ‎ ‎ ・*Skiped from a voice channel:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kskip`/`.ks`\n‎ ‎ ‎ ‎ ・*Stopped from a voice channel:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kstop`\n‎ ‎ ‎ ‎ ・*Disconnect from a voice channel:*\n‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ `.kleave`/`.kdc`\n‎ ‎ ‎ ‎ ", inline=False)
    embed.add_field(name='__Support me__', value="[Click here](https://www.youtube.com/channel/UCR36T_P4ZfD2JRg6jJtd7rw)", inline=False)
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def about(self, ctx):
    embed=discord.Embed(title="Information", description=f"Koshu adalah Bot yang dibuat untuk melayani member di dalam server ini :)\n\nUntuk informasi lebih lanjut tentang commands ini, gunakan `.khelp`\n\n[Subscribe](https://www.youtube.com/channel/UCR36T_P4ZfD2JRg6jJtd7rw) Oser\n\nPrefix: `.k`\nDevelop by: `Oser`", colour=discord.Color.orange())
    embed.set_footer(text=f"Command  used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def info(self, ctx):
    embed = discord.Embed(
    title = 'Bot Information',
    description = 'Koshu adalah Bot yang dibuat untuk melayani member di dalam server ini.', 
    colour = discord.Color.orange())
    embed.set_footer(text=f"command used by: {ctx.author.name}",icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def userinfo(self, ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
    roles = ' '.join([r.mention for r in user.roles][1:])
    avatar = f'{user.avatar_url}'
    embed = discord.Embed(title="User Informations",color=discord.Color.orange())
    embed.set_thumbnail(url=avatar)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="Nickname", value=user.nick, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Top Role", value=user.top_role.name, inline=True)
    embed.add_field(name=f"Roles ({len(user.roles)-1})", value=roles, inline=False)
    embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=True)
    embed.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y | %H:%M:%S'), inline=True)
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def avatar(self, ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
    embed = discord.Embed(title=f'{user.name}\'s avatar.',url=f"{user.avatar_url}",colour=discord.Colour.orange())
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def servericon(self, ctx):
    embed = discord.Embed(title=f'{ctx.guild.name} server icon.',url=f"{ctx.guild.icon_url}",colour=discord.Colour.orange())
    embed.set_image(url=ctx.guild.icon_url)
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def serverinfo(self, ctx):
    name = f'{ctx.guild.name}'
    owner = f'<@{ctx.guild.owner_id}>'
    id = f'`{ctx.guild.id}`'
    icon = f'{ctx.guild.icon_url}'
    categories = f'{len(ctx.guild.categories)}'
    channels = f'{len(ctx.guild.channels)}'
    text_channels = f'{len(ctx.guild.text_channels)}'
    voice_channels = f'{len(ctx.guild.voice_channels)}'
    total_member = f'`{ctx.guild.member_count}`'
    online_members = f'{sum(member.status==discord.Status.online and not member.bot for member in ctx.guild.members)}'
    offline_members = f'{sum(member.status==discord.Status.offline and not member.bot for member in ctx.guild.members)}'
    humans = f'{sum(not member.bot for member in ctx.guild.members)}'
    bots = f'{sum(member.bot for member in ctx.guild.members)}'
    roles = f'`{len(ctx.guild.roles)}`'
    boost_level = f'{ctx.guild.premium_tier}'
    total_boosts = f'{ctx.guild.premium_subscription_count}'
    embed = discord.Embed(title=name + " Server Information", color = discord.Color.orange())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Server Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="‎", value="‎", inline=True)
    embed.add_field(name="Members Informations:", value=f"All members: `{total_member}`\nHumans (hopefully): `{humans}`\nBots: `{bots}`\nOnline members: `{online_members}`\nOffline members: `{offline_members}`", inline=True)
    embed.add_field(name="Server Informations:", value=f"Total roles: `{roles}`\nCategories: `{categories}`\nTotal channels: `{channels}`\nText channels: `{text_channels}`\nVoice channels: `{voice_channels}`\nBoost level: `{boost_level}`\nTotal boost: `{total_boosts}`", inline=True)
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['perms'])
  async def permissions(self, ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
    avatar = f'{user.avatar_url}'
    perms = '`,\n `'.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed = discord.Embed(title=f'{user.name}' + "'s Permissions", description=f'`{perms}`', color = discord.Color.orange())
    embed.set_thumbnail(url=avatar)
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=['inv'])
  async def invite (self, ctx):
    embed=discord.Embed(title="Invite me to your server!", description="[Click here](https://discord.com/api/oauth2/authorize?client_id=920703102766678147&permissions=1632590363766&scope=bot)\n",color=discord.Color.orange())
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=["role"])
  async def roleinfo(self, ctx, *, role: discord.Role):
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    members = ''
    i = 0
    for user in role.members:
      members += f'{user.name}, '
      i+=1
      if i > 30:
        break
    embed=discord.Embed(color=discord.Color.orange())
    embed.set_author(name=role.name)
    embed.add_field(name="Users", value=len(role.members))
    embed.add_field(name="Mentionable", value=role.mentionable)
    embed.add_field(name="Hoist", value=role.hoist)
    embed.add_field(name="Position", value=role.position)
    embed.add_field(name="Managed", value=role.managed)
    embed.add_field(name="Colour", value=role.colour)
    embed.add_field(name='Creation Date', value=created_on)
    embed.add_field(name='Members', value=members[:-2], inline=False)
    embed.add_field(name=f'Role ID', value=f'{role.id}', inline=False)
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command(aliases=["channel"])
  async def channelinfo(self, ctx, channel: discord.TextChannel = None):
    if channel is None:
      channel = ctx.message.channel
    embed=discord.Embed(description=channel.mention, color=discord.Color.orange())
    embed.add_field(name="Name", value=channel.name)
    embed.add_field(name="Server", value=channel.guild)
    embed.add_field(name="ID", value=channel.id)
    embed.add_field(name="Category ID", value=channel.category_id)
    embed.add_field(name="Position", value=channel.position)
    embed.add_field(name="NSFW", value=str(channel.is_nsfw()))
    embed.add_field(name="Members (cached)", value=str(len(channel.members)))
    embed.add_field(name="Category", value=channel.category)
    embed.add_field(name="Created", value=channel.created_at.strftime("%d %b %Y %H:%M"))
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Info(bot))