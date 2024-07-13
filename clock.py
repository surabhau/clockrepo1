import tkinter as tk
from time import strftime

# Function to update time
def update_time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, update_time)  # Update every second (1000 milliseconds)

# Create tkinter window
window = tk.Tk()
window.title('Digital Clock')

# Create label widget for the time display
label = tk.Label(window, font=('calibri', 40, 'bold'), background='purple', foreground='white')

# Place the label in the window
label.pack(anchor='center')

# Call update_time initially to start the clock
update_time()

# Run the tkinter main loop
window.mainloop()
