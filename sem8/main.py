from create_json import create_json

from add_name_to_json import ui
from hw_save_to_files import get_result_travers_directory, write_to_json, write_to_csv, write_to_pickle

if __name__ == '__main__':
    # create_json(Path('result.txt'))
    # ui('data.json')
    # print(type(read_json()))
    result = get_result_travers_directory('C:\\Users\\rimtimti\\Desktop\\test')
    write_to_json('info_dir_to_.json', result)
    write_to_csv('info_dir_to_.csv', result)
    write_to_pickle('info_dir_to_.pickle', result)