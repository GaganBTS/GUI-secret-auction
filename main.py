from tkinter import *
from tkinter import messagebox

bids = {}
bidding_finished = False

# --------------------------------------------------------brain------------------------------------------ #

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    messagebox.showinfo(title="WINNER DECLARATION",message=f"The winner is {winner} with a bid of ${highest_bid}")
    name_entry.delete(0,END)
    price_entry.delete(0,END)


def enter_details():
   name = name_entry.get()
   price = price_entry.get()
   if name=="" or price == "":

        messagebox.showerror(title="EMPTY",message="Please don't leave any fields empty")
   else:
    try:
      price2 = int(price)
    except:
        messagebox.showerror(title="INVALID",message="Please enter details validly.")
    else:
        messagebox.askyesno(title=f"{name}",message=f"Bidding price is {price} \n Would you like to add these details?")
        if messagebox.YES:
             bids[name] = price2
             MSG = messagebox.askyesno(title="another bidder",message="Is there any other bidder?")
             if MSG:
                name_entry.delete(0,END)
                price_entry.delete(0,END)
             else:
                find_highest_bidder(bids)


# ------------------------------------------ UI SETUP --------------------------------------------- #
window = Tk()
window.config(padx=50,pady=50,bg="white")
image = PhotoImage(file="bid.png")
canvas = Canvas(height=300,width=300,bg="white",highlightthickness=0)
canvas.create_image(100,150,image= image)
canvas.grid(column=1,row=0,pady=50)

# --------------------------------------labels---------------------------------------- #
name_label = Label(text="Name of Bidder:",font=("Comic Sans MS",12,"normal"),bg="white")
name_label.grid(row=1,column=0)
price_label= Label(text="Bidding price:",font=("Comic Sans MS",12,"normal"),bg="white")
price_label.grid(row=2,column=0)

# -----------------------------------entries-------------------------------- #
name_entry = Entry(width=35)
name_entry.grid(row=1,column=1)
price_entry = Entry(width=35)
price_entry.grid(row=2,column=1)

# -----------------------button-----------------------------#
btn = Button(text="Enter the details",font=("Comic Sans MS",10,"normal"),bg="white",command=enter_details)
btn.grid(row=3,column=1,pady=10)

window.mainloop()
