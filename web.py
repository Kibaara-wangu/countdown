import tkinter as tk

class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")


        # initializing timer variable
        self.seconds = 0
        self.timer_running = False


       # label for displaying the timer
        self.timer_label = tk.label(root, text ="00:00")
        self.timer_label.pack(pady=20)

        # start and stop buttons
        self.Start_button = tk.button(root, text="Start", command=self.Start_timer)
        self.Stop_button = tk.button(root, text="Stop", command=self.stop_timer)
        self.Start_button.pack(side=tk.LEFT, padx=10)
        self.Stop_button.pack(side=tk.LEFT, padx=10)

        # timer display
        self.update_timer()

    def Start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def Stop_timer(self):
        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            self.seconds += 1
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            time_str = f"{minutes:02}:{seconds:02}"
            self.timer_label.config(text=time_str)
            self.root.after(1000, self.update_timer)  


if __name__ == "__main__":
    root = tk.Tk()
    app = Timer(root)
    root.mainloop()
        


