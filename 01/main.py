if __name__ == '__main__':
    input_file = open("./input.txt", "r")
    puzzle_input = list(input_file)
    depth_increased_count = 0
    for index, measurement in enumerate(puzzle_input):
        if index != 0 and measurement != "":
            previous_depth = int(puzzle_input[index-1])
            current_depth = int(measurement)
            if current_depth > previous_depth:
                depth_increased_count += 1
            else:
                print(f"{previous_depth} is greater than {current_depth}. Skipping")
    input_file.close()
    print(depth_increased_count)
