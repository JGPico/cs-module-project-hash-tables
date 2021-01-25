def no_dups(s):
    # Your code here
    dup_words = {}
    output = ''
    first_iter = True

    for word in enumerate(s.split()):
        if word[1] not in dup_words:
            dup_words[word[1]] = word[1]
            if first_iter:
                output = word[1]
                first_iter = False
            else:
                output = output + " " + word[1]

    # for i in dup_words:
    #     print("dup words at i", dup_words[i])
    #     s.replace(dup_words[i], '')

    return output


print("cats dogs fish")

if __name__ == "__main__":
    # print(no_dups(""))
    # print(no_dups("hello"))
    # print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    # print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
