import random

print(input('Press enter to continue'))

W = 0
L = 0

while True :
    try:
        o = random.randint(0,2)
        
        if o == 0:
            this = 'Rock'
        elif o == 1:
            this = 'Paper'
        else:
            this = 'Scissor'
        i = int(input('Enter your choice :\n0 for rock\n1 for paper\n2 for scissor\n:->'))
        if i == o :
            print('Its a tie\n')
            W += 0
            print(f'Wins = {W}, Loses ={L}\n')
            
        elif i > 2:
            print('Choose 0, 1 or 2\n')
            print(f'Wins = {W}, Loses ={L}\n')
        elif i == 0:
            if o == 2:
                print('You win')
                print(f'I choose {this}\n')
                W += 1
                print(f'Wins = {W}, Loses ={L}\n')
            else :
                print('You loose')
                print(f'I chose {this}\n')
                L += 1
                print(f'Wins = {W}, Loses ={L}\n')
        elif i == '1':
            if o == 0:
                print('You win')
                print(f'I choose {this}\n')
                W += 1
                print(f'Wins = {W}, Loses ={L}\n')
            else :
                print('You loose')
                print(f'I chose {this}\n')
                L += 1
                print(f'Wins = {W}, Loses ={L}\n')
        elif i == '2':
            if o == 1:
                print('You win')
                print(f'I choose {this}\n')
                W += 1
                print(f'Wins = {W}, Loses ={L}\n')
            else :
                print('You loose')
                print(f'I chose {this}\n')
                L += 1
                print(f'Wins = {W}, Loses ={L}\n')


    except:
        print('Invalid Input\n')
        print(f'Wins = {W}, Loses ={L}\n')

