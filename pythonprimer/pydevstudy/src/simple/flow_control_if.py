'''
Created on 2010-6-27

@author: me
'''
number = 23
guess = int(raw_input("Enter a Integer:"))

if guess > number :
    print "No, it is a little lower than that!"
elif guess == number :
    print "Congratulations, you guessed it."
else :
    print "No, it is a little higher than that!"
    
n = 5
if n in [1,4,5,6]:
    print 'find n!'