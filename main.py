import numpy as np
import matplotlib.pyplot as plt


class Classmate:
    def __init__(self, name, section, fav_subject):
        self.name = name
        self.section = section
        self.fav_subject = fav_subject
    
    def introduce(self):
        print(f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.fav_subject}.")

classmates = [
    Classmate("Kristine", "Amethyst", "Math"),
    Classmate("Jean", "Amethyst", "Science"),
    Classmate("Hariette", "Amethyst", "English"),
    Classmate("Jubilee", "Amethyst", "Math"),
    Classmate("Vivian", "Amethyst", "History"),
    Classmate("Luisito", "Topaz", "Math"),
    Classmate("Renn", "Topaz", "Math"),
    Classmate("Josua", "Topaz", "Math")
]

while True:
    print("\n" + "="*40)
    print("1. Show All Classmates")
    print("2. Add New Classmate")
    print("3. Exit")
    print("="*40)
    
    choice = input("Choice: ")
    
    if choice == "1":
        print("\n--- CLASSMATES ---")
        for c in classmates:
            c.introduce()
    
    elif choice == "2":
        print("\n--- ADD NEW ---")
        n = input("Name: ")
        s = input("Section: ")
        f = input("Favorite Subject: ")
        classmates.append(Classmate(n, s, f))
        print(f"{n} added!")
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")