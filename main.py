def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count_of_chars = count_by_character(text)
    #print(f"{num_words} words found in the document")
    #print(count_of_chars)
    report(num_words, count_of_chars, book_path)
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()  
    
def get_num_words(text):
    words = text.split()
    return len(words)

def count_by_character(text_list):
    count_of_char = {}
    for i in text_list:
        for letter in i:
            if letter.lower() not in count_of_char and letter.lower().isalpha():
                count_of_char[letter.lower()] = 1
            elif letter.lower().isalpha(): 
                count_of_char[letter.lower()] += 1
    new_dict = sorted(count_of_char.items(), key=lambda x:x[1], reverse=True)
    print(new_dict)
    return new_dict

def report(word_count:int, char_count:dict, book_path:str):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document \n")
    for letter in char_count:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End Report ---")    

main()