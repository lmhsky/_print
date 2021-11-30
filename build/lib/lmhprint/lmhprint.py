import random

def _print(str):
    _printl = [
        # # 不要你们了.亮瞎我的眼了.
        # f'\033[7m{str}\033[0m',
        # f'\033[41m{str}\033[0m',
        # f'\033[46m{str}\033[0m',
        f'******\033[31m{str}\033[0m',
        f'******\033[32m{str}\033[0m',
        f'******\033[33m{str}\033[0m',
        f'******\033[34m{str}\033[0m',
        f'******\033[35m{str}\033[0m',
        f'******\033[36m{str}\033[0m']
    ix = random.randint(0, len(_printl) - 1)
    print(_printl[ix])
