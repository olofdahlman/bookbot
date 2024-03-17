
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #The print function will print alot of text, the entire book; uncomment it at your own leisure
        #print(file_contents)
        words = file_contents.split()

        word_count = 0
        for word in words:
            
            word_count += 1

        print(word_count)

main()