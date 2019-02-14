# untamed card llibrary

terms = {
    'animal':"Animal - Card type. Animals are placed on the table in the Exhausted position when played, and thus cannot attack on the turn that they were played. Animals have Power Cost (blue icon), Attack (red flame icon) and Health (green shield icon) values, as well as one or more special abilities. Animals can attack other Animals or the opponent's Stronghold.",
    'arrive':"Arrive - Card Ability. This effect happens when an Animal comes into play. A player can also decide not to use the Arrive effect.",
    'elite':"Elite - An indicator on a card. A player checks if the 2 cards they draw when their Stronghold is defeated has the Elite written on it. If so that card may immediately be played without having to pay the card?s Power Cost.",
    'favor token':"Favor Token - Token that can grant, Guard, Surge or Sneak to an Animal when it's played. Each player starts the game with one token of each type. Removed from the game after they've been used.",
    'fury':"Fury - Token. A token that grants the Animal it is placed on +1 Attack for as long as the token is on the Animal.",
    'guard':"Guard - Card Ability. This Animal must first be defeated before other Animals or Strongholds can be attacked. When multiple Animals with Guard are on the board, the attacker may choose one of them to attack. Guard does not affect Items and Animal/Stronghold card effects. A player can grant an Animal Guard by spending the appropriate Favor token when playing the Animal.",
    'item':"Item - Card type. Items have a single use effect and are placed into their owner's Stronghold after they are resolved.",
    'inspire':"Inspire - Card Ability. While playing the card, players may pay the stated Support cost to get a bonus or stronger Arrive effect. Paying the Support cost is optional, all support costs are paid before the effect is resolved.",
    'last words':"Last Words - Card Ability. This effect happens when an Animal is defeated.",
    'power': "Power - Any card that is placed face down in a Player's playing area Power. Players may only play a single card as a Power per turn and can have a maximum of 10 Power.",
    'reveal':"Reveal - Action. When a card states to reveal a card, the player shows the card to the other player, then puts the card back where it came from. If multiple cards were revealed from the top of a player's deck, put it back in the same order.",
    'sneak':"Sneak - Card Ability. Animals with this ability come into play in the Sneak Position (upside down). Animals in the Sneak position cannot be attacked until it's controller attacks with it, and thus moves it to the Exhausted position. Animals in the Sneak position cannot be targeted by Items and abilities by either player. A player can grant an Animal Sneak by spending the appropriate Favor token when playing the Animal.",
    'surge':"Surge - Card Ability. Animals with this ability come into play in the Ready Position and may immediately be used the turn it's played to attack the opponents Animals. It cannot however attack the opponent's Stronghold on the same turn it was played. A player can grant an Animal Surge by spending the appropriate Favor token when playing the Animal.",
    'void':"Void - Zone. Place cards in the Void somewhere away from the playing area. Cards in the Void are effectively out of the game until a player's deck is empty. If a player's deck is empty, the Void is reshuffled to form a new deck. If a player's deck is empty for a second time, that player loses the game."}

factions = {
    'rabbit': {
        'name': 'Rabbit',
        'discord_emoji': '<:untamedrabbit:544906418436964353>'}, #':rabbit:'},
    'panda': {
        'name': 'Panda',
        'discord_emoji': '<:untamedpanda:544906418394759179>'}, #':panda_face:'},
    'crocodile': {
        'name': 'Crocodile',
        'discord_emoji': '<:untamedcrocodile:544906418705399828>'}, #':crocodile:'},
    'fox': {
        'name': 'Fox',
        'discord_emoji': '<:untamedfox:544906418843680768>'}, #':fox:'},
    'rhino': {
        'name': 'Rhino',
        'discord_emoji': '<:untamedrhino:544906418671583233>'}, #':rhino:'},
    'chameleon': {
        'name': 'Chameleon',
        'discord_emoji': '<:untamedchameleon:544906418936086558>'}}#':frog:'}}

