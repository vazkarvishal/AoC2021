import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

if __name__ == '__main__':
    input_file = open("./input.txt", "r")
    puzzle_input = list(input_file)
    forward: int = 0
    depth: int = 0
    for navigation_details in puzzle_input:
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
    logging.info(f"Final movement of the submarine is {total_movement}")

    input_file.close()
