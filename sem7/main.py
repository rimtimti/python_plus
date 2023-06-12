from pathlib import Path
from feel_numbers import feel_numbers
from gen_names import name_gen
from two_files_in_one import two_files_in_one
from gen_files import gen_files
from hw import rename_files

if __name__ == '__main__':
    # feel_numbers(3, 'file_1.txt')
    # name_gen(10, 4, 7, Path('name_gen'))
    # two_files_in_one('file_1.txt', 'name_gen', 'result.txt')
    # gen_files('C:\\Users\\rimtimti\\Desktop\\test', 'bin', 5, 10, 1024, 4096, 5)
    rename_files(3, '4', 'bin', 'txt', 0, 5, 'C:\\Users\\rimtimti\\Desktop\\test')