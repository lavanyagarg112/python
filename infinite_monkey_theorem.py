'''
Here's a self check that really covers everything so far. You may have heard of the infinite monkey theorem? 
The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost 
surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python 
function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence 
we'll shoot for is: “methinks it is like a weasel”

You're not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we'll simulate this is to 
write a function that generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet 
plus the space. We'll write another function that will score each generated string by comparing the randomly generated string to 
the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters 
are not correct then we will generate a whole new string.To make it easier to follow your program's progress this third function 
should print out the best string generated so far and its score every 1000 tries.
'''

import string
import random

lowercase_letters = list(string.ascii_lowercase)
lst = lowercase_letters + [" "]
goal = "methinks it is like a weasel"

def generate():
    sentence = ""
    for i in range(28):
        index = random.randint(0,26)
        sentence += lst[index]

    return sentence

def compare(sentence, goal):
    score = 0
    for i in range(28):
        if sentence[i] == goal[i]:
            score += 1
    return score

def call(score, count, sentence):

    while score != 28:

        if count == 10000: # rather than calling repititively, i am just trying to see how this works
            return(sentence,score)

        sen = generate()
        newscore = compare(sen, goal)

        if newscore == 28:
            return sen
        
        elif newscore > score:
            sentence = sen
            score = newscore
        count += 1



print(call(0,0,""))

'''
Challenge

See if you can improve upon the program in the self check by keeping letters that are correct and only modifying one 
character in the best string so far. This is a type of algorithm in the class of 'hill climbing' algorithms, that is we only 
keep the result if it is better than the previous one.
'''

