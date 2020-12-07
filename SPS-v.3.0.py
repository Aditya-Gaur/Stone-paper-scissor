#This is just a prototype. It runs but it is far from completion.
import random
import pyttsx3
import speech_recognition as sr
import time

def listen():
    try:
        with sr.Microphone() as source:
            print('Listnening...')
            sr.Recognizer().adjust_for_ambient_noise(source, duration=0.1)
            i = sr.Recognizer().record(source, duration = 3)
            
        print('Recognizing..\n')
        return sr.Recognizer().recognize_google(i)
    except:
        print('Could not understand audio.\nTry checking your mic\n')
        engine.say('Could not understand audio, Try checking your mic')
engine = pyttsx3.init()
engine.setProperty('rate', 180)

engine.say('Welcome to the Game , Press enter to continue')
engine.runAndWait()
print(input('Press enter to continue'))

engine.setProperty('rate', 170)
engine.say('You can either enter your choice or, say your choice to play')
engine.runAndWait()

engine.setProperty('rate', 200)
W = 0
L = 0

while True :
        o = random.randint(0,2)
        engine.say('RockPaperscissor')
        engine.runAndWait()

        k = str(listen())
        print(k)
             
        if o == 0:
            this = 'rock'
        elif o == 1:
            this = 'paper'
        else:
            this = 'scissor'


        acpt_cmd = ['rock', 'paper', 'scissor']

        if k not in acpt_cmd:
            engine.say('Say Rock, Paper or scissor')
            engine.runAndWait()
            print('Say Rock, Paper or scissor\n')
        elif k == this :
            engine.say('You win')
            engine.runAndWait()
            print('You win\n')
        elif k != this:
            engine.say('You loose')
            engine.runAndWait()
            print('You loose')
            engine.say(f'I chose {this}')
            engine.runAndWait()
            print(f'I chose {this}\n')
        else:
            pass
        
        while k not in acpt_cmd:
            try:    
                i = int(input('Enter your choice for now :\n0 for Rock\n1 for Paper\n2 for Scissor\n:->'))
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
                        break
                    else:
                        engine.say('You loose')
                        engine.runAndWait()
                        print('You loose')
                        engine.say(f'I chose {this}')
                        engine.runAndWait()
                        print(f'I chose {this}\n')
                        L += 1
                        print(f'Wins = {W}, Loses ={L}\n')
                        break
            
                elif i == 1:
                    if o == 0:
                        engine.say('You win')
                        engine.runAndWait()
                        print('You win\n')
                        W += 1
                        print(f'Wins = {W}, Loses ={L}\n')
                        break
                    else:
                        engine.say('You loose')
                        engine.runAndWait()
                        print('You loose')
                        engine.say(f'I chose {this}')
                        engine.runAndWait()
                        print(f'I chose {this}\n')
                        L += 1
                        print(f'Wins = {W}, Loses ={L}\n')
                        break
            
                elif i == 2:
                    if o == 1:
                        engine.say('You win')
                        engine.runAndWait()
                        print('You win\n')
                        W += 1
                        print(f'Wins = {W}, Loses ={L}\n')
                        break
                    else:
                        engine.say('You loose')
                        engine.runAndWait()
                        print('You loose')
                        engine.say(f'I chose {this}')
                        engine.runAndWait()
                        print(f'I chose {this}\n')
                        L += 1
                        print(f'Wins = {W}, Loses ={L}\n')
                        break
            except:
                engine.say('Invalid intput')
                engine.runAndWait()
                print('Invalid Input\n')
            

