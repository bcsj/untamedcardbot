from discord.ext import commands

# Custom tools
from bot_token import token
import untamed
import tools

# String logic
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import shlex

# Initialize bot
bot = commands.Bot(command_prefix='!')

# Remove default help
bot.remove_command('help')

# Server-side notification
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# Help command
@bot.command()
async def commands(ctx,*cmd):
    msg = '```\n' \
        + 'Type "!<command> <args>" to invoke a command.\n' \
        + 'For example: try typing "!card Radann".\n\n' \
        + 'This is a list of available commands:\n' \
        + ' - card <name>: looks up a card by it\'s name.\n' \
        + ' - factions: lists all animal factions.\n' \
        + ' - faction <name>: lists cards on a particular faction.\n' \
        + ' - search <query>: searches for cards. Type "!search syntax" for more info.\n' \
        + ' - what <keyword>: returns rules information about a keyword.\n' \
        + ' - commands: returns this message.\n' \
        + '```'
    await ctx.send(msg)

# Silly function
@bot.command()
async def who(ctx, *cmd):
    cmd = ' '.join(cmd)
    if cmd.lower() == "are you?":
        await ctx.send("I'm an untamed cardbot! I'm wild!")
    if cmd.lower() == "am i?":
        await ctx.send("I don't know, but compared to me you are tame...")


# Looks up game terms
@bot.command()
async def what(ctx, *cmd):
    # Easter Egg
    if ' '.join(cmd).lower() == "the hell":
        await card.callback(ctx, 'whitefur infantry')
        return

    i = 1 if cmd[0].lower() == 'is' else 0
    cmd = ' '.join(cmd[i:])
    closest = process.extractOne(cmd.lower(),untamed.terms.keys())
    if closest[1] < 75:
        msg = 'Could not recognize term "' + cmd + '".\n' \
            + 'Did you mean "' + closest[0] + '"'
    else:
        msg = untamed.terms[closest[0]]
    await ctx.send(msg)


# Lists factions
@bot.command()
async def factions(ctx):
    L = []
    for key in untamed.factions.keys():
        L.append(untamed.factions[key]['discord_emoji'] \
            + ' ' + untamed.factions[key]['name'])
    msg = 'Available factions are:\n' \
        + '\n'.join(L)
    await ctx.send(msg)
    
    
# Lists card in the chosen faction
@bot.command()
async def faction(ctx, name : str):
    closest = process.extractOne(name.lower(), untamed.factions.keys())
    if closest[1] < 75:
        msg = 'Could not recognize faction "' + name + '".\n' \
            + 'Type "!factions" for a full list of factions.'
    else:
        name = closest[0]
        L = []
        for key in untamed.cards.keys():
            if untamed.cards[key]['faction'].lower() == name:
                card = untamed.cards[key]
                L.append(tools.print_card_short(card))
        msg = name + ' faction contains the cards:\n' \
            + '\n'.join(L)
    await ctx.send(msg)


# Searches for cards satisfying the parameters
@bot.command()
async def search(ctx, *query : str):
    # Display syntax guide
    if query[0].lower() in ["help", "syntax", "guide"]:
        msg = '```\n' \
            + 'Search Syntax Guide:\n' \
            + ' f:<faction>\n' \
            + ' t:<type>\n' \
            + ' x:<body text>, use \'\' if the search string has spaces. "" doesn\'t work!\n' \
            + '\n' \
            + 'For example try "!search x:\'last words\'" or "!search f:rabbit t:item".\n' \
            + '```'
        await ctx.send(msg)
        return

    # Query code mapper
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
            'strictness': 100}}

    # Process query
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

    # Display results
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


# Looks up the chosen card
@bot.command()
async def card(ctx, *name : str):
    name = ' '.join(name)
    closest = process.extractOne(name.lower(), untamed.cards.keys())
    if closest[1] < 75 and name.lower() != "what the hell":
        msg = 'Could not find card "' + name + '"\n' \
            + 'Did you mean "' + closest[0] + '"'
    elif name.lower() == "what the hell":
        card = untamed.cards['whitefur infantry']
        msg = tools.print_card(card)
    else:
        card = untamed.cards[closest[0]]
        msg = tools.print_card(card)      
    await ctx.send(msg)


# Run bot
bot.run(token)



