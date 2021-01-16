from tkinter import *
from linalg import *

from PIL import Image, ImageTk

# This method destroys the current window
def click():
    root.destroy()


# This method generates the matrix for the user to input to find the subspaces
def generate():

    # user input try except statement (can only enter integer value between 1 and 20)
    user_var = False
    try:
        user_in = int(entry.get())
        if not (1 <= user_in <= 20):
            user_var = False
        else:
            user_var = True
    except:
        user_var = False

    if user_var:

        # making a window to display the matrix
        array_window = Tk()

        # making the textboxes for the matrix and displaying in the window
        txtboxes = [[0 for x in range(user_in)] for x in range(user_in)]
        for y in range(user_in):
            for x in range(user_in):
                txtboxes[x][y] = Entry(array_window, width=10, font="Times 15 bold", justify='center')
                txtboxes[x][y].grid(column=x, row=y)

        compute_btn = Button(array_window, text="Compute", font="Times 15 bold", fg="white", bg="black", width=8,
                             command=lambda: compute(txtboxes, array_window))
        compute_btn.grid(column=y//2, row=x + 1)


# This method will compute the subspaces and show the jordan
def compute(txtboxes, array_window):
    array_window.destroy()
    matrix = [[0 for x in range(len(txtboxes))] for x in range(len(txtboxes))]
    for y in range(len(txtboxes)):
        for x in range(len(txtboxes)):
            matrix[x][y] = int(txtboxes[x][y].get())

if __name__ == "__main__":

    # making the home screen window
    root = Tk()
    root.geometry("1000x600")

    # uploading the picture of space as the background
    bg = ImageTk.PhotoImage(file="space.png")

    # making a canvas and using the picture of space as the background
    canvas = Canvas(root)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")

    # making the title for the applet
    canvas.create_text(500, 150, text="SUBSPACE-INATOR", font="Times 70 bold", fill="white")

    # making the buttons and the textbox for input, to generate the matrix, and an exit button to close the applet
    exit_button = Button(canvas, text="Exit", command=click, font="Times 30 bold", bg="black", fg="white")
    generate_button = Button(canvas, text="Generate", command=generate, font="Times 30 bold", bg="black", fg="white")
    entry = Entry(canvas, font="Times 30 bold", justify='center')

    # making windows to put the buttons in the canvas
    exit_button_window = canvas.create_window(400, 450, anchor="nw", window=exit_button, width=200)
    generate_button_window = canvas.create_window(400, 350, anchor="nw", window=generate_button, width=200)
    entry_window = canvas.create_window(400, 250, anchor="nw", window=entry, width=200)

    root.mainloop()