import random
import tkinter as tk

def rps(choice):
    botChoice = random.randint(0,2)
    bot = ''

    if botChoice == 0:
        bot = 'I picked Rock!'
    elif botChoice == 1:
        bot = 'I picked Paper!'
    elif botChoice == 2:
        bot = 'I picked Scissors!'

    if choice == botChoice:
        return [bot, 'tie']
    elif choice - botChoice == 1 or choice - botChoice == -2:
        return [bot, 'win']
    else:
        return [bot, 'lose']

# --- GUI ---

window = tk.Tk()
window.title('Rock Paper Scissors')
window.geometry('800x800')
window.resizable(False, False)

canvas = tk.Canvas(
    master=window,
    bg='#323738',
    height=1000,
    width=1000,
    highlightthickness=0
)
canvas.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

play = tk.Label(
    master=canvas,
    text='Click to Play!',
    fg='white',
    bg='#222626',
    width=10,
    height=2
)
play.pack(fill=tk.BOTH, padx=40, pady=(40,20))

def playerChoice(choice):
    res = rps(choice)
    
    bot1 = tk.Label(
        master=canvas,
        text=res[0],
        fg='white',
        bg='#222626',
        width=10,
        height=2
    )
    bot1.place(anchor=tk.S, height=20, width=300, x=400, y=400)

    bot2 = tk.Label(
        master=canvas,
        text='You ' + res[1] + '!',
        fg='white',
        bg='#222626',
        width=10,
        height=2
    )
    bot2.place(anchor=tk.S, height=40, width=400, x=400, y=450)


rock = tk.Button(
    master=canvas,
    text='Rock',
    width=25,
    height=5,
    bg='#42CBF5',
    fg='black',
    command=lambda: playerChoice(0)
)
rock.pack(side=tk.LEFT, expand=True, anchor=tk.N, padx=20)

paper = tk.Button(
    master=canvas,
    text='Paper',
    width=25,
    height=5,
    bg='#42CBF5',
    fg='black',
    command=lambda: playerChoice(1)
)
paper.pack(side=tk.LEFT, expand=True, anchor=tk.N)

scissors = tk.Button(
    master=canvas,
    text='Scissors',
    width=25,
    height=5,
    bg='#42CBF5',
    fg='black',
    command=lambda: playerChoice(2)
)
scissors.pack(side=tk.RIGHT, expand=True, anchor=tk.N, padx=20)



window.mainloop()