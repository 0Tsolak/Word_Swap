def stringConvert( word ):
    if type(word) == type("a"):
        newWord = ''
        for i in range( (len(word) // 2) - 1,  (len(word) // 2) + 2 ):
            newWord += word[i]
        return newWord
    else:
        print("Type error")

str1 = "JhonJonPeat"
str2 = "JaSonAy"
print( stringConvert(str1) )
print( stringConvert(str2) )