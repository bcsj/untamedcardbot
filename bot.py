from discord.ext import commands

from bot_token import token
import untamed
import tools

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import shlex

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def factions(ctx):
    L = []
    for key in untamed.factions.keys():
        L.append(untamed.factions[key]['discord_emoji'] + ' ' + untamed.factions[key]['name'])
    msg = 'Available factions are:\n' \
        + '\n'.join(L)
    await ctx.send(msg)
    
@bot.command()
async def faction(ctx, name : str):
    closest = process.extractOne(name, untamed.factions.keys())
    if closest[1] < 75:
        msg = 'Could not recognize faction "' + name + '".\n' \
            + 'Type "!factions" for a full list of factions.'
    else:
        name = closest[0]
        L = []
        for key in untamed.cards.keys():
            if untamed.cards[key]['faction'] == name:
                card = untamed.cards[key]
                L.append(tools.print_card_short(card))
        msg = name + ' faction contains the cards:\n' \
            + '\n'.join(L)
    await ctx.send(msg)

@bot.command()
async def search(ctx, *query : str):
    if query[0].lower() in ["help", "syntax", "guide"]:
        msg = 'Search Syntax Guide:\n' \
                + 'f:<faction>\n' \
                + 't:<type>\n' \
                + 'x:<body text>, use \'\' if the search string has spaces. "" doesn\'t work!'
        await ctx.send(msg)
        return

    q_map = {
        'f': {
            'name': 'faction',
            'type': str,
            'check': 'fuzz',
            'strictness': 75},
        't': {
            'name': 'type',
            'type': str,
            'check': 'fuzz',
            'strictness': 95},
        'x': {
            'name': 'text',
            'type': str,
            'check': 'substring',
            'strictness': None}}

    query = ' '.join(query)
    query = shlex.split(query)
    res = untamed.cards.copy()
    for que in query:
        if ":" not in que:
            return
        q,s = que.split(':')
        if q not in q_map.keys():
            msg = 'Unknown parameter "'+q+'".'
            await ctx.send(msg)
            return
        
        for key in untamed.cards.keys():
            if key in res.keys():
                card = res[key]
                if q_map[q]['check'] == "fuzz":
                    if fuzz.partial_ratio(card[q_map[q]['name']],s) < q_map[q]['strictness']:
                        del res[key]
                    continue
                if q_map[q]['check'] == "substring":
                    if s.lower() not in card[q_map[q]['name']].lower():
                        del res[key]
                    continue

    n = len(res.keys())
    if n > 1:
        L = []
        for key in res:
            card = res[key]
            L.append(tools.print_card_short(card))
            msg = str(n) + ' hits! Matches:\n' \
                + '\n'.join(L)
    elif len(res.keys()) == 1:
        key = list(res.keys())[0]
        card = res[key]
        msg = '1 hit! Match:\n' + tools.print_card(card)
    else:
        msg = 'No matching cards'
    await ctx.send(msg)

@bot.command()
async def card(ctx, *name : str):
    name = ' '.join(name)
    closest = process.extractOne(name.lower(), untamed.cards.keys())
    if closest[1] < 75 and name.lower() != "what the hell":
        msg = 'Could not find card "' + name + '"\n' + ' Did you mean ' + closest[0]
    else:
        card = untamed.cards[closest[0]]
        msg = tools.print_card(card)      
    await ctx.send(msg)

bot.run(token)
