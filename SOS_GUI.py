import tkinter as tk
from tkinter import ttk


class GUI:
    """Graphic User Interface of the main application window.

    This class creates the main window of the SOS application, including a label,
    a checkbox, radio buttons, and separators for structuring the layout.

    Attributes:
        root (tk.Tk): The main window object.
        top_frame (tk.Frame): Frame containing the label, checkbox, and radio buttons.
        check_var (tk.IntVar): Variable for the state of the checkbox.
        radio_var (tk.StringVar): Variable for tracking the selected radio button value.

     Notes:
        This code was debugged with assistance from OpenAI's ChatGPT, 
        which provided suggestions and support during implementation.

    References:
        OpenAI. (2024). ChatGPT (v4.0) [Large language model]. Retrieved from 
        https://openai.com/chatgpt/
    """

    def __init__(self, root):
        """Initializes the application window and its widgets."""
        self.root = root
        self.root.title("SOS Application")

        # Create a fixed startup window size
        self.root.geometry("400x150")

        # Prevent the window from being resized
        self.root.resizable(False, False)

        # Create a top frame containing a label, checkbox, separator, and radio buttons
        self.top_frame = tk.Frame(self.root)
        self.top_frame.grid(row=0, column=0, padx=10, pady=1, sticky="ew")

        # Game Label Title
        self.label = tk.Label(self.top_frame, text="SOS")
        self.label.grid(row=0, column=0, padx=5, pady=1, sticky="w")

        # Checkbox
        self.check_var = tk.IntVar() 
        self.checkbutton = tk.Checkbutton(
            self.top_frame, text="Enable", variable=self.check_var
        )
        self.checkbutton.grid(row=0, column=10, padx=10, pady=1, sticky="e")

        # Expand the top frame to fill the window
        self.root.grid_columnconfigure(0, weight=1)

        # Radio Buttons
        self.radio_var = tk.StringVar(value="Simple Game")

        # Frame for radio buttons
        self.radio_frame = tk.Frame(self.top_frame)
        self.radio_frame.grid(row=0, column=3, padx=10, pady=1, sticky="w")

        # Radio button 1 for Simple Game
        self.radio_simple_game = tk.Radiobutton(
            self.radio_frame, text="Simple Game",
            variable=self.radio_var, value="Simple Game"
        )
        self.radio_simple_game.grid(row=0, column=0, padx=5, pady=1, sticky="w")

        # Radio button 2 for General Game
        self.radio_general_game = tk.Radiobutton(
            self.radio_frame, text="General Game",
            variable=self.radio_var, value="General Game"
        )
        self.radio_general_game.grid(row=0, column=1, padx=5, pady=1, sticky="w")

        # Vertical Separator with a line between checkbox and radio buttons
        self.vert_separator = ttk.Separator(self.top_frame, orient="vertical")
        self.vert_separator.grid(row=0, column=9, rowspan=1, sticky="ns", padx=10)

        # Horizontal Separator with a line below the widgets
        self.separator = ttk.Separator(self.root, orient="horizontal")
        self.separator.grid(row=1, column=0, sticky="ew", padx=10, pady=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

