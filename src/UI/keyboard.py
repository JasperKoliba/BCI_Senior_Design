import tkinter as tk
from tkinter import messagebox

class PopupKeyboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Popup Keyboard")
        self.root.geometry("600x400")

        # Frame for text box
        text_frame = tk.Frame(self.root)
        text_frame.pack(pady=10)

        self.text_box = tk.Text(text_frame, height=3, font=("Arial", 14))
        self.text_box.pack()

        # Frame for keyboard
        self.keyboard_frame = tk.Frame(self.root)
        self.keyboard_frame.pack()

        self.keys = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
            ['Space', 'Delete', 'Cursor']
        ]

        self.current_row = 0
        self.current_col = 0

        self.create_keyboard()

        # Key bindings for arrow keys and spacebar
        self.root.bind('<Up>', lambda event: self.update_selection("up", False))
        self.root.bind('<Down>', lambda event: self.update_selection("down", False))
        self.root.bind('<Left>', lambda event: self.update_selection("left", False))
        self.root.bind('<Right>', lambda event: self.update_selection("right", False))
        self.root.bind('<space>', lambda event: self.update_selection("no movement", True))

        self.root.mainloop()

    def create_keyboard(self):
        self.button_grid = []

        for row_index, row in enumerate(self.keys):
            button_row = []
            for col_index, key in enumerate(row):
                button = tk.Button(self.keyboard_frame, text=key, width=5, height=2,
                                   font=("Arial", 12), command=lambda k=key: self.key_press(k))
                button.grid(row=row_index, column=col_index, padx=5, pady=5)
                button_row.append(button)
            self.button_grid.append(button_row)

        self.highlight_key()

    def highlight_key(self):
        for row_index, row in enumerate(self.button_grid):
            for col_index, button in enumerate(row):
                if row_index == self.current_row and col_index == self.current_col:
                    button.config(bg='lightblue')
                else:
                    button.config(bg='SystemButtonFace')

    def key_press(self, key):
        if key == 'Space':
            self.text_box.insert(tk.INSERT, ' ')
        elif key == 'Delete':
            self.text_box.delete("insert-1c")
        elif key == 'Cursor':
            self.text_box.insert(tk.INSERT, '|')
        else:
            self.text_box.insert(tk.INSERT, key)

    def update_selection(self, movement, press):
        if movement == "up" and self.current_row > 0:
            self.current_row -= 1
        elif movement == "down" and self.current_row < len(self.button_grid) - 1:
            self.current_row += 1
        elif movement == "left" and self.current_col > 0:
            self.current_col -= 1
        elif movement == "right" and self.current_col < len(self.button_grid[self.current_row]) - 1:
            self.current_col += 1

        self.highlight_key()

        if press:
            current_key = self.keys[self.current_row][self.current_col]
            self.key_press(current_key)

if __name__ == "__main__":
    PopupKeyboard()