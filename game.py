from gui import SuperHeroGameGUI
import tkinter as tk

def start_game():
    root = tk.Tk()
    game_gui = SuperHeroGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    start_game()
