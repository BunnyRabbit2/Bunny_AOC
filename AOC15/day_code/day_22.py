import os
import errno
from sys import maxsize

try:
    os.makedirs("output/d22/")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

p1_min_mana = maxsize
p2_min_mana = maxsize
final_spell_used = []
magic_short = {
    "Magic_Missile": "MM",
    "Drain": "DD",
    "Recharge": "RE",
    "Shield": "SH",
    "Poison": "PP"
}


def solve():
    file_loc = "inputs/day22.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)


def load_inputs(file_location):
    if os.path.exists(file_location):
        file = open(file_location)
        return file.read().split('\n')
    else:
        print("Day 22 input file does not exist")


def create_game_data(inputs):
    boss = {}
    magic = {}

    for i in range(len(inputs)):
        if 'BOSS START' in inputs[i]:
            boss["hp"] = int(inputs[i+1].split(': ')[1])
            boss["dam"] = int(inputs[i+2].split(': ')[1])

        if 'MAGIC START' in inputs[i]:
            mC = 1
            m = inputs[i+mC]
            while not m == 'END':
                mS = m.split()
                magic.setdefault(mS[0], {})
                magic[mS[0]]['cost'] = int(mS[1])

                first_e = mS[2].split('->')
                magic[mS[0]][first_e[0]] = int(first_e[1])
                if len(mS) > 3:
                    second_e = mS[3].split('->')
                    magic[mS[0]][second_e[0]] = int(second_e[1])
                mC += 1
                m = inputs[i+mC]

    return (boss, magic)


def fight(boss_hp, boss_dmg, player_hp, player_mana, magic, next_spell, file, mana_used=0, spells_used='', shield=0, poison=0, recharge=0, hard_mode=False):
    m = magic[next_spell]

    # PLAYER TURN

    if hard_mode:
        player_hp -= 1
        if player_hp <= 0:
            return

    playerA = 0

    if shield > 0:
        playerA = magic['Shield']['ARM']
        shield -= 1

    if poison > 0:
        boss_hp -= magic['Poison']['DAM']
        poison -= 1

    if recharge > 0:
        player_mana += magic['Recharge']['MANA']
        recharge -= 1

    global magic_short
    spells_used += magic_short[next_spell] + ' -> '

    player_mana -= m['cost']
    mana_used += m['cost']

    if 'EFFECT' in m:
        if 'DAM' in m and poison <= 0:
            poison = m['EFFECT']
        elif 'ARM' in m and shield <= 0:
            shield = m['EFFECT']
        elif 'MANA' in m and recharge <= 0:
            recharge = m['EFFECT']
    else:
        if 'DAM' in m:
            boss_hp -= m['DAM']
        if 'HEAL' in m:
            player_hp += m['HEAL']

    # BOSS TURN

    if shield > 0:
        playerA = magic['Shield']['ARM']
        shield -= 1
    else:
        playerA = 0

    if poison > 0:
        boss_hp -= magic['Poison']['DAM']
        poison -= 1

    if recharge > 0:
        player_mana += magic['Recharge']['MANA']
        recharge -= 1

    player_hp -= boss_dmg - playerA

    global p1_min_mana

    if player_hp <= 0:
        return
    if boss_hp <= 0:
        global final_spell_used
        spells_used = 'FINAL -  PlayerHP: ' + str(player_hp) + '\tBossHP: ' + str(
            boss_hp) + '\tManaUsed: ' + str(mana_used) + '\tSpells: ' + spells_used[:-3]
        file.write(spells_used + '\n')
        if mana_used < p1_min_mana:
            p1_min_mana = mana_used
        return

    for mk in magic.keys():
        if magic[mk]['cost'] < player_mana and mana_used < p1_min_mana:
            fight(boss_hp, boss_dmg, player_hp, player_mana, magic, mk, file,
                  mana_used, spells_used, shield, poison, recharge, hard_mode)


def solve_puzzle_1(file_location):
    inputs = load_inputs(file_location)

    DATA = create_game_data(inputs)
    boss = DATA[0]
    magic = DATA[1]
    player = {'hp': 50, 'mana': 500}

    # boss['hp'] = 10

    file_path_out = 'output/d22/output_fight.txt'
    os.makedirs(os.path.dirname(file_path_out), exist_ok=True)
    if os.path.exists(file_path_out):
        os.remove(file_path_out)
    file = open(file_path_out, "a+")
    for mk in magic.keys():
        fight(boss['hp'], boss['dam'], player['hp'],
              player['mana'], magic, mk, file)
    file.close()

    output = p1_min_mana

    print(f'Day 22 Puzzle 1 Solution - {output}')
    global final_spell_used

    file = open("output/d22/output.txt", "w+")
    for r in final_spell_used:
        file.write(r + '\n')
    file.close()


def solve_puzzle_2(file_location):
    inputs = load_inputs(file_location)

    DATA = create_game_data(inputs)
    boss = DATA[0]
    magic = DATA[1]
    player = {'hp': 50, 'mana': 500}

    # boss['hp'] = 10

    file_path_out = 'output/d22/output_fightp2.txt'
    if os.path.exists(file_path_out):
        os.remove(file_path_out)
    file = open(file_path_out, "a+")
    for mk in magic.keys():
        fight(boss['hp'], boss['dam'], player['hp'],
              player['mana'], magic, mk, file, hard_mode=True)
    file.close()

    output = p1_min_mana

    print(f'Day 22 Puzzle 2 Solution - {output}')
    global final_spell_used

    file = open("output/d22/outputp2.txt", "w+")
    for r in final_spell_used:
        file.write(r + '\n')
    file.close()
