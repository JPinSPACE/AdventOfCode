""" Solution to the second puzzle of Day 21 on adventofcode.com
"""

def main():
    """ I hate this game!
    """

    b_start_hp = 109
    b_dmg = 8
    b_arm = 2


    weapons = {
        'dagger' : {
            'cost' : 8,
            'dmg' : 4
        },
        'shortsword' : {
            'cost' : 10,
            'dmg' : 5
        },
        'warhammer' : {
            'cost' : 25,
            'dmg' : 6
        },
        'longsword' : {
            'cost' : 40,
            'dmg' : 7
        },
        'greataxe' : {
            'cost' : 74,
            'dmg' : 8
        }
    }

    armors = {
        'no_armor' : {
            'cost' : 0,
            'arm' : 0
        },
        'leather' : {
            'cost' : 13,
            'arm' : 1
        },
        'chainmail' : {
            'cost' : 31,
            'arm' : 2
        },
        'splintmail' : {
            'cost' : 53,
            'arm' : 3
        },
        'bandedmail' : {
            'cost' : 75,
            'arm' : 4
        },
        'platemail' : {
            'cost' : 102,
            'arm' : 5
        }
    }

    rings = {
        'no_ring' : {
            'cost' : 0,
            'points' : 0
        },
        'dmg_1' : {
            'cost' : 25,
            'points' : 1
        },
        'dmg_2' : {
            'cost' : 50,
            'points' : 2
        },
        'dmg_3' : {
            'cost' : 100,
            'points' : 3
        },
        'def_1' : {
            'cost' : 20,
            'points' : -1
        },
        'def_2' : {
            'cost' : 40,
            'points' : -2
        },
        'def_3' : {
            'cost' : 80,
            'points' : -3
        }
    }

    worst_loadout = []
    worst_price = 0
    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring2 == ring1:
                        continue
                    price = weapons[weapon]['cost'] + \
                            armors[armor]['cost'] + \
                            rings[ring1]['cost'] + \
                            rings[ring2]['cost']

                    player = {
                        'hp' : 100,
                        'dmg' : weapons[weapon]['dmg'],
                        'arm' : armors[armor]['arm']
                    }

                    if rings[ring1]['points'] > 0:
                        player['dmg'] += rings[ring1]['points']
                    else:
                        player['arm'] -= rings[ring1]['points']

                    if rings[ring2]['points'] > 0:
                        player['dmg'] += rings[ring2]['points']
                    else:
                        player['arm'] -= rings[ring2]['points']

                    b_hp = b_start_hp
                    while player['hp'] > 0:
                        b_hp -= max(1, (player['dmg']-b_arm))

                        if b_hp <= 0:
                            break

                        player['hp'] -= max(1, (b_dmg-player['arm']))

                    if player['hp'] <= 0 and price >= worst_price:
                        print 'player', player['hp'], 'boss', b_hp
                        worst_loadout = [weapon, armor, ring1, ring2]
                        worst_price = price
                        print worst_price, worst_loadout

    print '*' * 30
    print worst_price, worst_loadout







if __name__ == '__main__':
    main()

