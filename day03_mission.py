# 6.2
guess_me = 5

for number in range(10):
    print("number is ", number)
    if number > guess_me:
        print("oops")
        break
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("too low")