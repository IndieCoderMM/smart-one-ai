from smart_one.utils.settings import MEMORY_PATH, NAME, USER


def load_memory() -> str:
    """Get the prompt to be use as initial conversation
    """
    memo = ""
    with open(MEMORY_PATH + "memory.txt") as memory:
        for line in memory:
            memo += line.replace("$[USERNAME]",
                                 USER).replace("$[AINAME]", NAME)
    return memo


def save_memory(filename: str, data: str):
    filename = "saved_data" if not filename else filename
    with open(MEMORY_PATH + filename + ".txt", "w") as file:
        file.write(data)