def list_from_file(filename):
    with open(filename) as file:
        return [x.split(" ") for x in file.read().split("\n")]


def part_one(command_list):
    final_position = 0
    final_depth = 0

    for command in command_list:
        if command[0] == "forward":
            final_position += int(command[1])
        elif command[0] == "down":
            final_depth += int(command[1])
        elif command[0] == "up":
            final_depth -= int(command[1])
        else:
            raise ValueError("Command not recognized!")

    return final_position, final_depth


def part_two(command_list):
    final_position = 0
    final_depth = 0
    aim = 0

    for command in command_list:
        if command[0] == "forward":
            final_position += int(command[1])
            final_depth += int(command[1]) * aim
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
        else:
            raise ValueError("Command not recognized!")

    return final_position, final_depth


def main():
    control_list = list_from_file("input.txt")
    position, depth = part_one(control_list)
    print(f"Part 1: {position*depth}")
    position_2, depth_2 = part_two(control_list)
    print(f"Part 2: {position_2*depth_2}")


if __name__ == "__main__":
    main()
