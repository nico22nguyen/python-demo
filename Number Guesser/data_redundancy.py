#0, 1, 8
raw = open("raw_training_data.txt", 'r')
lines = raw.readlines()
raw.close()

flipped_lines = []
for line in lines:
    if line[256] == '1' or line[257] == '1' or line[264] == '1':
        data = line[:256]
        label = line[256:]
        flipped_data = data[::-1]
        flipped_lines.append((flipped_data + label))

raw = open("raw_training_data.txt", 'a')
raw.write("\n")
for i in range(len(flipped_lines)):
    if i == len(flipped_lines) - 1:
        raw.write(flipped_lines[i].replace('\n', ''))
    else:
        raw.write(flipped_lines[i])

raw.close()