import tkinter as tk
from characters import superheroes, villains
from battle import SuperHeroBattle

class SuperHeroGameGUI:
     def __init__(self, master):
         self.master = master
         master.title("Superhero Battle Game")

         self.canvas = tk.Canvas(master, width=800, height=600)
         self.canvas.pack()

         self.label = tk.Label(master, text="🌟 Welcome to Superhero Battle Arena! 🌟\nChoose your hero:")
         self.label.pack()

         self.hero_buttons = []
         for i, hero in enumerate(superheroes):
             button = tk.Button(master, text=f"{hero.name} (Health: {hero.health})", command=lambda i=i: self.choose_hero(i))
             button.pack()
             self.hero_buttons.append(button)

     def choose_hero(self, index):
         self.player = superheroes[index]
         self.label.config(text=f"You have chosen {self.player.name}!\nPrepare for battle!")
         self.play_animation()

         # Proceed to battle
         self.start_battle()

     def start_battle(self):
         import random
         self.villain = random.choice(villains)
         self.label.config(text=f"⚠️ Your opponent is {self.villain.name}! ⚠️\nBattling...")

         self.battle = SuperHeroBattle(self.player, self.villain, self)

         self.create_action_buttons()

     def create_action_buttons(self):
         self.action_frame = tk.Frame(self.master)
         self.action_frame.pack()

         self.attack_button = tk.Button(self.action_frame, text="Attack", command=self.battle.attack)
         self.attack_button.pack(side="left")

         self.special_button = tk.Button(self.action_frame, text=f"Use Special Move ({self.player.special_move['name']})", command=self.battle.use_special)
         self.special_button.pack(side="left")

         self.heal_button = tk.Button(self.action_frame, text="Heal", command=self.battle.heal)
         self.heal_button.pack(side="left")

     def update_label(self, text):
         self.label.config(text=text)

     def play_animation(self):
         self.canvas.delete("all")
         player_rect = self.canvas.create_rectangle(50, 50, 150, 150, fill="blue")
         villain_rect = self.canvas.create_rectangle(650, 50, 750, 150, fill="red")
         
         # Simple animation loop
         for _ in range(50):
             self.canvas.move(player_rect, 5, 0)  # Move player right
             self.canvas.move(villain_rect, -5, 0)  # Move villain left
             self.master.update()
             self.master.after(50)  # Pause to create animation effect

root = tk.Tk()
game_gui = SuperHeroGameGUI(root)
root.mainloop()
 
 