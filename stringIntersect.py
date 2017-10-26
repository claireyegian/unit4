#Claire Yegian
#10/26/17
#stringIntersect.py - returns all letters in both words

def stringIntersect(word1,word2):
    string = ''
    for ch in word1 + word2:
        if (not ch.lower() in string) and (ch.lower() in word1 and word2):
            string = string + ch.lower()
    return string

print(stringIntersect('Mississippi','Pensylvania'))
