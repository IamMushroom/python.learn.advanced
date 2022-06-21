# Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files уникальные имена файлов c расширением .png, независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением, все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg',
         'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']


def solution(__files: list[str], __ext: str) -> set[str]:
    result = {file.lower() for file in __files if file[-4::].lower() == __ext}
    return result


ext = '.png'
print(*sorted(solution(files, ext)))
