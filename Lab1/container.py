from bitstring import BitArray

from Lab1 import methods


class Container:
    def __init__(self, key):
        self.key = key

    def encrypt(self, input_file, output_file):
        if methods.is_encrypt(input_file):
            text = methods.clear_container(input_file)
        else:
            text = methods.read_file(input_file)
        bit_array = methods.string_to_bitstr(self.key)
        count = 0
        if len(bit_array) * 7 > len(text):
            print('Big data for input file!')
            print('Volume of input data: ' + str(len(bit_array) * 7))
            print('Container volume: ' + str(len(text)))
            output = [chr(164) + ' ' + str(len(text)) + ' ' + str(len(text)) + '\n']
        else:
            print('Volume of input data: ' + str(len(bit_array) * 7))
            print('Container volume: ' + str(len(text)))
            output = [chr(164) + ' ' + str(len(bit_array) * 7) + ' ' + str(len(text)) + '\n']
        for symbol in bit_array:
            for i in range(len(symbol)):
                if count == len(text):
                    break
                if symbol[i] == '0':
                    output.append(text[count])
                    count += 1
                else:
                    output.append(methods.modify_str(text[count]))
                    count += 1
        while count < len(text):
            output.append(text[count])
            count += 1
        methods.write_file(output, output_file)
        print('Encryption ' + output_file + ' successfully!')


    def decrypt(self, input_file):
        word = ''
        with open(input_file, 'r') as file:
            count = int(file.readline().split()[1])
            symbol = ''
            for i in range(count):
                symbol += str(methods.get_info(file.readline()))
                if len(symbol) % 7 == 0:
                    word += chr(BitArray(bin=symbol).uint)
                    symbol = ''
        file.close()
        print('Decryption ' + input_file + ' successfully!')
        return word
