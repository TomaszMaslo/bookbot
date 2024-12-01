def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    list_of_dicts = make_list_of_dicts_from_dict(letter_count)
    sorted_list = sort_list(list_of_dicts)
    print_report(sorted_list, book_path, word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    count = text.split()
    return len(count)

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def make_list_of_dicts_from_dict(dict):
    list_of_dict = []

    for key, value in dict.items():
        list_of_dict.append({key: value})
    return list_of_dict

def sort_on(dict):
    return list(dict.values())[0]

def sort_list(list_of_dicts):
    sorted_list = sorted(list_of_dicts, reverse=True, key=sort_on)
    return sorted_list

def print_report(sorted_list, text, word_count):
    print(f'--- Begin report on {text} ---')
    print(f'{word_count} words found in the document')

    for i in range (len(sorted_list)):
        for key, value in sorted_list[i].items():
            if key.isalpha() == True:
                print(f"The '{key}' character was found {value} times")

    print('--- End report ---')


main()