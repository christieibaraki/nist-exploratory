from main.utility.io_utility import *

def main():

    file1 = read_dictionary_from_file(get_main_path("resources/NVD/nvdcve-1.0-2002.json"))
    print(file1.keys())


if __name__ == '__main__':
    main()
