from Lab1 import methods
from Lab1.container import Container

if __name__ == '__main__':
    input_str = input('Write keyword: ')
    input_file = input('Write input file: ')
    output_file = input('Write output file: ')
    app = Container(input_str)
    app.encrypt(input_file, output_file)
    key = app.decrypt(output_file)
    print(key)
    print(methods.string_to_bitstr(key))
