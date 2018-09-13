def disemvowel(word):
    word_as_list = list(word)
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    for char in vowels:
        while True:
            try:
                word_as_list.remove(char)
            except ValueError:
                break
    return ''.join(word_as_list)