
lines = [2, 8, 10, 13, 17]
lines_words = ['Two', 'Eight', "Ten", "Thirteen", "Seventeen"]

# zipped_list = list(zip(lines, lines_words))

data = {
    2: 'Two',
    8: 'Eight',
    10: 'Ten',
    13: 'Thirteen',
    17: 'Seventeen'
}

with open('numbers.txt', 'w') as file:
    last_line = lines[-1]
    current_line = 1

    while current_line <= last_line:
        if current_line in data.keys():
            file.write(data[current_line] + '\n')
        else:
            file.write('\n')
        current_line += 1




lines = [2, 8, 10, 13, 17]
lines_words = ['Two', 'Eight', "Ten", "Thirteen", "Seventeen"]

zipped_list = list(zip(lines, lines_words))
with open('numbers.txt', 'w') as file:
    last_line = lines[-1]
    line_counter = 1

    while line_counter <= last_line:
        word_written = False
        for line, word in zipped_list:
            if line_counter == line:
                file.write(word + '\n')
                word_written = True
                break
        if not word_written:
            file.write('\n')
        line_counter += 1