def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_character = character_count(text)
    characters_sorted_list = sort_dict(num_character)

    print (f"--- Begin report of {book_path} ---")
    print (f"{num_words} found in the document")
    print ()

    for item in characters_sorted_list:
        if not item["char"].isalpha():
            continue
        print (f"The '{item['char']}' character was found {item['num']} times")
           
    print ("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_dict = {}
    for i in text:
        lower_case = i.lower()
        if lower_case in character_dict:
            character_dict[lower_case] += 1
        else:
            character_dict[lower_case] = 1
    return character_dict

def sort_on(d):
    return d["num"]

def sort_dict(new_dict):
    sorted_list = []
    for i in new_dict:
        sorted_list.append({"char": i, "num": new_dict[i]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
     
main()

