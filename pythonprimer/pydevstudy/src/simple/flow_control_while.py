'''
Created on 2010-6-27

@author: me
'''
import traceback

NUMBER = 23
RUNNING = True
def whileSimple():
    global NUMBER
    global RUNNING
    
    while RUNNING :
        try :
            guess = int(raw_input("Enter an integer, input 23 exit:"))
        except Exception,e:
            #print e
            print traceback.format_exc()
            continue
            
        if guess == NUMBER :
            print "Congratulations, you guessed it."
            RUNNING = False
            print 'whileSimple successful finish.'
        elif guess > NUMBER :
            print "No, it is a little lower than that!"
        else :
            print "No, it is a little higher than that!"
            
    else :
        print "The while else you want to do here"
    
def whileTest():
    while True :
        #s = input("Enter a something:")
        s = raw_input("Enter a something, enter 'quit' exit:")
        if s == "quit" or s == "QUIT" or s == "Q" :
            break
        elif len(s) < 3:
            continue
        print "Length of the string is ", len(s)
    print "Done" 


if __name__ == '__main__':
    whileSimple()
    whileTest()