cards = {
    'general greycoat': {
        'name': 'General Greycoat',
        'type': 'animal',
        'faction': 'Rabbit',
        'cost': 5,
        'power': 6,
        'health': 4,
        'text': 'Arrive: Choose one: give another Animal 2 Fury OR copy the Arrive ability of a friendly Animal. You may Pay 5 Support to do both.',
        'img': None},
    'whitefur bombardier': {
        'name': 'Whitefur Bombardier',
        'type': 'animal (elite)',
        'faction': 'Rabbit',
        'cost': 2,
        'power': 2,
        'health': 3,
        'text': 'Arrive: Choose one: Deal 1 damage to an Animal OR Stronghold. You may Pay 2 Support to do both.',
        'img': None},
    'war council': {
        'name': 'War Council',
        'type': 'animal (elite)',
        'faction': 'Rabbit',
        'cost': 3,
        'power': 3,
        'health': 5,
        'text': 'Arrive: You may return a friendly Animal to your hand. Last Words: Give an Animal 1 Fury.',
        'img': None},
    'carrot saber': {
        'name': 'Carrot Saber',
        'type': 'item',
        'faction': 'Rabbit',
        'cost': 3,
        'power': None,
        'health': None,
        'text': 'Deal 2 damage to an Animal. You may Pay 4 Support. If you do, deal 2 damage to all enemy Animals instead.',
        'img': None},
    'elite infantry': {
        'name': 'Elite Infantry',
        'type': 'animal (elite)',
        'faction': 'Rabbit',
        'cost': 1,
        'power': 2,
        'health': 1,
        'text': 'Arrive: Choose one: This may attack immediately OR This gains 1 Fury. You may Pay 2 Support to do both.',
        'img': None},
    'whitefur command': {
        'name': 'Whitefur Command',
        'type': 'stronghold',
        'faction': 'Rabbit',
        'cost': None,
        'power': None,
        'health': 12,
        'text': 'Pay 4 Support: Deal 1 damage to an Animal OR Stronghold.',
        'img': None},
    'blackstone vault': {
        'name': 'Blackstone Vault',
        'type': 'stronghold',
        'faction': 'Panda',
        'cost': None,
        'power': None,
        'health': 12,
        'text': 'Pay 3 support: Draw a card.',
        'img': None},
    'ursan gambler': {
        'name': 'Ursan Gambler',
        'type': 'animal (elite)',
        'faction': 'Panda',
        'cost': 1,
        'power': 1,
        'health': 2,
        'text': 'Arrive: Put the top 2 cards of your deck into your Stronghold. If there was a Panda among them, this gains 2 Fury.',
        'img': None},
    'radann, merchant-king': {
        'name': 'Radann, Merchant-King',
        'type': 'animal',
        'faction': 'Panda',
        'cost': 5,
        'power': 4,
        'health': 6,
        'text': 'You may Pay 5 Support instead of paying this card\'s Power cost. Last Words: Trigger your Stronghold ability for free.',
        'img': None},
    'blackstone broker': {
        'name': 'Blackstone Broker',
        'type': 'animal (elite)',
        'faction': 'Panda',
        'cost': 2,
        'power': 2,
        'health': 3,
        'text': 'Whenever you use your Stronghold ability, this gains 1 Fury.',
        'img': None},
    'oromancer': {
        'name': 'Oromancer',
        'type': 'animal (elite)',
        'faction': 'Panda',
        'cost': 3,
        'power': 3,
        'health': 4,
        'text': 'Whenever you use your Stronghold ability, deal 1 damage to a Stronghold. Last Words: Put the top 2 cards of your deck into your Stronghold.',
        'img': None},
    'blackstone treasury': {
        'name': 'Blackstone Treasury',
        'type': 'item',
        'faction': 'Panda',
        'cost': 3,
        'power': None,
        'health': None,
        'text': 'You may Pay 5 Support instead of paying this card\'s Power Cost',
        'img': None},
    'goldscale temple': {
        'name': 'Goldscale Temple',
        'type': 'Stronghold',
        'faction': 'Crocodile',
        'cost': None,
        'power': None,
        'health': 12,
        'text': 'Pay 3 Support: Trigger the Last Words ability of an Animal in play.',
        'img': None},
    'toothblade magus': {
        'name': 'Toothblade Magus',
        'type': 'animal (elite)',
        'faction': 'Crocodile',
        'cost': 2,
        'power': 3,
        'health': 2,
        'text': 'Arrive: You may Pay 2 Support. If you do, this gains 1 Fury. Last Words: Deal 3 damage to a Stronghold.',
        'img': None},
    'high-priestess mekhet': {
        'name': 'High-Priestess Mekhet',
        'type': 'animal',
        'faction': 'Crocodile',
        'cost': 4,
        'power': 5,
        'health': 5,
        'text': 'Arrive: You may Pay 5 Support. If you do, all your Animals with Last Words get +2 Attack until end of turn. Last Words: Draw a card.',
        'img': None},
    'goldscale archer': {
        'name': 'Goldscale Archer',
        'type': 'animal (elite)',
        'faction': 'Crocodile',
        'cost': 1,
        'power': 2,
        'health': 1,
        'text': 'LAST WORDS: Deal 1 Damage to an Animal.',
        'img': None},
    'toothblade chosen': {
        'name': 'Toothblade Chosen',
        'type': 'animal (elite)',
        'faction': 'Crocodile',
        'cost': 4,
        'power': 3,
        'health': 5,
        'text': 'Arrive: For each Animal in your Stronhgold with Last Words, this gains 1 Fury. GUARD.',
        'img': None},
    'goldscale amulet': {
        'name': 'Goldscale Amulet',
        'type': 'item',
        'faction': 'Crocodile',
        'cost': 1,
        'power': None,
        'health': None,
        'text': 'Look at the top card of your deck, you may put it into your Stronghold. Pay 3 Supprt: Trigger the Last Words abilities of up to 2 Animals in your Stronghold.',
        'img': None},
    'spiritsong lodge': {
        'name': 'Spiritsong Lodge',
        'type': 'stronghold',
        'faction': 'Rhino',
        'cost': None,
        'power': None,
        'health': 12,
        'text': 'Pay 2 Support: Give 1 Fury to an Animal.',
        'img': None},
    'rockhide berserker': {
        'name': 'Rockhide Berserker',
        'type': 'animal (elite)',
        'faction': 'Rhino',
        'cost': 2,
        'power': 2,
        'health': 3,
        'text': 'Arrive: If any of your Animals is damaged, this gains 2 Fury. Each time this takes damage, place the top card of your deck into your Stronghold.',
        'img': None},
    'wildcaller mo\'gara': {
        'name': 'Wildcaller Mo\'Gara',
        'type': 'animal',
        'faction': 'Rhino',
        'cost': 3,
        'power': 3,
        'health': 2,
        'text': 'Arrive: Move 1 Damage from an Animal to another Animal. If that kills it: thius gains 1 Fury. You may Pay 2 Support, if you do, move 2 Damage instead.',
        'img': None},
    'rockhide defender': {
        'name': 'Rockhide Defender',
        'type': 'animal (elite)',
        'faction': 'Rhino',
        'cost': 3,
        'power': 2,
        'health': 4,
        'text': 'Each time this takes damage, this gains 1 Fury. GUARD',
        'img': None},
    'the bonehammer': {
        'name': 'The Bonehammer',
        'type': 'item (elite)',
        'faction': 'Rhino',
        'cost': 4,
        'power': None,
        'health': None,
        'text': 'You may Pay 5 Support instead of paying this card\'s Power cost. Deal 2 damagew each to 2 Animals.',
        'img': None},
    'war drums': {
        'name': 'War Drums',
        'type': 'item',
        'faction': 'Rhino',
        'cost': 1,
        'power': None,
        'health': None,
        'text': 'Heal an Animal or Stronghold for 2. Pay 2 Support: Move 1 Damage from an Animal to another Animal. This may be done before healing an Animal.',
        'img': None},
    'the dark tower': {
        'name': 'The Dark Tower',
        'type': 'stronghold',
        'faction': 'Fox',
        'cost': None,
        'power': None,
        'health': 12,
        'text': 'Pay 4 Support: Reveal the top card of your deck. If it\'s an Animal, give an Animal -2 Atack until end of turn. If it\'s an Item, draw it.',
        'img': None},
    'spymaster rohana': {
        'name': 'Spymaster Rohana',
        'type': 'animal',
        'faction': 'Fox',
        'cost': 4,
        'power': 3,
        'health': 4,
        'text': 'Arrive: Reveal the top 2 cards of your deck. Deal damage to a Stronghold equal to the highest cost card revealed. Gain Fury equal to the lowest cost card revealed.',
        'img': None},
    'reinhard thief': {
        'name': 'Reinhard Theif',
        'type': 'animal (elite)',
        'faction': 'Fox',
        'cost': 1,
        'power': 1,
        'health': 2,
        'text': 'Arrive: Put a card from your Stronghold on top of your deck. You may Pay 2 Support. If you do, give an Animal -2 Attack until end of turn.',
        'img': None},
    'scheming seer': {
        'name': 'Scheming Seer',
        'type': 'animal (elite)',
        'faction': 'Fox',
        'cost': 3,
        'power': 3,
        'health': 4,
        'text': 'Arrive: You may Pay 2 Support. If you do, reveal the top card of your deck. If it\'s an Animal, the next Animal you play this turn costs 2 Power less. Otherwise, gain 1 Fury.',
        'img': None},
    'spyglass': {
        'name': 'Spyglass',
        'type': 'item (elite)',
        'faction': 'Fox',
        'cost': 0,
        'power': None,
        'health': None,
        'text': 'Reveal the top 2 cards of your deck, put them back on the top or the bottom of your deck in any order. If you revealed at least 1 Animal, put 1 Fury on an Animal.',
        'img': None},
    'hidden blade': {
        'name': 'Hidden Blade',
        'type': 'item',
        'faction': 'Fox',
        'cost': 2,
        'power': None,
        'health': None,
        'text': 'Deal 2 Damage to an Animal. You may Pay 4 Support. If you do, move any Fury on the targeted Animal to a another Animal.',
        'img': None},
    'the laboratory': {
        'name': 'The Laboratory',
        'type': 'stronghold',
        'faction': 'Chameleon',
        'cost': None,
        'power': None,
        'health': 12,
        'text': 'Pay 4 Support: You may play an Item from your Stronghold as if it was in your hand. Then, put that Item in your Void.',
        'img': None},
    'dr. dolores': {
        'name': 'Dr. Dolores',
        'type': 'animal',
        'faction': 'Chameleon',
        'cost': 4,
        'power': 4,
        'health': 5,
        'text': 'Arrive: You may Pay 4 Support. If you do, return an Item from your Stronghold to your hand. \nWhenever you play or discard an Item, deal 1 damage to an Animal and this gains 1 Fury.',
        'img': None},
    'shiftscale assassin': {
        'name': 'Shiftscale Assassin',
        'type': 'animal (elite)',
        'faction': 'Chameleon',
        'cost': 1,
        'power': 1,
        'health': 2,
        'text': 'Whenever the deals damage to an Animal, destroy that Animal. Last Words: Draw a card, then discard a card.',
        'img': None},
    'lab deceptionist': {
        'name': 'Lab Deceptionist',
        'type': 'animal (elite)',
        'faction': 'Chameleon',
        'cost': 2,
        'power': 3,
        'health': 2,
        'text': 'Arrive: Draw a card, then discard a card. Deal 1 damage to an Animal. If the discarded card was an Itewm, deal 3 Damage instead.',
        'img': None},
    'expert alchemist': {
        'name': '"Expert" Alchemist',
        'type': 'animal (elite)',
        'faction': 'Chameleon',
        'cost': 3,
        'power': 2,
        'health': 5,
        'text': 'Arrive: Draw a card, then discard a card. Deal 3 Damage to a Stronghold, and 1 damage to this. If the discarded card was an item, this gains 1 Fury.',
        'img': None},
    'vile concoction': {
        'name': 'Vile Concoction',
        'type': 'item',
        'faction': 'Chameleon',
        'cost': 3,
        'power': None,
        'health': None,
        'text': 'Deal 2 damage to a Stronghold OR deal damage equal to the amount of Items in your Stronghold. You may Pay 4 Support: Also give an Animal that much Attack until end of turn.',
        'img': None}}
        
