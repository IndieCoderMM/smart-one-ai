from smart_one.utils.settings import MEMORY_PATH, NAME, USER


def load_memory() -> str:
    memo = ""
    with open(MEMORY_PATH) as memory:
        for line in memory:
            memo += line.replace("$[USERNAME]",
                                 USER).replace("$[AINAME]", NAME)
    return memo


def save_memory(data: str):
    data = data.replace("YOU:", "$[USERNAME]:").replace(NAME, "$[AINAME]")
    with open(MEMORY_PATH, "w") as file:
        file.write(data)