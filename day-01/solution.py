from typing import List


def list_from_file(filename) -> List[int]:
    with open(filename) as file:
        return [int(x) for x in file.read().split("\n")]


def part_one(data: List[int]) -> int:
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1

    return count


def part_two(data: List[int]) -> int:
    count = 0
    for i in range(1, len(data)):
        if i > 2:
            current = data[i] + data[i - 1] + data[i - 2]
            previous = data[i - 1] + data[i - 2] + data[i - 3]
            if current > previous:
                count += 1
    return count


def main():
    depthlist = list_from_file("input.txt")
    print(f"Part 1: {part_one(depthlist)}")
    print(f"Part 2: {part_two(depthlist)}")


if __name__ == "__main__":
    main()
