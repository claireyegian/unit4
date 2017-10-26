#Claire Yegian
#10/26/17
#stringUnion.py - takes two strings and returns all letters that appear in either word

def stringUnion(word1,word2):
    string = ''
    for ch in word1 + word2:
        if not ch.lower() in string:
            string = string+ch.lower()
    return string

print(stringUnion('Mississippi','Pensylvania'))

