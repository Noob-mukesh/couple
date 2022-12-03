from faker import Faker

#  IMPORT FAKER MODULES IN YOUR PC OR MOBILE
#  pip install faker
#  THIS PROGRAM WILL FIND YOUR COUPLE  YOU JUST NEED TO CHOOSE YOUR GENDER AND ENTER NAME
fake = Faker()

F = fake.first_name_female()

M = fake.first_name_male()

#  SELECT YOUR GENDER M FOR MALE OR F FOR FEMALE

enter = input('''Select your Gender!
       M:---- for Male
       F:--- for Female \t''')

if "M" in enter:

    #  HERE  BOY WILL ENTER  HIS NAME!

    PRINCE = "Enter your name I will find your princess 💖\t"

    M = input(PRINCE)

elif "F" in enter:

    #  HERE GIRL WILL ENTER HIS NAME!

    PRINCESS = "Enter your name I will find your Prince💖\t"

    F = input(PRINCESS)

elif input.str("M", "F") not in enter:

    print("try again")

else:

    print("wrong input")

#  Made  legend Mukesh @mr_sukkun

# THIS  DICTONARY IS FOR BOYS

couple1 = {M: F, "mukesh": "khushi", "Mukesh": "Khushi", "MUKESH": "KHUSHI"}
#  THIS DITCONARY IS FOR GIRLS

couple = {F: M, "khushi": "mukesh", "Khushi": "Mukesh", "KHUSHI": "MUKESH"}

if M in couple1:
    #  THIS WILL PRINT YOUR NAME AND UR GF

    print(M, "💖,", couple1[M], "is your Girlfriend ")

elif F in couple:

    #  THIS WILL PRINT YOUR NAME AND UR BOYFRIEND

    print(F, "💖", couple[F], "is your Boyfriend")
else:
    #  wont  run in any condition wtever is your name sabko princess ya prince milega

    print("you can't be single  🤣 sabko mil gya ")
