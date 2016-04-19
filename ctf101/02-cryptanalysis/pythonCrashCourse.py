##############################################################
# This is a utility file to help with laboratory exercises in
# the "Understanding Cryptology: Cryptanalysis" course offered
# by Dr. Kerry McKay
# Hosted at OpenSecurityTraining.info under a CC BY-SA license
# http://creativecommons.org/licenses/by-sa/3.0/
##############################################################

import random


x=5
y=0

# this is a comment

# different ways of printing
print "x =", x, ",  y =", y         #simple
print "x={0}, y={1}".format(x,y)    #preferred


#analogous C code
# for(int i=0; i<4; i++) {
#   y = y + x;
#   printf("x=%d, y=%d, i=%d\n", x, y, i);
# }
for i in range(0,4):
    #this needs to be indented
    y = y + x       
    print "x={0}, y={1}, i={2}".format(x,y, i)

    # an if example
    if y < 15:
        print "y is less than 15"
    elif y==15:
        print "y is 15"
    else:
        print "y is greater than 15"



#define a function (define function before calling it)
def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

#call factorial 
x=0
f=0
print "\nfactorial:"
while f<100:
    f = factorial(x)
    print f
    x=x+1


#fun with lists:
myList = []     #blank list
myList.append('a') #add to the end
myList.append('b')
myList.append('c')
print "myList: {0}".format(myList)
print "myList[1]: {0}".format(myList[1])
myList[1] = myList[2]
print "copy third element to second"
print "myList: {0}".format(myList)

#set list value
myList = ['a', 'b', 'c']
print "reset"
print "myList: {0}\n".format(myList)


# fun with strings
myString = "hello"
for i in range(len(myString)):
    # 0 is implied start of range
    # len is length function
    print myString[i]

print

# dictionaries: key-value pairs
d = dict()
d['banana'] = "fruit"
d['carrot']= "veggie"
print d
for k in d.keys():
    print "A {0} is a {1}".format(k, d[k])


# choosing random integers
print
for i in range(5):
    print random.randint(1,5) #random int 1<=a<=5

