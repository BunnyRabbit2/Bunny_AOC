"""Code to solve puzzle for day 07"""
import os
import re

def solve():
    """Solves the day"""
    file_loc = "inputs/day07.txt"
    solve_puzzle_1(file_loc)
    solve_puzzle_2(file_loc)

def load_inputs(file_location):
    """Loads the input file"""
    if os.path.exists(file_location):
        input_file = open(file_location)
        first_line = input_file.readline().strip()
        if not first_line == 'AOC16_INPUT_DAY07':
            print("Invalid input file header: Day07")
            return ''
     
        return input_file.read()
    else:
        print("Day 07 input file does not exist")
        return ''
    
def get_test_data():
    return [
        'abba[mnop]qrst',
        'abcd[bddb]xyyx',
        'aaaa[qwer]tyui',
        'ioxxoj[asdfgh]zxcvbn'
    ]

def ip_has_tls(ip_string):
    abba_match = re.compile(r'(\w)(?!\1)(\w)\2\1')
    hnet_grabber = re.compile(r'\[\w*\]')

    snet_seqs = hnet_grabber.sub(' ', ip_string).split()
    hnet_seqs = hnet_grabber.findall(ip_string)

    has_abba = any([abba_match.search(i) for i in snet_seqs])
    hnet_has_abba = any([abba_match.search(h) for h in hnet_seqs])
    
    has_tls = has_abba and not hnet_has_abba
    
    return has_tls

def ip_has_ssl(ip_string):
    aba_match = re.compile(r'(\w)(?!\1)\w\1')
    hnet_grabber = re.compile(r'\[\w*\]')

    snet_seqs = hnet_grabber.sub(' ', ip_string).split()
    hnet_seqs = hnet_grabber.findall(ip_string)

    snet_abas = [aba_match.search(i) for i in snet_seqs]
    babs = []

    for s in snet_abas:
        if s is None:
            continue
        aba = s.group(0)
        babs.append(aba[1] + aba[0] + aba[1])

    snet_has_aba = any(snet_abas)

    if snet_has_aba:
        hnet_has_bab = any([any([bab in h for bab in babs]) for h in hnet_seqs])

        return hnet_has_bab
    return False


def solve_puzzle_1(file_location):
    """Solves puzzle 1 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 07 Puzzle 1 - NO INPUTS")
    else:
        ip_addrs = inputs.split('\n')

        # ip_addrs = get_test_data()

        ips_with_tls = [s for s in ip_addrs if ip_has_tls(s)]

        output = len(ips_with_tls)

        print("Day 07 Puzzle 1 Solution - " + str(output))

def solve_puzzle_2(file_location):
    """Solves puzzle 2 for the day"""
    inputs = load_inputs(file_location)
    if inputs == '':
        print("Day 07 Puzzle 2 - NO INPUTS")
    else:
        ip_addrs = inputs.split('\n')

        # ip_addrs = get_test_data()

        ips_with_ssl = [s for s in ip_addrs if ip_has_ssl(s)]

        output = len(ips_with_ssl)

        print("Day 07 Puzzle 2 Solution - " + str(output))
    