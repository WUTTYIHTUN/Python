numbers = int(input('1から100までの数値を入力してください'))

if numbers < 1 or numbers > 100:
    print("It's Error.Please write correct number.")
elif numbers % 3 == 0:
    print("Fizz")
elif numbers % 5 == 0:
    print("Buzz")
elif numbers % 3 == 0 and numbers % 5 == 0:
    print("FizzBuzz")
else:
    print("Nothing in here.")