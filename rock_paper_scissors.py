import random


def play():
    switcher = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }
    print(switcher)  
    i = input("Enter Your Choice: ") 
    p = switcher.get(int(i))
    print("The Player Has Selected: " +p)
    i = random.randint(1,3)
    c = switcher.get(i)
    print("The Computer has Selected: " +c)

    if p==1 and c==3:
        print('you win against the computer \n')
    elif p==3 and c==1:
        print('you lose against the computer \n')
    elif p>c:
        print('you win against the computer \n ')
    elif p<c:
        print('you lose against the computer \n')
    elif p==c:
        print( 'you tie against the computer\n')
    
    
play()
