import os
from typing import List
from sortedcontainers import SortedList

FILE_NAMES = ['small', 'large']
YEAR = 2025
DAY = "Day 05"

def solve(filename):
    INPUT_PATH = f'{os.getcwd()}/{YEAR}/{DAY}/Input/{filename}.txt'
    ar: List[str] = []
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()
            ar.append(line)

    # This will store the non-overlapping range of fresh ingredients in a sorted order.
    fresh_ingredient_ranges: SortedList[List[int]] = []

    def optimize_ranges(start, end):
        # Iterate the available ranges. Keep on expanding the new range and delete existing ranges that overlap with this one.
        
        range_idx_to_delete: List[int] = []

        for idx in range(len(fresh_ingredient_ranges)):
            old_start, old_end = fresh_ingredient_ranges[idx]

            # No overlap
            if old_end < start or old_start > end:
                continue

            # Overlap found
            range_idx_to_delete.append(idx) # need to delete this idx
            start = min(start, old_start) # expand start if possible
            end = max(end, old_end) # expand end if possible
        
        # Delete indices in reverse fashion to sustain the correct index value.
        for idx in range_idx_to_delete[::-1]:
            fresh_ingredient_ranges.pop(idx)
        
        # Put new start and end in the range.
        fresh_ingredient_ranges.append([start, end])

    # Process each ingredient and if it overlaps, optimize the range.
    for line in ar:
        if not line:
            break

        start, end = map(int, line.split('-'))
        optimize_ranges(start, end)
    
    ans = 0
    for start, end in fresh_ingredient_ranges:
        ans += end - start + 1
    
    return ans

for name in FILE_NAMES:
    print(name, solve(name))
