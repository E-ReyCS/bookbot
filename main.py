def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = wordcount(text)
    char_count = character_count(text)
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document.")
    for word in char_count:
        print(f"The {word} character was found {char_count[word]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def wordcount(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lowered_string = text.lower()
    count_dictionary = {}
    for letter in lower_alphabet:
        char_count = lowered_string.count(letter)
        count_dictionary[letter] = char_count
    return count_dictionary



main()