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
    symbols = [Symbol(value=char, chance=frq/length) for char, frq in counts.items()]
    symbols.sort(key=lambda char: char.chance, reverse=True)
    return symbols


async def get_symbols_codes(symbols: List[Symbol], start: int, end: int):
    if start >= end:
        return

    # Делим символы на две группы, чтобы сумма вероятностей групп была примерно равна
    mid = start
    left_sum = symbols[start].chance
    right_sum = sum(s.chance for s in symbols[start+1:end+1])
    while left_sum < right_sum:
        mid += 1
        left_sum += symbols[mid].chance
        right_sum -= symbols[mid].chance
    # Присваиваем код для символов каждой группы
    for i in range(start, mid+1):
        symbols[i].code += "1"
    for i in range(mid+1, end+1):
        symbols[i].code += "0"

    # Рекурсивно делим символы в каждой группе
    await asyncio.gather(
        get_symbols_codes(symbols, start, mid),
        get_symbols_codes(symbols, mid + 1, end)
    )


async def encode(string: str):
    symbols_list = await get_sorted_symbols(string)
    await get_symbols_codes(symbols=symbols_list, start=0, end=len(symbols_list) - 1)
    result = {}
    for s in symbols_list:
        result[s.value] = s.code
    return result

