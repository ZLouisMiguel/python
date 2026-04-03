#Exercise to practice basics
import random

user_name = input("What is your name ? : ")

greetings = ["Hello there, {}" , "Yoo!! Wassup {}" , "Konnichiwa, {}-desu!"]

random_index = random.randint(0,len(greetings)-1)
    
print(greetings[random_index].format(user_name))

