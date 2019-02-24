import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='wik')

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    
@bot.command(pass_context=True)
async def invite():
    await bot.say('Help Share our server')
    await bot.say('https://discord.gg/gyP2UUS')
    await bot.say('https://discordapp.com/api/oauth2/authorize?client_id=546627382153576455&permissions=0&scope=bot')
    
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    role=discord.utils.get(ctx.message.server.roles,name='Muted')
    
    await bot.add_roles(target,role)
    
@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    await bot.send_message(target,'Warning!!')
    
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    await bot.kick(target)
    
@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    await bot.ban(target)
    
    
    
    
client.run(str(os.environ.get('NTQ2NjI3MzgyMTUzNTc2NDU1.D0rcAg.jDVUVS8Wv2Lt3j5AtO3uvmuWL6Eh')))
