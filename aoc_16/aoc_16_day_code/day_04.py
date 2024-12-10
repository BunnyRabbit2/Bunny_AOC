"""Code to solve puzzle for day 04"""
import os
import errno

try:
    os.makedirs("output/y16d04/")
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

def solve():
    """Solves the day"""
    file_loc = "inputs/day04.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC16_INPUT_DAY04':
            print("Invalid input file header: Day04")
            return ''
     
        return input_file.read()
    else:
        print("Day 04 input file does not exist")
        return ''
def generate_rooms_information(room_list: list[str]):
    rooms_info = []

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for room in room_list:
        room_name, rest = room.rsplit('-',1)

        sector_id, checksum = rest.split('[')

        sector_id = int(sector_id)

        checksum = checksum.replace(']','')

        letters_contained = {c for c in room_name.replace('-','')}

        letter_count = [(c,room_name.count(c)) for c in letters_contained]

        letter_count = sorted(letter_count, key = lambda l: (-l[1], l[0]))

        decrypted_room_name = ''

        for c in room_name:
            if c in alphabet:
                decrypted_room_name += alphabet[(alphabet.find(c) + sector_id) % 26]
            else:
                decrypted_room_name += c

        rooms_info.append({
            'room_name': room_name,
            'decrypted_room_name': decrypted_room_name,
            'sector_id': sector_id,
            'checksum': checksum,
            'letter_count': letter_count
        })

    return rooms_info

def get_test_rooms():
    return [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]'
    ]

def write_room_names(rooms):
    file_path_out = 'output/y16d04/output_room_names.txt'
    os.makedirs(os.path.dirname(file_path_out), exist_ok=True)
    if os.path.exists(file_path_out):
        os.remove(file_path_out)
    file = open(file_path_out, "a+")
    for r in rooms:
        file.write(f'{r['sector_id']} | {r['decrypted_room_name']}\n')
    file.close()

def is_real_room(room_info):
    generated_checksum = ''.join([c[0] for c in room_info['letter_count'][0:5]])

    return generated_checksum == room_info['checksum']

def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 04 Puzzle 1 - NO INPUTS")
    else:
        rooms_info = generate_rooms_information(inputs.split('\n'))
        
        output = sum([r['sector_id'] if is_real_room(r) else 0 for r in rooms_info])

        print("Day 04 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 04 Puzzle 2 - NO INPUTS")
    else:
        rooms_info = generate_rooms_information(inputs.split('\n'))

        valid_rooms = [r for r in rooms_info if is_real_room(r)]

        write_room_names(valid_rooms)

        output = [r['sector_id'] for r in valid_rooms if 'north' in r['decrypted_room_name']][0]

        print("Day 04 Puzzle 2 Solution - " + str(output))
    