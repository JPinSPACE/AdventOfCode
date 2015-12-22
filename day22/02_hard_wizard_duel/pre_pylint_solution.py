""" Solution to the second puzzle of Day 22 on adventofcode.com
"""
from random import randrange

def main():
    """ Hard Wizard Duel!
    """

    spells = {
        'magic_missile' : {
            'target' : ['boss'],
            'mana' : 53,
            'add_mana' : 0,
            'heal' : 0,
            'dmg' : 4,
            'arm' : 0,
            'turns' : 0
        },
        'drain' : {
            'target' : ['boss', 'player'],
            'mana' : 73,
            'add_mana' : 0,
            'heal' : 2,
            'dmg' : 2,
            'arm' : 0,
            'turns' : 0
        },
        'shield' : {
            'target' : ['shield'],
            'mana' : 113,
            'add_mana' : 0,
            'heal' : 0,
            'dmg' : 0,
            'arm' : 7,
            'turns' : 6
        },
        'poison' : {
            'target' : ['boss'],
            'mana' : 173,
            'add_mana' : 0,
            'heal' : 0,
            'dmg' : 3,
            'arm' : 0,
            'turns' : 6
        },
        'recharge' : {
            'target' : ['player'],
            'mana' : 229,
            'add_mana' : 101,
            'heal' : 0,
            'dmg' : 4,
            'arm' : 0,
            'turns' : 5
        }
    }

    start = {
        'player_hp' : 50,
        'player_mana' : 500,
        'player_arm' : 0,
        'boss_hp' : 58
    }

    best = {
        'mana' : 99999,
        'actions' : [],
        'final_bhp': 0,
        'final_php': 0
    }

    count = 0
    for _ in range(10000):
        player = {
            'hp' : start['player_hp'],
            'mana' : start['player_mana'],
            'arm' : start['player_arm']
        }
        boss = {
            'hp' : start['boss_hp'],
            'dmg' : 9
        }

        '''
        player = {
            'hp' : 10,
            'mana' : 250,
            'arm' : 0
        }
        boss = {
            'hp' : 14,
            'dmg' : 8
        }
        '''

        actions = []
        effects = []

        mana_spent = 0

        replay = ['poison', 'magic_missile']
        replay = ['recharge', 'shield', 'drain', 'poison', 'magic_missile']
        replay_count = 0
        while True:
            player['hp'] -= 1
            if player['hp'] <= 0:
                break
            shield = 0
            if 'shield' in [effect['name'] for effect in effects]:
                shield = 7
            #print "-- Player turn --"
            #print "- Player has {} hit points, {} armor, {} mana".format(player['hp'], shield, player['mana'])
            #print "- Boss has {} hit points".format(boss['hp'])
            new_effects = []
            for effect in effects:
                if effect['name'] == 'poison':
                    #print "Poison deals 3 damage; its timer is now {}".format(effect['turns'] - 1)
                    boss['hp'] -= 3
                elif effect['name'] == 'recharge':
                    #print "Recharge provides 101 mana; its timer is now {}".format(effect['turns'] - 1)
                    player['mana'] += 101
                elif effect['name'] == 'shield':
                    pass
                    #print "Shield's timer is now {}".format(effect['turns'] - 1)
                else:
                    print "ERROR: Unexpected effect:", effect
                    quit()

                if effect['turns'] > 1:
                    new_effects.append({'name' : effect['name'], 'turns' : effect['turns'] - 1})
                else:
                    pass
                    #print "{} wears off.".format(effect['name'])

            effects = new_effects

            if boss['hp'] <= 0:
                #print "This kills the boss"
                if mana_spent <= best['mana']:
                    best['mana'] = mana_spent
                    best['actions'] = actions[:]
                    best['final_bhp'] = boss['hp']
                    best['final_php'] = player['hp']
                break

            # player turn, choose new spell
            valid_spell = False
            while not valid_spell:
                new_spell = spells.keys()[randrange(len(spells))]
                #new_spell = replay[replay_count]
                if new_spell not in [effect['name'] for effect in effects]:
                    valid_spell = True
            replay_count += 1
            if replay_count > len(replay):
                pass

            if player['mana'] - spells[new_spell]['mana'] < 0:
                break

            player['mana'] -= spells[new_spell]['mana']
            mana_spent += spells[new_spell]['mana']
            if mana_spent >= best['mana']:
                # don't bother, it's too expensive
                break

            if new_spell == 'magic_missile':
                #print "Player casts Magic Missle, dealing 4 damage."
                boss['hp'] -= spells['magic_missile']['dmg']
            elif new_spell == 'drain':
                #print "Player casts Drain, dealing 2 damage and gaining 2 health"
                boss['hp'] -= spells['drain']['dmg']
                player['hp'] += spells['drain']['heal']
            else:
                #print "Player casts {}".format(new_spell)
                effects.append({'name' : new_spell, 'turns' : spells[new_spell]['turns']})
            actions.append(new_spell)

            if boss['hp'] <= 0:
                #print "This kills the boss"
                if mana_spent <= best['mana']:
                    best['mana'] = mana_spent
                    best['actions'] = actions[:]
                    best['final_bhp'] = boss['hp']
                    best['final_php'] = player['hp']
                break

            #print "\n-- Boss turn --"
            #print "- Player has {} hit points, {} armor, {} mana".format(player['hp'], shield, player['mana'])
            #print "- Boss has {} hit points".format(boss['hp'])

            # effects on boss turn
            new_effects = []
            for effect in effects:
                if effect['name'] == 'poison':
                    #print "Poison deals 3 damage; its timer is now {}".format(effect['turns'] - 1)
                    boss['hp'] -= 3
                elif effect['name'] == 'recharge':
                    #print "Recharge provides 101 mana; its timer is now {}".format(effect['turns'] - 1)
                    player['mana'] += 101
                elif effect['name'] == 'shield':
                    pass
                    #print "Shield's timer is now {}".format(effect['turns'] - 1)
                else:
                    print "ERROR: Unexpected effect:", effect
                    quit()

                if effect['turns'] > 1:
                    new_effects.append({'name' : effect['name'], 'turns' : effect['turns'] - 1})
                else:
                    pass
                    #print "{} wears off.".format(effect['name'])

            effects = new_effects

            if boss['hp'] <= 0:
                #print "This kills the boss"
                if mana_spent <= best['mana']:
                    best['mana'] = mana_spent
                    best['actions'] = actions[:]
                break
            # boss turn effect resolution complete

            # calculate current player armor based on shield effects
            shield = 0
            if 'shield' in [effect['name'] for effect in effects]:
                shield = 7

            # boss attacks
            #print "Boss attacks for {} damage.".format(max(1, boss['dmg'] - shield))
            player['hp'] -= max(1, boss['dmg'] - shield)

            # if player is dead, bail
            if player['hp'] <= 0:
                break

            #print





    print '*' * 20
    print best



if __name__ == '__main__':
    main()


