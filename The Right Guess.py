import random

def guessit():   

    print(" **welcome** ")
    print("what you want to guess : number(n) or alphabet(a) ")
    y=input("enter :")
    if y=="n":
        guesnum()
    elif y=="a":
        guesschar()


def guesnum():
    val=random.randint(1,100)
    print(val)
    guess =0
    userinput=None
    while(userinput!=val):
        userinput=int(input("enter the value: "))
        if userinput==val:
            print(" >> you guessed it right <<")
        else:
            if userinput<val:
                print("you guessed it wrong : try larger number ")
                if (userinput-5) <val <(userinput+5):
                    print("you are close to it")
            else:         
                print("you guessed it wrong : try smaller number ")
                if (userinput-5) <val <(userinput+5):
                    print("you are close to it")    
            guess+=1
    print(f"---> you guess the num in {guess} guesses")   

def guesschar():
    st="abcdefghijklmnopqrstuvwxyz"
    val=random.choice(st)
    print(val)
    guess =0
    userinput=None
    while(userinput!=val):
        userinput=input("enter the value:  ")
        if userinput==val:
            print(" >> you guessed it right <<")
        else:
            if userinput<val:
                print("you guessed it wrong : try larger number ")
            else:         
                print("you guessed it wrong : try smaller number ")
            guess+=1
    print(f"---> you guess the alphabet in {guess} guesses")
print("welcome  to 'guess it right'")
print('''howmany time you want to play :
single [enter :1]
num of time [enter : any num]
endless [enter: 0]      ''')
p=int(input("enter >> "))
if p==1:
 guessit()
 print("Have a good day!")
elif p== "e" :
    while (5<6):
        guessit()   
else:
    for i in range(p):
        guessit()



   
