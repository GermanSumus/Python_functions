def write_to(file_path, input_to_file):
    f = open(file_path, 'a+')
    f.write(input_to_file)
    f.close()

def read_from(file_path):
    f = open(file_path)
    line = f.readline()
    while line:
        line = line.strip('\n')
        print(line)
        line = f.readline()
