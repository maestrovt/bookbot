def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"Number of words found in this document: {get_word_count(text)}")
    char_dict = get_letter_count(text)
    list_tuples = list(char_dict.items())
    list_tuples.sort(key = lambda x: x[1], reverse = True)
    for char, count in list_tuples:
        print(f"The '{char}' character was found {count} times")
def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_letter_count(text):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                "j", "k", "l", "m", "n", "o", "p", "q",
                "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    count = []
    for i in range(0, 26):
        count.append(0)
    letter = {}
    text_lower = text.lower()
    for char in text_lower:
        for i in range(0, 26):
            if char == alphabet[i]:
                count[i] += 1
                letter[alphabet[i]] = count[i]
    return letter
def get_word_count(string):
    words = []
    words = string.split()
    return len(words)

main()