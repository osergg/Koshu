import discord, os
from discord.ext import commands

class Mod(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(
    title = 'Kick',
    description = 'Anda di Kick Oleh',
    colour = discord.Color.red())
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(
    title = 'Banned',
    description = 'Anda di Banned oleh',
    colour = discord.Color.red())
    embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        embed = discord.Embed(
        title = 'UnBanned',
        description = 'Anda di UnBanned Oleh ',
        colour = discord.Color.green())
        embed.set_footer(text=f"Command used by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

  @commands.command(description="Mutes the specified user.")
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="🤫Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="🤫Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"🤫Muted {member.mention} Alasan : {reason}")
    await member.send(f"Kamu Mute di server {guild.name} Alasan : {reason}")

  @commands.command(description="Unmutes a specified user.")
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: discord.Member):
    await ctx.message.delete()
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"Lain kali jangan begitu ya {ctx.guild.name}")

  @commands.command()
  @commands.has_permissions(manage_messages=True, manage_channels=True)
  async def delete(self, ctx, limit=0, member: discord.Member = None):
      await ctx.message.delete()
      msg = []
      try:
        limit = int(limit)
      except:
        await ctx.send("Please pass in an integer as limit")
        return
      if limit == 0:
        await ctx.send("Harap tentukan berapa banyak pesan yang ingin Anda hapus!", delete_after=4)
        return
      if not member:
          await ctx.channel.purge(limit=limit)
          return await ctx.send(f"Dihapus {limit} pesan", delete_after=3)
      async for m in ctx.channel.history():
        if len(msg) == limit:
                break
        if m.author == member:
                msg.append(m)
      await ctx.channel.delete_messages(msg)
      await ctx.send(f"Dihapus {limit} pesan dari {member.mention}", delete_after=3)

def setup(bot):
  bot.add_cog(Mod(bot))  