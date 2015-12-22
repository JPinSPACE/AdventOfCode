""" Solution to the second puzzle of Day 22 on adventofcode.com
"""
from random import randrange

SPELLS = {
    'magic_missile' : {
        'mana' : 53,
        'heal' : 0,
        'dmg' : 4,
        'turns' : 0
    },
    'drain' : {
        'mana' : 73,
        'heal' : 2,
        'dmg' : 2,
        'turns' : 0
    },
    'shield' : {
        'mana' : 113,
        'add_mana' : 0,
        'dmg' : 0,
        'turns' : 6
    },
    'poison' : {
        'mana' : 173,
        'add_mana' : 0,
        'dmg' : 3,
        'turns' : 6
    },
    'recharge' : {
        'mana' : 229,
        'add_mana' : 101,
        'dmg' : 0,
        'turns' : 5
    }
}

START = {
    'player_hp' : 50,
    'player_mana' : 500,
    'boss_hp' : 58,
    'boss_dmg' : 9
}

def main():
    """ Hard Wizard Duel!
    """

    best = {
        'mana' : 99999,
        'final_bhp': 0,
        'final_php': 0
    }

    for _ in range(100000):
        player = {
            'hp' : START['player_hp'],
            'mana' : START['player_mana']
        }
        boss = {
            'hp' : START['boss_hp'],
            'dmg' : START['boss_dmg']
        }

        effects = []

        mana_spent = 0

        while True:
            player['hp'] -= 1

            new_effects = []
            for effect in effects:
                boss['hp'] -= SPELLS[effect['name']]['dmg']
                player['mana'] += SPELLS[effect['name']]['add_mana']

                new_effects.append({'name' : effect['name'],
                                    'turns' : effect['turns'] - 1
                                   })
            effects = [ new for new in new_effects if new['turns'] > 0 ]

            # check the player hp here so I don't need to
            # piss off pylint with another branch
            if boss['hp'] <= 0 or player['hp'] <= 0:
                break

            # player turn, choose new spell
            new_spell = SPELLS.keys()[randrange(len(SPELLS))]
            while new_spell in [effect['name'] for effect in effects]:
                new_spell = SPELLS.keys()[randrange(len(SPELLS))]

            if player['mana'] - SPELLS[new_spell]['mana'] < 0 or \
               mana_spent + SPELLS[new_spell]['mana'] >= best['mana']:
                break

            player['mana'] -= SPELLS[new_spell]['mana']

            mana_spent += SPELLS[new_spell]['mana']

            if SPELLS[new_spell]['turns'] == 0:
                boss['hp'] -= SPELLS[new_spell]['dmg']
                player['hp'] += SPELLS[new_spell]['heal']
            else:
                effects.append({'name' : new_spell,
                                'turns' : SPELLS[new_spell]['turns']
                               })

            if boss['hp'] <= 0:
                break

            # effects on boss turn
            new_effects = []
            for effect in effects:
                boss['hp'] -= SPELLS[effect['name']]['dmg']
                player['mana'] += SPELLS[effect['name']]['add_mana']

                new_effects.append({'name' : effect['name'],
                                    'turns' : effect['turns'] - 1
                                   })
            effects = [ new for new in new_effects if new['turns'] > 0 ]

            if boss['hp'] <= 0:
                break

            shield = 7 if 'shield' in [eff['name'] for eff in effects] else 0

            player['hp'] -= max(1, boss['dmg'] - shield)

            if player['hp'] <= 0:
                break

        best['mana'] = mana_spent if boss['hp'] <= 0 and \
                                     mana_spent <= best['mana'] \
                                  else best['mana']


    print best['mana']
    assert best['mana'] == 1309


if __name__ == '__main__':
    main()

