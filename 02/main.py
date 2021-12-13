import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def part_one(data):

    forward: int = 0
    depth: int = 0
    for navigation_details in data:
        direction, steps = navigation_details.split(" ")
        if str(direction).lower() == "forward":
            forward = forward + int(steps)
        elif str(direction).lower() == "down":
            depth = depth + int(steps)
        elif str(direction).lower() == "up":
            depth = depth - int(steps)
        else:
            logging.error(f"invalid input found {navigation_details}")
    total_movement = forward * depth
    logging.debug(f"Forward is {forward} and depth is {depth}")
    return total_movement


def part_two(data):

    aim: int = 0
    horizontal_position: int = 0
    depth: int = 0

    for navigation_details in data:
        direction, steps = navigation_details.split(" ")
        if str(direction).lower() == "forward":
            horizontal_position = horizontal_position + int(steps)
            depth = (depth + (aim * int(steps)))
        elif str(direction).lower() == "down":
            aim = aim + int(steps)
        elif str(direction).lower() == "up":
            aim = aim - int(steps)
        else:
            logging.error(f"invalid input found {navigation_details}")
    total_movement = horizontal_position * depth
    logging.debug(f"horizontal_position is {horizontal_position} and aim is {aim}")
    return total_movement


if __name__ == '__main__':
    input_file = open("./input.txt", "r")
    puzzle_input = list(input_file)

    submarine_movement_part_one = part_one(puzzle_input)
    logging.info(f"Final movement of the submarine part one is {submarine_movement_part_one}")

    submarine_movement_part_two = part_two(puzzle_input)
    logging.info(f"Final movement of the submarine part two is {submarine_movement_part_two}")

    input_file.close()
