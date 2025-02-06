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
        self.configure(bg='#87CEEB')  # Cool shade of blue
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        ttk.Label(self, text="Select an Option:", font=("Arial", 16)).pack(pady=20)

        ttk.Button(self, text="Start Experiment", command=self.start_experiment_menu, width=25).pack(pady=10)
        ttk.Button(self, text="Start Operation", command=self.start_operation_menu, width=25).pack(pady=10)
        ttk.Button(self, text="Visualize", command=self.visualize_menu, width=25).pack(pady=10)

        # Load and display the image
        try:
            image = Image.open("assets/brain.png")  # Replace with your image path
            image = image.resize((200, 150), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self, image=photo, bg='#87CEEB')
            label.image = photo  # Keep a reference to avoid garbage collection
            label.pack(pady=20)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to load image: {e}")

    def start_experiment_menu(self):
        self.clear_window()

        ttk.Label(self, text="Choose Experiment:", font=("Arial", 16)).pack(pady=30)

        ttk.Button(self, text="Blink Experiment", command=lambda: self.show_message("Blink Experiment Started"), width=25).pack(pady=10)
        ttk.Button(self, text="Mouse Experiment", command=lambda: self.show_message("Mouse Experiment Started"), width=25).pack(pady=10)
        ttk.Button(self, text="Combined Experiment", command=lambda: self.show_message("Combined Experiment Started"), width=25).pack(pady=10)
        
        ttk.Button(self, text="Back", command=self.create_main_menu, width=25).pack(pady=20)

    def start_operation_menu(self):
        self.clear_window()

        ttk.Label(self, text="Choose Operation:", font=("Arial", 16)).pack(pady=30)

        ttk.Button(self, text="Use Keyboard", command=lambda: self.show_message("Keyboard Control Started"), width=25).pack(pady=10)
        ttk.Button(self, text="Solve Maze", command=lambda: self.show_message("Maze Solving Started"), width=25).pack(pady=10)
        ttk.Button(self, text="Play Game", command=lambda: self.show_message("Game Started"), width=25).pack(pady=10)

        ttk.Button(self, text="Back", command=self.create_main_menu, width=25).pack(pady=20)

    def visualize_menu(self):
        self.clear_window()

        ttk.Label(self, text="Select Traces to Visualize:", font=("Arial", 16)).pack(pady=20)

        self.trace_vars = {
            "Trace 1": tk.BooleanVar(),
            "Trace 2": tk.BooleanVar(),
            "Trace 3": tk.BooleanVar()
        }

        for trace, var in self.trace_vars.items():
            ttk.Checkbutton(self, text=trace, variable=var).pack(anchor='w', padx=40, pady=5)

        self.fft_var = tk.BooleanVar()
        ttk.Checkbutton(self, text="Apply Fourier Transform", variable=self.fft_var).pack(anchor='w', padx=40, pady=10)

        ttk.Button(self, text="Visualize", command=self.visualize_traces, width=25).pack(pady=10)
        ttk.Button(self, text="Back", command=self.create_main_menu, width=25).pack(pady=10)

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
