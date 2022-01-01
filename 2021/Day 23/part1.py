from typing import List, Tuple
from collections import defaultdict
import heapq


YEAR = 2021
DAY = 'Day 23'
FILE_NAMES = ['small', 'large']


def any_blocking(apods, idx, dest):
    # Check if any amphipods between a pods[idx] and dest room
    assert len(apods) == 8

    hall_loc, room, _ = apods[idx]
    assert hall_loc == -1 or room == -1
    loc = max(hall_loc, room)

    for j in range(8):
        if j == idx or apods[j][0] == -1:
            continue

        o_loc = apods[j][0]
        assert loc != o_loc

        if (dest <= o_loc <= loc) or (loc <= o_loc <= dest):
            return True

    return False


def children(state):
    # Compute all next states from given state
    cost, apods = state
    assert len(apods) == 8

    for i, apod in enumerate(apods):
        type = i // 2
        loc, room, depth = apod

        assert not loc in [2, 4, 6, 8]

        # Is this amphipod settled in?
        if loc == -1:
            assert room != -1
            if room == (type + 1) * 2:
                if depth == 2:
                    continue

                partner = apods[type*2 + (1 - i % 2)]
                if (partner[2], depth) in [(1, 2), (2, 1)]:
                    # All settled in
                    continue

        if True:
            out_cost = 0 if room == -1 else depth
            practical_loc = max(loc, room)

            # Try to move into a room next turn
            dest_room = (type + 1) * 2

            # If you are in a room and wish to go out, check first if you can actually get out
            good = True
            if room != -1 and depth == 2:
                assert loc == -1
                blocking = False
                for j in range(8):
                    if j == i:
                        continue
                    if apods[j][1] == room and apods[j][2] == 1:
                        blocking = True
                        break

                good = not blocking

            if good:
                # Any foreigners in this room?
                foreigners = False
                for j in range(8):
                    if j == i or j == type*2 + (1 - i % 2) or apods[j][1] == -1:
                        # Is self, or is partner, or not in dest room
                        continue

                    if apods[j][1] == dest_room:
                        foreigners = True
                        break

                if not foreigners:
                    partner = apods[type*2 + (1 - i % 2)]

                    if partner[1] == (type + 1) * 2:
                        if partner[2] != 1:
                            assert partner[2] == 2

                            # Partner occupies at depth 2 ig
                            if not any_blocking(apods, i, dest_room):
                                cost_to_move = pow(
                                    10, type) * (abs(practical_loc - dest_room) + 1 + out_cost)
                                apods_copy = list(apods)
                                apods_copy[i] = (-1, dest_room, 1)
                                yield cost + cost_to_move, tuple(apods_copy)

                    else:
                        # There might be others in this room
                        if not any([apods[j][1] == dest_room for j in range(8) if j != i]):

                            if not any_blocking(apods, i, dest_room):

                                # If empty, we can move here!
                                cost_to_move = pow(
                                    10, type) * (abs(practical_loc - dest_room) + 2 + out_cost)
                                apods_copy = list(apods)
                                apods_copy[i] = (-1, dest_room, 2)
                                yield cost + cost_to_move, tuple(apods_copy)

        # In a room
        if room == -1:
            assert loc != -1
            continue

        assert room != -1 and depth != -1 and loc == -1

        # Check if anyone's blocking in the room
        if depth == 2:
            blocking = False
            for j in range(8):
                if j == i:
                    continue

                if apods[j][1] == room and apods[j][2] == 1:
                    blocking = True
                    break
            if blocking:
                continue

        # Go into the hallway?
        for dest_loc in [0, 1, 3, 5, 7, 9, 10]:
            cost_to_move = pow(10, type) * (abs(room - dest_loc) + (depth))

            if any_blocking(apods, i, dest_loc):
                continue

            apods_copy = list(apods)
            apods_copy[i] = (dest_loc, -1, -1)
            yield cost + cost_to_move, tuple(apods_copy)

        # And that's it!


def detect_end(apods: List[Tuple[int, int, int]]) -> bool:
    for i in range(8):
        apod = apods[i]
        loc, room, depth = apod
        if loc != -1:
            return False
        if room != (i // 2) * 2 + 2:
            return False

    return True


def getCost(hallway, rows) -> int:
    start_apods = [None] * 8
    type_counter = [0, 0, 0, 0]

    # Parse hallway
    for loc in range(11):
        if hallway[loc] == '.':
            continue
        type = 'ABCD'.index(hallway[loc])
        start_apods[type * 2 + type_counter[type]] = (loc, -1, -1)
        type_counter[type] += 1

    # Parse rooms
    for depth, row in enumerate(rows, start=1):
        for i in range(4):
            if row[i] == '.':
                continue
            type = 'ABCD'.index(row[i])
            start_apods[type * 2 + type_counter[type]
                        ] = (-1, (i * 2) + 2, depth)
            type_counter[type] += 1

    start_state = 0, tuple(start_apods)
    pq = [start_state]

    done = set()
    cost = defaultdict(int)

    while pq:
        cur_cost, cur_apods = heapq.heappop(pq)
        if cur_apods in done:
            continue
        done.add(cur_apods)

        cost[cur_apods] = cur_cost

        if detect_end(cur_apods):
            return cur_cost

        for next_state in children((cur_cost, cur_apods)):
            if next_state[1] in done:
                continue
            heapq.heappush(pq, next_state)


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'

    with open(INPUT_PATH, 'r') as _file:
        data = _file.read().strip().splitlines()

    hallway = data[1][1:12]
    rows = [data[2][3:10:2]] + [data[3][3:10:2]]

    return getCost(hallway, rows)


for name in FILE_NAMES:
    print(name, solve(name))
