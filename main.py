def countletter(text):
    letmap = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    text = text.lower()
    for let in text:
        if let.islower():
            letmap[let] += 1
    return letmap
    # print(letmap)
    # print(letmap[letter])


def dicprint(dic):
    dic = dict(sorted(dic.items(), key=lambda item: -item[1]))
    for val in dic:
        print("The \'%s\' character was found %d times" %(val, dic[val]))


def wordcount(text):
    words = text.split()
    return (len(words))


def report(text):
    print("--- Begin report of books/frankenstein ---")
    print("%d words found in the document\n" %(wordcount(text)))
    dicprint(countletter(text))
    print("--- End report ---")

def main():
    with open("./books/Fankenstein") as f:
        file_contents = f.read()
        # words = file_contents.split()
        # print(len(words))
        # print(countletter('p', file_contents))
        report(file_contents)


main()
