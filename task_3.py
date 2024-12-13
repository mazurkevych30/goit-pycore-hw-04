import sys
from pathlib import Path
from colorama import Fore, Style

def structure_of_directory(path, level = 1):
    t = "   " * level
    for element in path.iterdir():
        if element.is_dir():
            print(f"{Fore.BLUE}{t}{element.name}/{Style.RESET_ALL}")
            structure_of_directory(element, level+1)
        else:
            print(f"{Fore.GREEN}{t}{element.name}{Style.RESET_ALL}")


p = Path(sys.argv[1])
if p.is_dir() and p.exists():
    print(f"{Fore.BLUE}{p.name}/{Style.RESET_ALL}")
    structure_of_directory(p)
else:
    print(f"{Fore.RED}Помилка. Вказаний шлях не існує або він не веде до директорії{Style.RESET_ALL}")
