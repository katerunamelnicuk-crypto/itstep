import colorama
from colorama import init, Fore, Back, Style

init(autoreset=True)
print("init(autoreset=True) потрібне для того, щоб минулі маніпуляції з текстом не впливали на наступні. Також можна використовувати Style.RESET_ALL, але це займає багато часу")
print(f"{Style.BRIGHT}Жирний шрифт")
print(Fore.RED + "Текст червоний")
print(Fore.GREEN + "Зелений")
print(Back.MAGENTA + Fore.BLACK + "Чорний текст на фіолетовому фоні")
print(Back.CYAN + Fore.BLACK + f"{Style.DIM}синій текст на наче синьому фоні, а завдяки style.dim текст тьмяний")
print("Це все можна використовувати для гарного оформлення тексту, наприклад це:")
print(Back.RED + Fore.BLACK + "!!ERROR!!")
