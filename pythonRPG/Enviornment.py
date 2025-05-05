import random
class Enviornment:
    def __init__(self):
        self.day = 1
        self.floor = 0
        self.weather = ""
    
    def changeFloor(self, bossKilled):
        if bossKilled == False:
            pass
        elif bossKilled == True:
            print(f"You have made it to floor {self.floor}!")
            floor += 1
    def nextDay(self):
        self.day += 1

    def changeWeather(self):
        weather = ["sunny", "rainy", "snowy", "stormy"]
        self.weather = random.choices(weather, weights=[0.7, 0.1, 0.05, 0.15], k=1)[0]
        if(self.weather == "sunny"):
            print("It is sunny today!")
        elif(self.weather == "rainy"):
            print("It is rainy today!")
        elif(self.weather == "snowy"):
            print("It is snowy today!")
        elif(self.weather == "stormy"):
            print("It is stormy today!")

    def checkOutside(self):
        if self.floor > 0:
            print("You are in a dungeon")
        else:
            self.changeWeather()