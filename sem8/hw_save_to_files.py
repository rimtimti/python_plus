# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import json
import csv
import pickle
import os
from pathlib import Path


def volume_path(path: Path) -> int:
    """
    Возвращает размер файлов в директории в байтах
    """
    for path, _, files in os.walk(path):
        return sum([(Path(path) / file).stat().st_size for file in files])


def get_result_travers_directory(
    directory: Path, result={}
) -> dict[int : {str: str | int}]:
    """
    Обходит директорию и выдает список фалов и папок в ней и всех вложенных папках
    """
    for path, directories, files in os.walk(directory):
        for file in files:
            result[len(result) + 1] = {
                "name": file,
                "parent": path.split("\\")[-1],
                "type": "file",
                "size": f"{os.path.getsize(os.path.join(path, file))} bytes",
            }
        for direct in directories:
            result[len(result) + 1] = {
                "name": direct,
                "parent": path.split("\\")[-1],
                "type": "folder",
                "size": f"{volume_path(os.path.join(path, direct))} bytes",
            }
            get_result_travers_directory(direct, result)
    return result


def write_to_json(file, data: dict[int : {str: str | int}]) -> None:
    """
    Записывает словарь в json-файл
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_to_csv(file, data: dict[int : {str: str | int}]) -> None:
    """
    Записывает словарь в csv-файл
    """
    with open(file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(
            f, dialect="excel", quoting=csv.QUOTE_NONNUMERIC, delimiter=","
        )
        writer.writerow(("id", "name", "parent", "type", "size"))
        for key, value in data.items():
            writer.writerow(
                (key, value["name"], value["parent"], value["type"], value["size"])
            )


def write_to_pickle(file, data: dict[int : {str: str | int}]) -> None:
    """
    Записывает словарь в pickle-файл
    """
    with open(file, "wb") as f:
        pickle.dump(data, f)
