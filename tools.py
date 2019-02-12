import untamed

def factionemoji(card):
    return untamed.factions[card['faction'].lower()]['discord_emoji']

def print_card_short(card):
    msg = factionemoji(card) + ' ' + card['name'] + ', ' + card['type']
    return msg

def print_card(card):
    msg = card['name'] + ', ' + factionemoji(card) + ' ' + card['faction'] + ' faction' + '\n' \
            + card['type'] + (', cost: ' + str(card['cost']) if card['cost'] is not None else '') + '\n' \
            + ('Power: ' + str(card['power']) + ', ' if card['power'] is not None else '') \
            + ('Health: ' + str(card['health']) + '\n' if card['health'] is not None else '') \
            + card['text']
    return msg
