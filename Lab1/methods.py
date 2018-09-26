from bitstring import BitArray


def read_file(input_file):
    data = []
    with open(input_file, 'r') as file:
        for line in file:
            data.append(line)
    file.close()
    return data


def modify_str(string):
    return string[:len(string) - 1] + ' \n'


def write_file(data, output_file):
    with open(output_file, 'w') as file:
        for line in data:
            file.write(line)
    file.close()


def get_info(string):
    if string[len(string) - 2] == ' ':
        return 1
    else:
        return 0


def string_to_bitstr(string):
    data = []
    for i in string:
        value = BitArray(bin=bin(ord(i))).bin
        data.append('0' * (7 - len(value)) + value)
    return data


def is_encrypt(input_file):
    with open(input_file, 'r') as file:
        if file.readline()[0] == chr(164):
            return True
    file.close()
    return False


def clear_container(input_file):
    data = []
    with open(input_file, 'r') as file:
        file.readline()
        for line in file:
            if line[len(line) - 2] == ' ':
                line = line[:len(line) - 2] + '\n'
                data.append(line)
            else:
                data.append(line)
    file.close()
    return data


def clear_file(input_file):
    data = []
    with open(input_file, 'r') as file:
        line = file.readline()
        while line:
            result = clear_str(line)
            data.append(result)
            line = file.readline()
    return data


def clear_str(line):
    i = len(line) - 2
    while line[i] == ' ':
        i -= 1
    return line[:i + 1:] + '\n'
