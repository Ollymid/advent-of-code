from collections import Counter
from typing import List


def list_from_file(filename) -> List[str]:
    with open(filename) as file:
        return file.read().splitlines()


def part_one(binaries):
    cols = zip(*[[int(i) for i in x.strip()] for x in binaries])

    gamma = "".join([str(Counter(c).most_common(1)[0][0]) for c in cols])
    epsilon = "".join("1" if char is "0" else "0" for char in gamma)

    return int(gamma, 2) * int(epsilon, 2)


def main():
    bin_list = list_from_file("input.txt")
    print(f"Part 1: {part_one(bin_list)}")


if __name__ == "__main__":
    main()
