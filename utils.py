import random

class Character:
    def __init__(self, name, health, attack_power, defense, special_move):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.special_move = special_move
        self.potions = 2

    def attack(self, opponent):
        crit_chance = random.randint(1, 5)  # 20% chance of critical hit
        damage = max(0, self.attack_power - opponent.defense + random.randint(-5, 5))
        if crit_chance == 1:
            damage *= 2
            print(f"🔥 CRITICAL HIT by {self.name}! 🔥")
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def use_special(self, opponent):
        print(f"{self.name} unleashes {self.special_move['name']}!")
        damage = self.special_move["power"] + random.randint(-5, 10)
        opponent.health -= damage
        print(f"{self.special_move['name']} deals {damage} damage!")

    def heal(self):
        if self.potions > 0:
            heal_amount = random.randint(20, 40)
            self.health = min(self.max_health, self.health + heal_amount)
            self.potions -= 1
            print(f"{self.name} used a health potion and restored {heal_amount} HP!")
        else:
            print("No potions left!")

    def is_alive(self):
        return self.health > 0

    def status(self):
        return f"{self.name} - Health: {self.health}/{self.max_health} | Potions: {self.potions}"
