import matplotlib.pyplot as plt

people = [23,44,11,22,16]
date = [1,2,3,4,5]


while True:

    choice = input()
    if choice == "exit":
        break

    if choice == "plot":
        print("plotting")
        plt.plot(date, people)
        plt.show()