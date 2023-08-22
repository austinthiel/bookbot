def count_words(text):
    return len(file_contents.split())

def count_letters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

frankenstein_book_path = "books/frankenstein.txt"
print(f"--- Begin report of {frankenstein_book_path} ---")
with open(frankenstein_book_path) as f:
    file_contents = f.read()
    
    total_word_count = count_words(file_contents)
    print(f"{total_word_count} words found in the document")

    character_count = count_letters(file_contents)
    character_count_list = list(character_count.items())
    character_count_list.sort(key=lambda x: x[1], reverse=True)
    for char, count in character_count_list:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
print (f"--- End report ---")
