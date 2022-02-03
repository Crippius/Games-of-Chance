from tkinter import *
from tkinter import messagebox
from problems_check import problems_check
from casino import Casino


class Intry(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().isdigit(): 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)


root = Tk()
root.title("Games of Chance")
root.iconbitmap("sprites/duh.ico")
root.configure(background="#009900")
#root.geometry("%dx%d" % (root.winfo_screenwidth() , root.winfo_screenheight()))
root.geometry("1232x465")

player = Casino()
chips = StringVar()
chips.set(f"{player.balance()} chips")
# messagebox.showinfo("Welcome!", 
# """
# Thanks for installing Games of Chance!
# In this program you can play some of the most famous gambling games ever!
# Hope you will enjoy this project!
# You will be starting with 100 chips to bet on, good luck!
# """)

def update():
    global chips
    chips.set(f"{player.balance()} chips")

def play(game, *args):
    if args[0]  == "":
        messagebox.showerror("Error!", "No amount of money betted")
        return

    if game == "slots":
        check, result = player.slot_machine(int(args[0]))
    elif game == "baccarat":
        if args[1] == "Player":
            check, result = player.baccarat(int(args[0]), args[1], False, False)
        else:
            check, result = player.baccarat(int(args[0]), args[1], args[2], args[3])
    if check == -1:
        messagebox.showerror("Error!", str(result))
    
    update()





def baccarat_prep():
    branch = Toplevel()
    branch.title("Baccarat")
    branch.iconbitmap("sprites/duh.ico")
    branch.configure(background="#009900")

    money_label = Label(branch, text="Money to bet:", bg="#009000", font=("Helvetica", 14))
    money_label.grid(row=0, column=0, columnspan=4)

    bet = Intry(branch, bg="#D3D3D3")
    bet.grid(row=0, column=4, columnspan=2)

    player_or_better = StringVar()
    player_or_better.set("Player")

    x_win = StringVar()
    x_win.set(False)

    pair = StringVar()
    pair.set(False)

    p_radio = Radiobutton(branch, text="Player", bg="#008000", variable=player_or_better, value="Player")
    p_radio.grid(row=1, column=0, columnspan=3, sticky=W+E+N+S)

    b_radio = Radiobutton(branch, text="Better", bg="#008000", variable=player_or_better, value="Better")
    b_radio.grid(row=1, column=3, columnspan=3, sticky=W+E+N+S)

    p_win_radio = Radiobutton(branch, text="Player win", bg="#008000", variable=x_win, value="Player")
    p_win_radio.grid(row=2, column=0, columnspan=2, sticky=W+E+N+S)

    b_win_radio = Radiobutton(branch, text="Banker win", bg="#008000", variable=x_win, value="Banker")
    b_win_radio.grid(row=2, column=2, columnspan=2, sticky=W+E+N+S)

    tie_radio = Radiobutton(branch, text="Tie", bg="#008000", variable=x_win, value="Tie")
    tie_radio.grid(row=2, column=4, columnspan=2, sticky=W+E+N+S)

    p_pair_radio = Radiobutton(branch, text="Player pair", bg="#008000", variable=pair, value="Player")
    p_pair_radio.grid(row=3, column=0, columnspan=2, sticky=W+E+N+S)

    b_pair_radio = Radiobutton(branch, text="Banker pair", bg="#008000", variable=pair, value="Banker")
    b_pair_radio.grid(row=3, column=2, columnspan=2, sticky=W+E+N+S)

    a_pair_radio = Radiobutton(branch, text="Any pair", bg="#008000", variable=pair, value="Any")
    a_pair_radio.grid(row=3, column=4, columnspan=4, sticky=W+E+N+S)

    submit = Button(branch, text="Submit bet", bg="#008000", font=("Helvetica", 14),  
                    command=lambda:play("baccarat", bet.get(), player_or_better.get(), x_win.get(), pair.get()))
    submit.grid(row=4, column=0, columnspan=3, sticky=W+E+N+S)

    exit = Button(branch, text="Stop betting", bg="#008000", font=("Helvetica", 14), command=branch.destroy)
    exit.grid(row=4, column=3, columnspan=3, sticky=W+E+N+S)
    


def slot_prep():
    branch = Toplevel()
    branch.title("Slot Machine")
    branch.iconbitmap("sprites/duh.ico")
    branch.configure(background="#009900")

    money_label = Label(branch, text="Money to bet:", bg="#009000", font=("Helvetica", 14))
    money_label.grid(row=0, column=0)

    bet = Intry(branch, bg="#D3D3D3")
    bet.grid(row=0, column=1)

    submit = Button(branch, text="Submit bet", bg="#008000", font=("Helvetica", 14),  command=lambda:play("baccarat", bet.get()))
    submit.grid(row=1, column=0)

    exit = Button(branch, text="Stop betting", bg="#008000", font=("Helvetica", 14), command=branch.destroy)
    exit.grid(row=1, column=1)



title = Label(root, text="Games of Chance", borderwidth=2, relief="solid", font=("Helvetica", 32), bg="#008000")
title.grid(row=0, column=0, columnspan=5, sticky=N+W+E+S)

money = Label(root, textvariable=chips, borderwidth=2, relief="solid", font=("Helvetica", 32), bg="#008000")
money.grid(row=0, column=5, ipadx=0, sticky=N+S+W+E)

heads_or_tails = Button(root, text="Play\nHeads or Tails", font=("Helvetica", 42), bg="#008000", width=12)
heads_or_tails.grid(row=1, column=0, rowspan=2, columnspan=2, ipadx=10, padx=10, pady=10, sticky=N+W+E+S)

roulette = Button(root, text="Play\nRoulette", font=("Helvetica", 42), bg="#008000", width=10)
roulette.grid(row=1, column=2, rowspan=2, columnspan=2, padx=10, pady=10, sticky=N+W+E+S)

blackjack = Button(root, text="Play\nBlackjack", font=("Helvetica", 42), bg="#008000", width=12)
blackjack.grid(row=1, column=4, rowspan=2, columnspan=2, padx=10, pady=10, sticky=N+W+E+S)

slot_machine = Button(root, text="Play\nSlot Machine", font=("Helvetica", 42), bg="#008000", width=12, command=slot_prep)
slot_machine.grid(row=3, column=0, rowspan=2, columnspan=2, padx=10, pady=10, sticky=N+W+E+S)

baccarat = Button(root, text="Play\nBaccarat", font=("Helvetica", 42), bg="#008000", width=10, command=baccarat_prep)
baccarat.grid(row=3, column=2, rowspan=2, columnspan=2, padx=10, pady=10, sticky=N+W+E+S)

credits = Button(root, text="See Credits", font=("Helvetica", 32), bg="#008000", width=12)
credits.grid(row=3, column=4, columnspan=2, padx=10, pady=10, sticky=N+W+E+S)

exit = Button(root, text="Exit", font=("Helvetica", 32), bg="#008000", width=12, command=root.destroy)
exit.grid(row=4, column=4, columnspan=2, padx=10, pady=10, sticky=N+W+E+S)

root.mainloop()
