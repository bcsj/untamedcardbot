from discord.ext import commands

import untamed
import difflib

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def factions(ctx):
    msg = 'Available factions are:\n' \
        + '\n'.join(untamed.factions)
    await ctx.send(msg)
    
@bot.command()
async def faction(ctx, name : str):
    if name not in untamed.factions:
        msg = 'Could not recognize faction "' + name + '".\n' \
            + 'Type "!factions" for a full list of factions.'
    else:
        L = []
        for key in untamed.cards.keys():
            if untamed.cards[key]['faction'] == name:
                card = untamed.cards[key]
                L.append(key + ', ' + card['type'])
        msg = name + ' faction contains the cards:\n' \
            + '\n'.join(L)
    await ctx.send(msg)

@bot.command()
async def card(ctx, *name : str):
    name = ' '.join(name)
	closest = difflib.get_close_matches(name.lower(), untamed.cards.keys(),1)
	
    if closest not in untamed.cards.keys():
        msg = 'Could not find card "' + name + '".' + (' Did you mean\n' + '\n'.join(closest) if len(closest) > 0 else '')
    else:
		card = untamed.cards[closest]
        msg = card['name'] + ', ' + card['faction'] + ' faction' + '\n' \
              + card['type'] + (', cost: ' + str(card['cost']) if card['cost'] is not None else '') + '\n' \
              + ('Power: ' + str(card['power']) + ', ' if card['power'] is not None else '') \
              + ('Health: ' + str(card['health']) + '\n' if card['health'] is not None else '') \
              + card['text']        
    await ctx.send(msg)

bot.run('token')
