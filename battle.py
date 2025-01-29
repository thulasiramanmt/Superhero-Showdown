import time
from tkinter import messagebox

class SuperHeroBattle:
    def __init__(self, player, villain, gui):
        self.player = player
        self.villain = villain
        self.gui = gui
        self.game_over = False

    def attack(self):
        if not self.game_over:
            self.gui.animate_action("attack", self.player, self.villain)
            self.villain.take_damage(self.player.attack_power)
            self.gui.update_label(f"{self.player.name} attacks {self.villain.name} for {self.player.attack_power} damage!")
            self.check_battle_status()

    def use_special(self):
        if not self.game_over:
            self.gui.animate_action("special", self.player, self.villain)
            self.villain.take_damage(self.player.special_move["power"])
            self.gui.update_label(f"{self.player.name} uses {self.player.special_move['name']} on {self.villain.name} for {self.player.special_move['power']} damage!")
            self.check_battle_status()

    def heal(self):
        if not self.game_over:
            self.gui.animate_action("heal", self.player, None)
            heal_amount = random.randint(20, 40)
            self.player.health = min(self.player.max_health, self.player.health + heal_amount)
            self.gui.update_label(f"{self.player.name} heals for {heal_amount} HP!")
            self.check_battle_status()

    def check_battle_status(self):
        if not self.villain.is_alive():
            self.gui.update_label(f"\n🎉 You defeated {self.villain.name}! Victory! 🎉")
            messagebox.showinfo("Victory", f"🎉 You defeated {self.villain.name}! 🎉")
            self.game_over = True
            self.gui.end_game()
            return
        time.sleep(1)
        self.villain_turn()

    def villain_turn(self):
        if not self.game_over:
            self.gui.update_label("Villain's turn...")
            self.gui.animate_action("attack", self.villain, self.player)
            self.player.take_damage(self.villain.attack_power)
            self.gui.update_label(f"{self.villain.name} attacks {self.player.name} for {self.villain.attack_power} damage!")
            if not self.player.is_alive():
                self.gui.update_label(f"\n💀 You were defeated by {self.villain.name}. Game Over! 💀")
                messagebox.showinfo("Game Over", f"💀 You were defeated by {self.villain.name}. 💀")
                self.game_over = True
                self.gui.end_game()
            else:
                self.gui.update_label(f"{self.player.status()} | {self.villain.status()}")
