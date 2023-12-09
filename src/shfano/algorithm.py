from collections import Counter
from typing import List
import asyncio


class Symbol:
    def __init__(self, value: str, chance: float, code: str = ''):
        self.value = value
        self.chance = chance
        self.code = code

    def __repr__(self) -> str:
        return f"<Symbol {self.value} with chance {self.chance} and code {self.code}>"


async def get_sorted_symbols(string: str) -> List[Symbol]:
    length = len(string)
    counts = Counter(string)
    symbols = [Symbol(value=char, chance=frq) for char, frq in counts.items()]
    symbols.sort(key=lambda char: char.frequency, reverse=True)
    print(symbols)
    await get_codes(symbols=symbols, start=0, end=len(symbols) - 1)
    print(symbols)
    return symbols


async def get_codes(symbols: List[Symbol], start: int, end: int):
    if start >= end:
        return

    # Вычисляем сумму частот символов
    total_frequency = sum([symbol.frequency for symbol in symbols[start:end+1]])

    # Делим символы на две группы, чтобы сумма частот групп была примерно равна
    mid = start
    current_sum = symbols[start].frequency
    while current_sum < total_frequency // 2:
        mid += 1
        current_sum += symbols[mid].frequency

    # Присваиваем код для символов каждой группы
    for i in range(start, mid+1):
        symbols[i].code += "1"
    for i in range(mid+1, end+1):
        symbols[i].code += "0"

    # Рекурсивно делим символы в каждой группе
    await asyncio.gather(
        get_codes(symbols, start, mid),
        get_codes(symbols, mid + 1, end)
    )




st = 'A'* 50 + 'B' * 39 + 'C' * 18 + 'D' * 49 + 'E' * 35 + 'F' * 24
print(st)
asyncio.run(get_sorted_symbols(st))


