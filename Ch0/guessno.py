from random import uniform

myNumber = int(uniform(2, 99))
noGuess = 1

while noGuess:
    urNumber = int(input('guess 1~99 number? --> '))
    if urNumber < myNumber:
        print("...(~_~) small")
    elif urNumber > myNumber:
        print("......big (^_-")
    else:
        print("u got it \\(^o^)/ play again")
        break
