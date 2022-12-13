from pprint import pprint

def build(line):
    depth = None
    packet = None
    pointer = None
    cache = ""
    for char in line:
        if char == "[":
            if packet is None:
                depth = 0
                packet = list()
                pointer = packet
                continue

            depth = depth + 1
            nested = list()
            pointer.append(nested)
            pointer = nested
            continue

        if char == "]":
            if len(cache) > 0:
                pointer.append(int(cache))
                cache = ""

            depth = depth - 1
            pointer = packet
            for d in range(depth):
                pointer = pointer[-1]

            continue

        if char == ",":
            if len(cache) > 0:
                pointer.append(int(cache))
                cache = ""

            continue

        cache = cache + char

    return packet

def parse(puzzle_input):
    pairs = list()
    left = None
    right = None
    for line in puzzle_input:
        if len(line) == 0:
            pair = left, right
            pairs.append(pair)
            left = None
            right = None
            continue

        packet = build(line)
        if left is None:
            left = packet
            continue

        right = packet

    pair = left, right
    pairs.append(pair)

    return pairs

def compare(left, right, lp=None, rp=None):
    if lp is None:
        lp = left

    if rp is None:
        rp = right

    tl = type(lp)
    tr = type(rp)

    if tl != tr:
        if tl != list:
            lp = [lp]

        if tr != list:
            rp = [rp]

    ll = len(lp)
    lr = len(rp)
    for i in range(min(ll, lr)):
        lv = lp[i]
        tlv = type(lv)

        rv = rp[i]
        trv = type(rv)

        if list not in [tlv, trv]:
            if lv < rv:
                return True

            if lv > rv:
                return False

            continue

        result = compare(left, right, lv, rv)
        if result is None:
            continue

        return result

    if ll == lr:
        return None

    return ll < lr

def partition(packets, low, high):
    pivot = packets[high]
    i = low - 1
    for j in range(low, high):
        packet = packets[j]
        if compare(packet, pivot) in [True, None]:
            i = i + 1
            packets[i], packets[j] = packets[j], packets[i]

    packets[i+1], packets[high] = packets[high], packets[i+1]
    return i + 1

def qsort(packets, low=0, high=None):
    if high is None:
        high = len(packets) - 1

    if low < high:
        index = partition(packets, low, high)
        qsort(packets, low, index-1)
        qsort(packets, index+1, high)

def p1(puzzle_input):
    pairs = parse(puzzle_input)
    valid = 0
    for i, (left, right) in enumerate(pairs):
        if compare(left, right):
            valid = valid + i + 1

    return valid

def p2(puzzle_input):
    pairs = parse(puzzle_input)
    packets = list()
    fst = [[2]]
    snd = [[6]]
    packets.append(fst)
    packets.append(snd)
    for (left, right) in pairs:
        packets.append(left)
        packets.append(right)

    qsort(packets)
    fi, si = None, None
    for i, packet in enumerate(packets):
        if None not in [fi, si]:
            break

        if packet == fst:
            fi = i + 1
            continue

        if packet == snd:
            si = i + 1

    return fi * si

def solve(puzzle_input):
    return p1(puzzle_input), p2(puzzle_input)
