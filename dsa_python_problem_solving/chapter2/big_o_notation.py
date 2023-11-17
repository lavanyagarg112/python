'''
Write two Python functions to find the minimum number in a list. The first function should compare each number to 
every other number on the list. 
O(n^2). The second function should be linear. O(n).
'''

def minnum(xs):
    overallmin = xs[0]
    for i in xs:
        issmallest = True # initialise every i to be small, then check with every other element (j)
        for j in xs:
            if i > j:
                issmallest = False

        if issmallest:
            overallmin = i # if this initialised i is still smallest, then overallmin is now my i
            # it is because of the use of boolean issmallest that we say this is O(n^2) as we compare i to everything
            # if we simply make issmallest the smallest element everytime we encounter a smaller element, at the end of one for loop
            # we will have the smallest
            # the next one basically
            # it is because here we are not storing it that we have to check everytime
    return overallmin

def minnum2(xs):
    if xs != []:
        min = xs[0]
    else:
        return "Empty list"
    for i in xs[1:]:
        if i < min:
            min = i

    return min


'''
usually trade off needs to be made between order of growth of space and order of growth of time
'''

        