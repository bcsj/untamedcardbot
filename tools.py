import untamed

def factionemoji(card):
    return untamed.factions[card['faction'].lower()]['discord_emoji']

def print_card_short(card):
    msg = factionemoji(card) + ' ' + card['name'] + ', ' + card['type']
    return msg

def print_card(card):
    #cost_emoji = '<:cost:544901369518096384>'
    cost_emoji = '<:cost:544910093637124100>'
    #attk_emoji = '<:attack:544900513490141194>'
    attk_emoji = '<:attack:544910182237339664>'
    #defn_emoji = '<:defense:544900512634372136>'
    defn_emoji = '<:defense:544910145772322816>'
    msg = card['name'] + ', ' + factionemoji(card) + ' ' + card['faction'] + ' faction' + '\n' \
            + card['type'] + (', ' + cost_emoji + ' ' + str(card['cost']) if card['cost'] is not None else '')  \
            + (', ' + attk_emoji + ' ' + str(card['power']) + ', ' if card['power'] is not None else '') \
            + (defn_emoji + ' ' + str(card['health']) + '\n' if card['health'] is not None else '') \
            + card['text']
    return msg
