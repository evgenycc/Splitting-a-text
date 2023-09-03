"""
pip install colorama
"""

from pathlib import Path

from colorama import Fore, init

init()

domain = set()


def save_line(path: str, file: Path, cnt: int) -> None:
    """
    Сохранение строк из множества в текстовый файл.
    :param path: Путь к целевой папке.
    :param file: Путь к файлу для обработки.
    :param cnt: Порядковый номер для сохранения файла.
    """
    global domain
    with open(Path(path) / f"{Path(file).name.strip(Path(file).suffix)}_{cnt}.txt", "a", encoding="utf-8") as spl:
        for dom in domain:
            spl.write(f'{dom}\n')


def main() -> None:
    """
    Запрос пути к целевой папке. Запрос кол-ва строк в файлах.
    Получение списка файлов в директории. Итерация по полученным файлам.
    Создание конвейера из генераторов для получения строки и ее обрезки.
    Итерация по генератору. Получение строки. Добавление в множество.
    Проверка на количество строк в множестве. При достижении указанного кол-ва строк
    сохранение строк в файл с номером. Увеличение номера на 1. Очистка множества.
    Проверка по завершении цикла, не является ли множество пустым. Если нет,
    сохраняем строки из него в файл. После обнуляем счетчик и удаляем обработанный файл.
    """
    global domain
    cnt = 0
    # path = input(Fore.GREEN + "Enter files path: " + Fore.RESET).replace('"', '').replace("'", "")
    path = r'D:\python\domain'
    count = int(input(Fore.GREEN + "Enter count lines: " + Fore.RESET))
    files = [x for x in Path(path).iterdir()]
    for file in files:
        try:
            lines = (x for x in open(file, 'r', encoding='utf-8'))
            f_strip = (x.strip() for x in lines)
            for nm, fl in enumerate(f_strip):
                domain.add(fl)
                print("\r\033[K", end="")
                print(f'\r{Fore.RESET}{nm+1} | {Fore.GREEN}{fl}{Fore.RESET}', end="")
                if len(domain) == count:
                    save_line(path, file, cnt)
                    domain.clear()
                    cnt += 1
            if 0 < len(domain) < count:
                cnt += 1
                save_line(path, file, cnt)
                domain.clear()
            cnt = 0
            Path(file).unlink()
        except UnicodeDecodeError:
            print(f"\nНе могу декодировать файл: {file}\n")
            continue
    print(f"\nAll split complete")


if __name__ == "__main__":
    main()
