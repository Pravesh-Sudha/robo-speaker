import os


if __name__ == '__main__':
    print("Welcome to Robo-Speaker 1.1. Created by Pravesh-Sudha")
    while True:
        x = input("Enter what you want me to Speak: ")
        if x == "q":
            break
        command = f'espeak "{x}"'
        os.system(command)
