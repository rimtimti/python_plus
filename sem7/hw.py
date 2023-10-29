# Напишите функцию группового переименования файлов.
# Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from pathlib import Path
import os


def rename_files(
    exponent: int,
    name_end: str,
    extension_old: str,
    extension_new: str,
    name_from: int,
    name_to: int,
    directory: Path,
) -> None:
    if os.path.isdir(directory) == False:
        os.mkdir(directory)
    os.chdir(directory)
    p = Path().cwd()
    count = 1
    for obj in p.iterdir():
        full_name = str(obj).split("\\")[-1]
        if "." in full_name:
            file_name, file_extension = full_name.split(".")
            if file_extension == extension_old and file_name.endswith(name_end):
                new_name = (
                    f"{file_name[name_from:name_to]}{count:0{exponent}}.{extension_new}"
                )
                if os.path.isfile(new_name) == False:
                    Path(full_name).rename(new_name)
                    count += 1
                else:
                    Path(full_name).rename(
                        f"{file_name[name_from:name_to]}{count:0{exponent}} - other.{extension_new}"
                    )
        else:
            continue
