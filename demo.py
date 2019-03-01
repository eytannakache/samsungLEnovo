import random

print("my two laptops project")
print("another line")


def whos_num_bigger(user_num):
    laptop_num = random.randint(0, 10)

    if laptop_num < user_num:

        print("your num is bigger \n I tought about {}".format(laptop_num))

    else:
        print("my num is bigger\n I tought about {}".format(laptop_num))


whos_num_bigger(int(input(" give me number between 0-10:  \n")))
