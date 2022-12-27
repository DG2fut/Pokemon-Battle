import time
import numpy as np
import sys

# Delay print function
# for style purposes only

def delay_print(s):
    #print one character at a time
    #imported from stackoverflow.com
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Creating pokemon class

class Pokemon:
    def __init__(self,name,types,moves,EVs,health="===================="):
        # pokemon attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs["ATTACK"]
        self.defense = EVs["DEFENSE"]
        self.health = health
        self.bars = 20 # max hp of 20 bars

    #function to initiate fight
    def fight(self,P2):
        #displaying fight info
        print("---- BATTLE START ----")
        #first pokemon
        print(f"\n{self.name}")
        print("TYPE: ",self.types)
        print("ATTACK: ",self.attack)
        print("DEFENSE: ",self.defense)
        #uses numpy mean function to determine lvl based on atk and def
        print("LVL: ", 3*(1+np.mean([self.attack,self.defense])))

        print("\nVS")

        print(f"\n{P2.name}")
        print("TYPE: ",P2.types)
        print("ATTACK: ",P2.attack)
        print("DEFENSE: ",P2.defense)
        print("LVL: ", 3*(1+np.mean([P2.attack,P2.defense])))

        #pauses for 2 seconds
        time.sleep(2)

    #type advantages
        typelist = ["Fire","Water","Grass"]


        for i,k in enumerate(typelist):
            if self.types == k:
                # Both are same type
                if P2.types == k:
                    attack_1 = "\nIts not very effective..."
                    attack_2 = "\nIts not very effective..."

                # If p2 > p1
                if P2.types == typelist[(i+1)%3]:
                    # %3 is used so index does not go out of bounds
                    P2.attack *= 2
                    P2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    attack_1 = "\nIts not very effective..."
                    attack_2 = "\nIts super effective!"

                # If p1 > p2
                if P2.types == typelist[(i+2)%3]:
                    P2.attack /= 2
                    P2.defense /= 2
                    self.attack *= 2
                    self.defense *= 2
                    attack_2 = "\nIts not very effective..."
                    attack_1 = "\nIts super effective!"
                
        # Fight mechanics
        # Loop continues until one pokemon faints
        while (self.bars > 0) and (P2.bars > 0):
            # Each pokemon health
            print(f"{self.name}\t\tHP\t{self.health}")
            print(f"{P2.name}\t\tHP\t{P2.health}")

            print(f"GO {self.name}!")
            for i,x in enumerate(self.moves):
                #picking move
                print(f"{i+1}.",x)
            choice = int(input("Pick a move:"))
            delay_print(f"\n{self.name} used {self.moves[choice-1]}!")
            time.sleep(1)
            delay_print(attack_1)

            #determining damage
            P2.bars -= self.attack
            P2.health = ""

            # Add back bars plus defense boost
            for j in range(int(P2.bars+1*P2.defense)):
                P2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHP\t{self.health}")
            print(f"\n{P2.name}\t\tHP\t{P2.health}")
            time.sleep(0.5)

            # Check if pokemon fainted
            if P2.bars <= 0:
                delay_print("\n..." + P2.name + " fainted.")
                break
            
            print(f"Go {P2.name}!")
            for i, x in enumerate(P2.moves):
                print(f"{i+1}.", x)
            choice = int(input("Pick a move: "))
            delay_print(f"\n{P2.name} used {P2.moves[choice-1]}!")
            time.sleep(1)
            delay_print(attack_2)

            # Determine damage
            self.bars -= P2.attack
            self.health = ""

            
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHP\t{self.health}")
            print(f"\n{P2.name}\t\tHP\t{P2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + " fainted.")
                break
        
        # random amt between 1 to 5000
        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.")



if __name__ == "__main__":
    # Creating pokemon (input)
    Charizard = Pokemon("Charizard","Fire", ["Flamethrower","Fly","Blast Burn","Fire Punch"], {"ATTACK":12,"DEFENSE":8})
    Blastoise = Pokemon("Blastoise", "Water", ["Water Gun", "Bubblebeam", "Hydro Pump", "Surf"],{"ATTACK": 10, "DEFENSE":10})
    Venusaur = Pokemon("Venusaur", "Grass", ["Vine Whip", "Razor Leaf", "Earthquake", "Frenzy Plant"],{"ATTACK":8, "DEFENSE":12})

    Charmander = Pokemon("Charmander", "Fire", ["Ember", "Scratch", "Tackle", "Fire Punch"],{"ATTACK":4, "DEFENSE":2})
    Squirtle = Pokemon("Squirtle", "Water", ["Bubblebeam", "Tackle", "Headbutt", "Surf"],{"ATTACK": 3, "DEFENSE":3})
    Bulbasaur = Pokemon("Bulbasaur", "Grass", ["Vine Whip", "Razor Leaf", "Tackle", "Leech Seed"],{"ATTACK":2, "DEFENSE":4})

    Charmeleon = Pokemon("Charmeleon", "Fire", ["Ember", "Scratch", "Flamethrower", "Fire Punch"],{"ATTACK":6, "DEFENSE":5})
    Wartortle = Pokemon("Wartortle", "Water", ["Bubblebeam", "Water Gun", "Headbutt", "Surf"],{"ATTACK": 5, "DEFENSE":5})
    Ivysaur = Pokemon("Ivysaur\t", "Grass", ["Vine Whip", "Razor Leaf", "Bullet Seed", "Leech Seed"],{"ATTACK":4, "DEFENSE":6})

    # calling fight
    Charizard.fight(Venusaur) #eg
