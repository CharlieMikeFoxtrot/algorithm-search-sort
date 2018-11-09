#Please Pass the Coded Messages
#==============================
#
#You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.
#
#You have L, a list containing some digits (0 to 9). Write a function answer(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.
#
#Languages
#=========
#
#To provide a Python solution, edit solution.py
#To provide a Java solution, edit solution.java
#
#Test cases
#==========
#
#Inputs:
#    (int list) l = [3, 1, 4, 1]
#Output:
#    (int) 4311
#
#Inputs:
#    (int list) l = [3, 1, 4, 1, 5, 9]
#Output:
#    (int) 94311
#
#Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.


# l = [3, 1, 4, 1, 5, 9]
# 954311
# 954131
# 954113
# 951413
# 951143


# l = [3,7,4,5,8]
# 847543

def perm(x):

    if len(x) <=1:
        return [x]
    ret = []
    for i, n in enumerate(x):
        for r in perm(x[:i]+x[i+1:]):
            ret.append([n]+r)
    return ret

           

def answer(L):

    L = sorted(L, reverse = True)
    if int(''.join(map(str,L))) % 3 == 0:
        print('found')
        return int(''.join(map(str,L)))
    
    print(L)
    len(L)
    perms = perm(L)
    perms = sorted(perms, reverse = True)
    print(perms.count([1, 1, 3, 5, 4, 9]))

    while len(perms[0])>0:  
        for i in range(len(perms)):
            number = int(''.join(map(str,perms[i])))

            if number %3 == 0:
                return number
            if perms[i].count(perms[i][:len(perms[i])-1]) == 0:   
                perms[i] = perms[i][:len(perms[i])-1]
            else:
                del perms[i]
                print(perms(len))

    return 0