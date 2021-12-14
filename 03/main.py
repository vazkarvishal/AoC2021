import logging
from operator import itemgetter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


if __name__ == '__main__':
    input_file = open("./input.txt", "r")
    puzzle_input = list(input_file)

    binary_number_length = len(puzzle_input[0].strip())
    logger.debug(binary_number_length)

    fragmented_puzzle_input_list: list = []

    for binary_number in puzzle_input:
        fragmented_puzzle_input_list.append(list(binary_number.strip()))

    gamma_rate: str = ""
    epsilon_rate: str = ""

    for number in range(0, binary_number_length):

        zero_count: int = 0
        one_count: int = 0
        pos_specific_list: list = list(
            map(
                itemgetter(number),
                fragmented_puzzle_input_list
            )
        )
        for item in pos_specific_list:
            if int(item) == 0:
                zero_count += 1
            elif int(item) == 1:
                one_count += 1
            else:
                logger.info(f"Invalid Input {item} is nor 0 or 1")

        if zero_count > one_count:
            gamma_rate += "0"
            epsilon_rate += "1"
            logging.debug(f"zero count {zero_count} is higher than one count {one_count}")
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
            logging.debug(f"one count {one_count} is higher than zero count {zero_count}")

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    logging.info(gamma_rate*epsilon_rate)

    input_file.close()

