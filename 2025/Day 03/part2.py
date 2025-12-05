import os
from typing import List

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 03"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar: List[str] = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    ans = 0

    for line in ar:
        # Start from the very end and take exactly 12 digits. Now, move left and try to take the next max for the very first index 
        # and see that former first one can be given to the second one and so on.

        # Create a list to hold 12 digits which needs to be activated.
        selected_idx: List[int] = list(range(len(line) - 12, len(line)))
        end_idx = len(line) - 13

        def handle_chain_reaction(new_idx: int) -> None:
            '''
            Recursively checks if the new index can be used instead of the old index. Give prev old index to the next old index.
            
            :param new_idx: New index to replace with the very first selected index.
            '''
            for old_idx in range(12):
                if int(line[new_idx]) < int(line[selected_idx[old_idx]]):
                    break
                selected_idx[old_idx], new_idx = new_idx, selected_idx[old_idx]

        # Now, traverse left and see if any new value can be assigned to the first idx value. It can only be assigend if it's greater
        # or equal.
        while end_idx >= 0:
            # Cannot be assigned
            if int(line[end_idx]) < int(line[selected_idx[0]]):
                end_idx -= 1
                continue

            # Current number can be given to the first idx. This will trigger a chain reaction.
            handle_chain_reaction(end_idx)

            end_idx -= 1
    
        # Now, generate the sequence.
        joltage: int = ''
        for idx in range(len(line)):
            if idx in selected_idx:
                joltage += line[idx]
        
        ans += int(joltage)
        
    return ans

for name in FILE_NAMES:
    print(name, solve(name))
