# ამოცანა 2

# def write_file(file_counter, lines_lst):
#     with open(f'filtered{file_counter}.txt', 'w') as new_file:
#         new_file.writelines(lines_lst)
#
# def manage_file(filename):
#     with open(filename, 'r') as file:
#         file_counter = 1
#         lines_lst = []
#         for line in file.readlines():
#             if lines_lst and len(lines_lst) % 10 == 0:
#                 write_file(file_counter, lines_lst)
#                 lines_lst.clear()
#                 file_counter += 1
#                 lines_lst.append(line)
#             else:
#                 lines_lst.append(line)
#         else:
#             write_file(file_counter, lines_lst)
#
# manage_file('test.txt')



# ამოცანა 3

def clean_file(old_file, new_file):
    lines = []

    with open(old_file, 'r') as file:
        for line in file.readlines():
            if line != '\n':
                lines.append(line)

    with open(new_file, 'w') as file:
        file.writelines(lines)

clean_file('test.txt', 'cleaned.txt')