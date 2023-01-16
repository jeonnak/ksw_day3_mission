# 6.2
guess_me = 7
number = 1

while number > 0:
    print("number is ", number)
    if number > guess_me:
        print("oops")
        break
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("too low")
        number += 1