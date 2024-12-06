import random


text = input("enter everybody's name seprated by commas : ")
text_slipt = text.split(",")
#print(text_slipt)
#lenght = len(text_slipt)
#random_choice = random.randint(0,lenght-1)
#print(f"{text_slipt[random_choice]} will pay the bill")
print(f"{random.choice(text_slipt)} will pay the bill")
