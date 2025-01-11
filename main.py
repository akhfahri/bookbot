def main():
    #get book text
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # count words
    word_list = text.split()
    word_count = len(word_list)
    # print (len(word_list))
    # print(word_list)

    # count characters
    character_count = count_characters(text)
    # print(character_count)

    print_report(book_path, word_count, character_count)

def get_book_text(path):
    with open(path)as f:
        return f.read()

def count_characters(text):
    text_lowercase = text.lower()
    output_dict = {}

    for i in text_lowercase:
        if i in output_dict:
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    
    return output_dict

def print_report(book_path, word_count, count_dict):
    output_string = f"--- Begin report of {book_path} ---\n"
    output_string += f"{word_count} words found in the document\n\n"
    sorted_dict = {k: v for k, v in sorted(count_dict.items(), key=lambda item: item[1], reverse=True) if k.isalpha()}

    for i in sorted_dict:
        output_string += f"The '{i}' character was found {count_dict[i]} times\n"

    output_string += "--- End report ---"

    print(output_string)


main()