def word_count(text):
    words = text.split()
    wordcount = len(words)
    return wordcount
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = word_count(file_contents) 
        print(num_words)
if __name__ == "__main__":
    main()