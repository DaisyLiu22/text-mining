def file_to_list():
    """return a list of words, from Dracula.txt"""
    words = []
    with open('data/dracula.txt') as f:
        for line in f.readlines():
            words.append(line.strip())
        return words

        