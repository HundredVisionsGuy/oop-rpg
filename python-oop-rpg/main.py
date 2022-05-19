# main.py
# The main game might go here
# for now, let's just test some stuff

# import our object
import Character 

# test our code
if __name__ == '__main__':
    # Create a character
    player1 = Character.Player("Benaconda", 300)

    # print the character
    print(player1.name)
    print(player1.get_stats())