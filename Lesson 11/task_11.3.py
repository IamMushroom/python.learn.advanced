# Напишите программу, переводящую цепь ДНК в цепь РНК.

def dnk_to_rnk(__dnk_chain: str) -> str:
    d = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    result = ''
    for char in __dnk_chain:
        result += d[char]
    return result


def solution() -> None:
    print(dnk_to_rnk(input()))


solution()
