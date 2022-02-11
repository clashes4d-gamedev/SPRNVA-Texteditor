import random
import string

sample_file = open('res/sample_file.txt', 'w')
num_of_lines = 60
current_line = ''
lines = []

for j in range(random.randint(0, num_of_lines)):
    num_of_chars = random.randint(0, num_of_lines)
    for i in range(num_of_chars):
        current_char = random.choice(string.ascii_letters)
        current_line += current_char

        if len(current_line) == num_of_chars:
            sample_file.write(current_line + '\n')
            current_line = ''

sample_file.close()