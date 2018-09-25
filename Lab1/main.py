from Lab1 import methods
from Lab1.container import Container

if __name__ == '__main__':
    input_str = input('Write keyword: ')
    app = Container(input_str)
    app.encrypt('input.txt', 'output.txt')
    key = app.decrypt('output.txt')
    print(key)
    print(methods.string_to_bitstr(key))
    print()
    input_str = input('Write keyword: ')
    app1 = Container(input_str)
    app1.encrypt('output.txt', 'test.txt')
    key1 = app1.decrypt('test.txt')
    print(key1)
    print(methods.string_to_bitstr(key1))
