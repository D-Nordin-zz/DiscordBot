import discord
from discord.ext import commands
from configUtil import configUtil

#import the config utility and load the config
config = configUtil()
config.loadConfig()
    
#create an instance of the bot
bot = commands.Bot(command_prefix='!')

#print to console when the bot has logged in to the server
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#register a command to message the user the github link
@bot.command(name='github')
async def dmGithub(ctx):
    direct = await ctx.author.create_dm()
    await direct.send(config.getProperty('githubLink'))

#register a test command
@bot.command(name='test')
async def test(ctx, *, args):
    await ctx.send('User {0}(perms: {2}), has sent the following message {1}.'.format(ctx.author, args, ctx.author.roles))


bot.run(config.getProperty('token'), bot=True)
