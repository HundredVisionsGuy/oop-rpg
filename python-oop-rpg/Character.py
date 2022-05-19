# TODO:
# 1. Practice inheritance - with Character Class
#       allow us to have players AND NPCs that share 
#       traits
# 2. Add some stats generation code
# 3. Add to .gitignore


class Player:
    # Init function (when an object is created)
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_stats(self):
        return f"Name: {self.name}\nAge: {self.age}"


## Credits:
# https://www.drivethrurpg.com/product/349171/Micro-Chapbook-RPG-Full-Page-Character-Sheet
# The 6 Stats: https://tvtropes.org/pmwiki/pmwiki.php/Main/TheSixStats
# Real Python article: https://realpython.com/python3-object-oriented-programming/#classes-vs-instances