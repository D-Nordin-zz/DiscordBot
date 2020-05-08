import discord
from discord.ext import commands
from configUtil import configUtil

#import the config
config = configUtil().loadConfig()
    
#create an instance of the bot
bot = commands.Bot(command_prefix='!')

#print to console when the bot has logged in to the server
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#register a test command
@bot.command(name='test')
async def test(ctx, *, args):
    await ctx.send('User {0}(perms: {2}), has sent the following message {1}.'.format(ctx.author, args, ctx.author.roles))


bot.run(config['token'], bot=True)
