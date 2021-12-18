YEAR = 2021
DAY = 'Day 16'
FILE_NAMES = ['part2-small-01', 'part2-small-02',
              'part2-small-03', 'part2-small-04', 'part2-small-05', 'part2-small-06',
              'part2-small-07', 'part2-small-08', 'large']


class Packet:
    def __init__(self, version, typeId, packets=None, literalValue=None) -> None:
        self.version = version
        self.typeId = typeId
        self.packets = packets
        self.literalValue = literalValue

    def __str__(self) -> str:
        print('asas')
        return f'Version: {self.version}, TypeId: {self.typeId}, Packets: {self.packets}, Literal: {self.literalValue}'


def parse_packet(bits) -> Packet:
    version = int(bits[0:3], 2)
    typeId = int(bits[3:6], 2)
    bits = bits[6:]

    if typeId == 4:
        cur = ''
        while bits[0] == '1':
            cur += bits[1:5]
            bits = bits[5:]
        cur += bits[1:5]
        bits = bits[5:]
        value = int(cur, 2)
        return Packet(version, typeId, [], value), bits
    else:
        lengthTypeId = bits[0]
        bits = bits[1:]
        if lengthTypeId == '0':
            cur = int(bits[:15], 2)
            bits = bits[15:]
            a = bits[:cur]
            bits = bits[cur:]
            packets = []

            while a:
                packet, a = parse_packet(a)
                packets.append(packet)
            return Packet(version, typeId, packets, None), bits
        else:
            cur = int(bits[:11], 2)
            bits = bits[11:]
            packets = []
            for i in range(cur):
                packet, bits = parse_packet(bits)
                packets.append(packet)
            return Packet(version, typeId, packets, None), bits


def toBinary(s) -> str:
    ans = ''
    for i in s:
        ans += bin(int(i, 16))[2:].zfill(4)
    return ans


def find_ans(packet: Packet) -> int:
    if packet.typeId == 0:
        return sum([find_ans(i) for i in packet.packets])
    if packet.typeId == 1:
        ans = 1
        for i in packet.packets:
            ans *= find_ans(i)
        return ans
    if packet.typeId == 2:
        return min([find_ans(i) for i in packet.packets])
    if packet.typeId == 3:
        return max([find_ans(i) for i in packet.packets])

    if packet.typeId == 5:
        a = find_ans(packet.packets[0])
        b = find_ans(packet.packets[1])
        return int(a > b)
    if packet.typeId == 6:
        a = find_ans(packet.packets[0])
        b = find_ans(packet.packets[1])
        return int(a < b)
    if packet.typeId == 7:
        a = find_ans(packet.packets[0])
        b = find_ans(packet.packets[1])
        return int(a == b)

    return packet.literalValue


def solve(filename):
    INPUT_PATH = f'./{YEAR}/{DAY}/Input/{filename}.txt'
    with open(INPUT_PATH, 'r') as _file:
        for line in _file:
            line = line.strip()

            line = toBinary(line)

    ans, _ = parse_packet(line)
    ans = find_ans(ans)
    return ans


for name in FILE_NAMES:
    print(name, solve(name))
