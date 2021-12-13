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


def part_two(input_data):

    depth_increased_count = 0
    length_of_input_data = len(input_data)
    logger.debug(len(input_data))
    for index, measurement in enumerate(input_data):
        logger.debug(f"Current index {index}")
        required_range_for_current_depth = index + 3
        required_index_available = required_range_for_current_depth < length_of_input_data
        if measurement != "" and required_index_available:
            previous_depth = int(measurement) + int(input_data[index + 1]) + int(input_data[index + 2])
            current_depth = int(input_data[index + 1]) + int(input_data[index + 2]) + int(input_data[index + 3])
            logger.debug(f"previous depth {previous_depth} current depth {current_depth}")
            if current_depth > previous_depth:
                depth_increased_count += 1
        else:
            logger.debug(f"Skipping execution because required index would be out of range")
            logger.debug(f"Current index is {index} and required would be {required_range_for_current_depth}")
    return depth_increased_count


if __name__ == '__main__':
    input_file = open("./input.txt", "r")
    puzzle_input = list(input_file)

    part_one_result = part_one(puzzle_input)
    logger.info(f"part one result is {part_one_result}")

    part_two_result = part_two(puzzle_input)
    logging.info(f"part two result is {part_two_result}")

    input_file.close()

