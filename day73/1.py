def check(w):
    if len(w) < 3:
        return w
    else:
        if w[-3:] == 'ing':
            return (w+'ly')
        else:
            return (w+'ing')

word = input("Enter any string: ")

print(check(word))    
