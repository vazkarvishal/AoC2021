import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def part_one(input_data):

    depth_increased_count = 0
    for index, measurement in enumerate(input_data):
        if index != 0 and measurement != "":
            previous_depth = int(input_data[index - 1])
            current_depth = int(measurement)
            if current_depth > previous_depth:
                depth_increased_count += 1
            else:
                logger.debug(f"{previous_depth} is greater than {current_depth}. Skipping")
    return depth_increased_count


if __name__ == '__main__':
    input_file = open("./input.txt", "r")
    puzzle_input = list(input_file)

    part_one_result = part_one(puzzle_input)
    logger.info(f"part one result is {part_one_result}")

    input_file.close()

