# TODO:
# 1. Practice inheritance - with Character Class
#       allow us to have players AND NPCs that share 
#       traits
# 2. Add some stats generation code


class Player:
    # Init function (when an object is created)
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_stats(self):
        return f"Name: {self.name}\nAge: {self.age}"