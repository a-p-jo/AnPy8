#Python8Ball by a-p-jo , contact @ apjo@tuta.io

#N.O.T.E : I have used " print('')" for the '/n' or newline effect, for readability.

import random

advice = ['It is certain.','It is decidedly so.','Wihout a doubt.', 'Yes-definitely.','You may rely on it.','As I see it, yes.', 'Most Likely.','Outlook Good.','Yes.','Signs point to yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.','Cannot predict now.','Concentrate and ask again later.','Dont count on it.','My reply is no.','My sources say no.','Outlook not so good.','Very doubtful.']
# Collection of the standard resposes given by a standard 8-ball

def baller(): #actual function for in-random_choice-out cycle of 8ball after 1st iteration 
    print('')
    input('Thoguhfully input question and press ENTER : ')
    answer = random.choice(advice)
    print('')
    print('The 8-ball says : ',answer)
    print('')
def baller2(): # function with baller() along with Yes/No choices, actual function being called in for loop
    print('')
    choicer= input ('Do you have another question (Y/N) : ')
    if choicer=='Y' or choicer == 'y':
        baller()
    elif choicer =='N' or choicer == 'n':
        print('')
        print('Hopefully, the 8-ball has proven helpful to you. Come back later to ask again.')
        print('')
        input('Press ENTER to Retry')  # 'No' choice does not lead to exit, rather allows for retry.
    else:
        print('')
        print('Invalid Input')
        print('')
        input('Press ENTER to Retry')
def rrpt():
    print('')
    rpt = input('Ask another question ? (Y/N) : ') # function for invalid response in first Y/N question

    if rpt == 'Y' or rpt == 'y':
        print('You may ask a total of 7 more questions')
        baller()
        for i in range(6): 
            baller2()
        print('')
        print('Hopefully, the 8-ball has proven helpful to you.')
        print('All 7 availible attempts have been used up. Come back later to ask again.')
        print('')
        input('Press ENTER to exit.')

    elif rpt == 'N' or rpt == 'n':
        print('Hopefully, the 8-ball has proven helpful to you. Come back later to ask again.')
        print('')
        input('Press ENTER to exit')

    else:
        print('')
        print('Invalid Input')
        print('')
        input('Press ENTER to exit')
#---intro begin---
print('AnPy8 is an 8-ball written in Python.')
print('')
print('When you are indecisive, you may approach an 8-ball.')
print('8-balls may also be used to ask a question about the future.')
print(' ')
print('Concentrate deeply and frame a valid Yes or No question.')
print('')
#---intro end---

input('Ready ? Type in your query : ')
#Typing query optional, query not stored.
#Reply is generated randomly and has nothing to do with the question, like a real 8-ball.
      
answer = random.choice(advice) # A reply is picked at random from collection
print('')
print('The 8-ball says : ',answer)
print('')

rpt = input('Ask another question ? (Y/N) : ')

if rpt == 'Y' or rpt == 'y':
    print('')
    print('You may ask a total of 7 more questions') #arbitrary limit to max. no. of questions, added for authenticity
    baller()
    for i in range(6):
        baller2()
    print('')
    print('Hopefully, the 8-ball has proven helpful to you.')
    print('All 7 availible attempts have been used up. Come back later to ask again.') #Message after all 7 attempts exhausted.
    print('')
    input('Press ENTER to exit.')

elif rpt == 'N' or rpt == 'n':
    print('')
    print('Hopefully, the 8-ball has proven helpful to you. Come back later to ask again.')
    print('')
    input('Press ENTER to exit')  #the only y/n choice where 'No' terminates AnPy8

else: #for invalid input
    print('')
    print('Invalid Input')
    print('')
    input('Press ENTER to retry')
    rrpt() 
