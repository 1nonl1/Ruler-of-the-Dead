import random
class Enviornment:
    def __init__(self):
        self.day = 1
        self.floor = 0
        self.weather = ""
    
    def changeFloor(self, bossKilled, team):
        if bossKilled == False:
            pass
        elif floor == 1000 and bossKilled == True:
            print("You've come a long way! ")
            print("You've defeated the final boss!")
            if team == True:
                print("As you start to celebrate with your team, you start to feel something surging inside you.")
                print("It feels as though `fjpabkwp uzj jbfakkbjwu az jokh`.")
                print("Before you know it, you lash out at your team.")
                print("You `Ghhh uhbb` before they can even react!")
                print("`Ku zjjhg hkgj cady fakc kg aw zkyj xg cady ggkw udywg yjk, xwk cad pyae x zayw`")
                print("`Fjn xed kqd Enide ju kqd Odxo`")
            else:
                print("As you start to celebrate you start to feel something surging inside you.")
                print("It feels as though you are `fjpabkwp uzj jbfakkbjwu az jokh`.")
                print("`Ku zjjhg hkgj cady fakc kg aw zkyj xg cady ggkw udywg yjk, xwk cad pyae x zayw`")
                print("`Fjn xed kqd Enide ju kqd Odxo`")
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