unwanted_chars = ["\"", ":", ";", ",", ".", "-", "+", "=",
                  "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]


def word_count(s):
    # Your code here
    dict_of_words = {}

    for word in s.split():
        for i in unwanted_chars:
            word = word.replace(i, '')
        if word.lower() in dict_of_words:
            dict_of_words[word.lower()] += 1
        else:
            dict_of_words[word.lower()] = 1

    if len(dict_of_words) == 1 and '' in dict_of_words:
        dict_of_words = {}
    return dict_of_words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
