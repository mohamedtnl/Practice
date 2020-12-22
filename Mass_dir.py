import os

def create_mass_dir():
    print("Your current working directory is " + os.getcwd())
    os.chdir(input("Type the directory where you want to create the folders "))
    b = []
    t = 0
    c = input("Typ de gemeenschappelijke naam voor de folders ")
    for i in range(int(input("type how many folders you want "))):
        b.append( c + "_" + str(i))
        os.makedirs(b[t])
        t = t + 1


create_mass_dir()

"""Written by Mohamed Taouil"""