try:
    import tkinter as tk
    from tkinter import ttk, messagebox
    from PIL import Image, ImageTk
except ImportError as e:
    raise ImportError("tkinter or PIL module is not available in your environment. Please ensure they are installed or run the code in an environment that supports them.") from e

class ControlUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Control Panel")
        self.geometry("400x500")
        self.configure(bg='#272483')  # Dark blue background
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        header = tk.Label(self, text="Select an Option:", font=("Arial", 16), bg='#272483', fg='#d3d3d3')
        header.pack(pady=20)

        self.create_custom_button("Start Experiment", self.start_experiment_menu).pack(pady=10)
        self.create_custom_button("Start Operation", self.start_operation_menu).pack(pady=10)
        self.create_custom_button("Visualize", self.visualize_menu).pack(pady=10)

        # Load and display the transparent PNG image
        try:
            image = Image.open("assets/BCI_logo.png").convert("RGBA")  # Ensure transparency is respected
            image = image.resize((200, 150), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self, image=photo, bg='#272483')
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(pady=20)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image: {e}")

    def create_custom_button(self, text, command):
        return tk.Button(self, text=text, command=command, width=25, bg='#b44dc2', fg='#d3d3d3', activebackground='#a03cb1', activeforeground='#ffffff', font=("Arial", 12, "bold"))

    def start_experiment_menu(self):
        self.clear_window()

        tk.Label(self, text="Choose Experiment:", font=("Arial", 16), bg='#272483', fg='#d3d3d3').pack(pady=30)

        self.create_custom_button("Blink Experiment", lambda: self.show_message("Blink Experiment Started")).pack(pady=10)
        self.create_custom_button("Mouse Experiment", lambda: self.show_message("Mouse Experiment Started")).pack(pady=10)
        self.create_custom_button("Combined Experiment", lambda: self.show_message("Combined Experiment Started")).pack(pady=10)
        
        self.create_custom_button("Back", self.create_main_menu).pack(pady=20)

    def start_operation_menu(self):
        self.clear_window()

        tk.Label(self, text="Choose Operation:", font=("Arial", 16), bg='#272483', fg='#d3d3d3').pack(pady=30)

        self.create_custom_button("Use Keyboard", lambda: self.show_message("Keyboard Control Started")).pack(pady=10)
        self.create_custom_button("Solve Maze", lambda: self.show_message("Maze Solving Started")).pack(pady=10)
        self.create_custom_button("Play Game", lambda: self.show_message("Game Started")).pack(pady=10)

        self.create_custom_button("Back", self.create_main_menu).pack(pady=20)

    def visualize_menu(self):
        self.clear_window()

        tk.Label(self, text="Select Traces to Visualize:", font=("Arial", 16), bg='#272483', fg='#d3d3d3').pack(pady=20)

        self.trace_vars = {
            "Trace 1": tk.BooleanVar(),
            "Trace 2": tk.BooleanVar(),
            "Trace 3": tk.BooleanVar()
        }

        for trace, var in self.trace_vars.items():
            tk.Checkbutton(self, text=trace, variable=var, bg='#272483', fg='#d3d3d3', selectcolor='#272483', activebackground='#272483').pack(anchor='w', padx=40, pady=5)

        self.fft_var = tk.BooleanVar()
        tk.Checkbutton(self, text="Apply Fourier Transform", variable=self.fft_var, bg='#272483', fg='#d3d3d3', selectcolor='#272483', activebackground='#272483').pack(anchor='w', padx=40, pady=10)

        self.create_custom_button("Visualize", self.visualize_traces).pack(pady=10)
        self.create_custom_button("Back", self.create_main_menu).pack(pady=10)

    def visualize_traces(self):
        selected_traces = [trace for trace, var in self.trace_vars.items() if var.get()]
        apply_fft = self.fft_var.get()

        if not selected_traces:
            messagebox.showwarning("No Traces Selected", "Please select at least one trace to visualize.")
            return

        msg = f"Visualizing: {', '.join(selected_traces)}"
        if apply_fft:
            msg += " with Fourier Transform"

        self.show_message(msg)

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = ControlUI()
    app.mainloop()
