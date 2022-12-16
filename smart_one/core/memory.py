def load_memory(file: str) -> str:
    memo = ""
    with open(file) as memory:
        for line in memory:
            memo += line
    return memo