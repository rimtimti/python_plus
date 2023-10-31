# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
from pathlib import Path


def _add_data(name: str, personal_id: int, level: int) -> dict[int, dict[str, int]]:
    return {level: {personal_id: name}}


def _write_json(data: dict, file: str) -> None:
    with open(file, "w+", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _read_json(file: str):
    with open(file, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return {}


def ui(file: str):
    file = Path(file)
    file.touch(exist_ok=True)
    base_dict = _read_json(file)
    print(base_dict)
    exit_program = True
    print("Добро пожаловать в программу. Введите данные для создания файла...")
    while exit_program:
        personal_id = input("Введите id: ")
        name = input("Введите имя: ")
        level = input("Введите уровень доступа: ")
        continue_program = input("Хотите продолжить? да/нет: ")
        if continue_program == "нет":
            exit_program = False
        res_dict = _add_data(name, personal_id, level)
        if level in base_dict.keys():
            base_dict[level].update({personal_id: name})
        else:
            base_dict.update(res_dict)
    print(base_dict)

    _write_json(base_dict, file)
