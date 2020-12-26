import random

    
xb = yb = 250

for i in range(20000):
    r = random.random()
    if r <= 0.25:
        xb +=1 1

    elif r >= 0.25 and r < 0.5:
        xb -= 1

    elif r >= 0.5 and r < 0.75:
        yb = yb + 1

    elif r >= 0.75 < 1.00:
        yb = yb -1

print("X coord is " + str(xb))
print("Y coord is "+ str(yb))


"""Written by Mohamed Taouil"""