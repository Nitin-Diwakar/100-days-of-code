def counts(sen):
    global letter,digit
    letter = digit = 0
    for check in sen:
        if check.isdigit():
            digit+=1
        elif check.isalpha():
            letter+=1
        else:
            pass
    return letter,digit
    
sentence = input('>>> ')
counts(sentence)
print("Letters:",letter)
print("Digits:",digit)
