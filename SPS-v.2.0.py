import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)

engine.say('Welcome to the Game , Press enter to continue')
engine.runAndWait()
print(input('Press enter to continue'))

engine.setProperty('rate', 200)
W = 0
L = 0

engine.say('Choose 0, 1 and 2 for rock paper and scissor')
engine.runAndWait()

while True :
    try:
        o = random.randint(0,2)
        if o == 0:
            this = 'Rock'
        elif o == 1:
            this = 'Paper'
        else:
            this = 'Scissor'
        engine.say('Enter your choice')
        engine.runAndWait()
        i = int(input('Enter your choice :\n0 for rock\n1 for paper\n2 for scissor\n:->'))
        if i == o :
            engine.say('Its a tie')
            engine.runAndWait()
            print('Its a tie\n')
            W += 0
            print(f'Wins = {W}, Loses ={L}\n')
            
        elif i > 2:
            engine.say('Choose 0, 1 or 2')
            engine.runAndWait()
            print('Choose 0, 1 or 2\n')
            print(f'Wins = {W}, Loses ={L}\n')
        elif i == 0:
            if o == 2:
                engine.say('You win')
                engine.runAndWait()
                print('You win\n')
                W += 1
                print(f'Wins = {W}, Loses ={L}\n')
            else:
                engine.say('You loose')
                engine.runAndWait()
                print('You loose')
                engine.say(f'I chose {this}')
                engine.runAndWait()
                print(f'I chose {this}\n')
                L += 1
                print(f'Wins = {W}, Loses ={L}\n')
            
        elif i == 1:
            if o == 0:
                engine.say('You win')
                engine.runAndWait()
                print('You win\n')
                W += 1
                print(f'Wins = {W}, Loses ={L}\n')
            else:
                engine.say('You loose')
                engine.runAndWait()
                print('You loose')
                engine.say(f'I chose {this}')
                engine.runAndWait()
                print(f'I chose {this}\n')
                L += 1
                print(f'Wins = {W}, Loses ={L}\n')
            
        elif i == 2:
            if o == 1:
                engine.say('You win')
                engine.runAndWait()
                print('You win\n')
                W += 1
                print(f'Wins = {W}, Loses ={L}\n')
            else:
                engine.say('You loose')
                engine.runAndWait()
                print('You loose')
                engine.say(f'I chose {this}')
                engine.runAndWait()
                print(f'I chose {this}\n')
                L += 1
                print(f'Wins = {W}, Loses ={L}\n')

    except:
        engine.say('Invalid Input')
        engine.runAndWait()
        print('Invalid Input\n')
        print(f'Wins = {W}, Loses ={L}\n')


