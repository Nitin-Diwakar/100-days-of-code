
"""Write a Python program for sequential search.
Sequential Search: In computer science, linear search or sequential search
is a method for finding a particular value in a list that checks each element in sequence until the desired element is
found or the list is exhausted. The list need not be ordered."""

def Sequential_Search(dlist, item):

    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos

print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))
