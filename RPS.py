import random
import tkinter as tk

def rps(choice):
    botChoice = random.randint(0,2)

    if botChoice == 0:
        print('I picked Rock!')
    elif botChoice == 1:
        print('I picked Paper!')
    elif botChoice == 2:
        print('I picked Scissors!')

    if choice == botChoice:
        return 'tie'
    elif choice - botChoice == 1 or choice - botChoice == -2:
        return 'win'
    else:
        return 'loss'

# --- GUI ---

window = tk.Tk()
window.title('Rock Paper Scissors')

canvas = tk.Canvas(
    master=window,
    bg="#323738",
    height=1000,
    width=1000,
    highlightthickness=0
)
canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

rock = tk.Button(
    master=canvas,
    text='Rock',
    width=25,
    height=5,
    bg='#42CBF5',
    fg='black'
)
rock.pack(side=tk.LEFT,expand=1,anchor='ne')

paper = tk.Button(
    master=canvas,
    text='Paper',
    width=25,
    height=5,
    bg='#42CBF5',
    fg='black'
)
paper.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

scissors = tk.Button(
    master=canvas,
    text='Scissors',
    width=25,
    height=5,
    bg='#42CBF5',
    fg='black'
)
scissors.pack(side=tk.LEFT,expand=1,anchor='nw')


window.mainloop()

'''
--- TEST ---
'''
'''
while True:
    x = int(input('Rock (0), Paper (1), Scissors (2): '))
    if x == 555:
        break
    print(rps(x))
    '''