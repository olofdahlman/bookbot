
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_content = file_contents.lower()
        #The print function will print alot of text, the entire book; uncomment it at your own leisure
        #print(file_contents)
        words = file_content.split()

        #This for loop counts words in the text via the "words" list
        word_count = 0
        for word in words:
            
            word_count += 1

        print(f"Number of words: {word_count}")

        #This dictionary and following for loops count the different characters used in the text
        
        letter_count = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"m":0,"n":0,"g":0,"h":0,
                        "k":0,"l":0,"j":0,"i":0,"t":0,"y":0,"u":0,"w":0,"q":0,"r":0,
                        "s":0,"o":0,"p":0,"z":0,"x":0,"v":0,".":0,"!":0,"?":0,"-":0,
                        "'":0,'"':0,";":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,
                        "7":0,"8":0,"9":0,":":0,"(":0,")":0,"*":0,",":0}
        
        nonletter_characters = 0
        formatting_characters = 0

        for word in words:
            for i in word:
                if i in letter_count:
                    letter_count[i] += 1
                else: 
                    #This section contains supplementary code to catch and count formatting type character from text line if a whole text rather than strings are used
                    #Edit the comments out and update the for loop to use the text rather than the "words" list
                    #if not i == (" ") or not i == ("\n") or not i == ("\r"):
                    nonletter_characters += 1
                   
                    #else:
                        #if i == (" ") or i == ("\n") or i == ("\r"):
                                 #formatting_characters += 1
                        #else:
                            #print("Error: non-string character detected")


        for letter in letter_count:
            
            print(f"Number of {letter} characters: {letter_count[letter]}")

        print(f"Number of other characters: {nonletter_characters}")
        #print(f"Number of file formatting characters like '\ n' and '\ r': {formatting_characters}")

main()