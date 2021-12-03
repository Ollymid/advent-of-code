from collections import Counter
from typing import List


def part_one() -> int:
    with open("input.txt") as file:
        cols = zip(*[[i for i in x.strip()] for x in file])

    gamma = "".join([Counter(c).most_common(1)[0][0] for c in cols])
    epsilon = "".join("1" if char is "0" else "0" for char in gamma)

    return int(gamma, 2) * int(epsilon, 2)


def part_two():
    with open("input.txt") as file:
        lines = [x.strip() for x in file]

    o2 = lines
    co2 = lines
    i = 0
    while len(o2) > 1 or len(co2) > 1:
        common = max(
            Counter(s[i] for s in o2).items(), key=lambda entry: (entry[1], entry[0])
        )[0]
        uncommon = min(
            Counter(s[i] for s in co2).items(), key=lambda entry: (entry[1], entry[0])
        )[0]

        o2 = [s for s in o2 if s[i] == common]
        co2 = [s for s in co2 if s[i] == uncommon]
        i += 1

    # common   '010111110111'
    # uncommon '100111001110'

    return int(o2[0], 2) * int(co2[0], 2)


def main():
    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")


if __name__ == "__main__":
    main()
