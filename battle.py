import time
from tkinter import messagebox

class SuperHeroBattle:
    def __init__(self, player, villain, gui):
        self.player = player
        self.villain = villain
        self.gui = gui

    def attack(self):
        self.gui.animate_action("attack", self.player, self.villain)
        self.check_battle_status()

    def use_special(self):
        self.gui.animate_action("special", self.player, self.villain)
        self.check_battle_status()

    def heal(self):
        self.gui.animate_action("heal", self.player, None)
        self.check_battle_status()

    def check_battle_status(self):
        if not self.villain.is_alive():
            self.gui.update_label(f"\n🎉 You defeated {self.villain.name}! Victory! 🎉")
            messagebox.showinfo("Victory", f"🎉 You defeated {self.villain.name}! 🎉")
            return
        time.sleep(1)
        self.villain_turn()

    def villain_turn(self):
        self.gui.update_label("Villain's turn...")
        self.gui.animate_action("attack", self.villain, self.player)
        if not self.player.is_alive():
            self.gui.update_label(f"\n💀 You were defeated by {self.villain.name}. Game Over! 💀")
            messagebox.showinfo("Game Over", f"💀 You were defeated by {self.villain.name}. 💀")
        else:
            self.gui.update_label(f"{self.player.status()} | {self.villain.status()}")

