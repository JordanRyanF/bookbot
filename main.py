def main(): 
    book_path = "books/frankenstein.txt"    
    text = get_book_text(book_path) 
    num_words = get_num_words(text) 
    letter_counter = get_letter_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document") 
    print("")
    letter_counter_list = [{"char": k, "num": v} for k, v in letter_counter.items()]
    letter_counter_list.sort(reverse=True, key=sort_on)
    for char in letter_counter_list:
        if char.get("char").isalpha():
            print(f"The '{char.get("char")}' character was found {char.get("num")} times")
    print("--- End report ---")
    

def get_num_words(text):
    words = text.split() 
    return len(words) 
    
def get_book_text(path): 
    with open(path) as f: 
        return f.read() 
    
def get_letter_count(text): 
    lowered_string = text.lower() 
    letter_count = {} 

    for letter in lowered_string: 
        if letter not in letter_count: 
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1 
    return letter_count 
def sort_on(char):
    return char["num"]


if __name__ == "__main__":
   
   main()

