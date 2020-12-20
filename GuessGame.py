min = 1
max = 1000
guesses =1
input("Press enter to start")
while True:
    print("Guessing in the range of {} and {}".format(min,max))
    guess= min +(max - min)//2
    uservalue =  input("My guess is {}.\nShould I Guess Higher or Lower?"
    " \nPlease Enter h , l or c if my guess was right : ".format(guess).casefold())
    if uservalue == "h":
        min= guess+1
    elif uservalue =="l":
        max= guess-1
    elif uservalue =="c":
        print("Hurray!!! I've guessed it in {} attempts".format(guesses))
        break
    else:
        print("Can You Please enter only h or l or c")
    guesses +=1
