from tkinter import *
import random


root = Tk()


root.title('Zar Atma oyunu')
root.iconbitmap('c:/guideneme')
root.geometry("400x900")

# get the dice number
def get_number(x):
    if x == '\u2680':
        return (1)
    elif x == '\u2681':
        return (2)
    elif x == '\u2682':
        return (3)
    elif x == '\u2683':
        return (4)
    elif x == '\u2684':
        return (5)
    elif x == '\u2685':
        return (6)


# roll the dice
def roll_dice():
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)

    # Determine dice number
    sd1 = get_number(d1)
    sd2 = get_number(d2)

    # label update
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)

    # uptade sub label
    sub_dice_label1.config(text=sd1)
    sub_dice_label2.config(text=sd2)

    #update total label
    total = sd1 + sd2
    total_label.config(text=total)


# zar listesi yarat
my_dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', ]

# Frame yarat
my_frame = Frame(root)
my_frame.pack(pady=20)

# zar labelları
dice_label1 = Label(my_frame, text='', font=("Helvetica", 70), fg=("green"))
dice_label1.grid(row=0, column=0, padx=1)


sub_dice_label1 = Label(my_frame, text="")
sub_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text='', font=("Helvetica", 70), fg=("green"))
dice_label2.grid(row=0, column=1, padx=5)

sub_dice_label2 = Label(my_frame, text="")
sub_dice_label2.grid(row=1, column=1)

#toplamak label
total_label = Label(root,text="", font=("Hevetica",  24), fg="red")
total_label.pack(pady=40)


# buton yaratma
my_button = Button(root, text="Yeşil takım için Zar at", command=roll_dice, fg="green")
my_button.pack(pady=0)

#buradan başladım 3. ve 4. zarlar !

def get_number(x):
    if x == '\u2680':
        return (1)
    elif x == '\u2681':
        return (2)
    elif x == '\u2682':
        return (3)
    elif x == '\u2683':
        return (4)
    elif x == '\u2684':
        return (5)
    elif x == '\u2685':
        return (6)


# roll the dice
def roll_dice():
    d3 = random.choice(my_dice)
    d4 = random.choice(my_dice)

    # Determine dice number
    sd3 = get_number(d3)
    sd4 = get_number(d4)

    # label update
    dice_label3.config(text=d3)
    dice_label4.config(text=d4)

    # uptade sub label
    sub_dice_label3.config(text=sd3)
    sub_dice_label4.config(text=sd4)

    #update total label
    total1 = sd3 + sd4
    total1_label.config(text=total1)


# zar listesi
my_dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', ]

# Frame yarat
my_frame = Frame(root)
my_frame.pack(pady=20)

# zar label
dice_label3 = Label(my_frame, text='', font=("Helvetica", 70), fg=("blue"))
dice_label3.grid(row=0, column=0, padx=5)


sub_dice_label3 = Label(my_frame, text="")
sub_dice_label3.grid(row=1, column=0)

dice_label4 = Label(my_frame, text='', font=("Helvetica", 70), fg=("blue"))
dice_label4.grid(row=0, column=1, padx=5)

sub_dice_label4 = Label(my_frame, text="")
sub_dice_label4.grid(row=1, column=1)

#toplama labelları
total1_label = Label(root,text="", font=("Hevetica",  24), fg="red")
total1_label.pack(pady=40)


# buton yaratma
my_button2 = Button(root, text="Mavi takım için Zar at", command=roll_dice , fg="blue")
my_button2.pack(pady=1)



# roll the dice
roll_dice()

root.mainloop()
