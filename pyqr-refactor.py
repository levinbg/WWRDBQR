import tkinter as tk


class Model:
    def __init__(self):
        self.counter = 0


class View:
    def __init__(self, main, controller):
        self.main = main
        self.controller = controller
        self.label = tk.Label(main, text="Counter: 0")
        self.label.pack()
        self.button = tk.Button(
            main, text="Increment", command=controller.increment_counter
        )
        self.button.pack()


class Controller:
    def __init__(self, main):
        self.model = Model()
        self.view = View(main, self)

    def increment_counter(self):
        self.model.counter += 1
        self.view.label.config(text=f"Counter: {self.model.counter}")


root = tk.Tk()  # Create the main application window
root.title("Hello, Tkinter!")  # Set the title of the window

controller = Controller(root)

root.mainloop()  # Start the main event loop
