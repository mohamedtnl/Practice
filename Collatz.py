def collatz(number) :
    while True:
        if number == 1:
            print(number)
            return 1
        elif number % 2 == 0:
            print(number)
            number = number // 2
        elif number % 2 != 0:
            print(number)
            number = 3 * number + 1

def collatz_test():
   while True:
       try :
           if collatz(int(input("Which number : "))) == 1 :
               break



       except :
           print("Use an integer")


collatz_test()

"""Written by Mohamed Taouil"""