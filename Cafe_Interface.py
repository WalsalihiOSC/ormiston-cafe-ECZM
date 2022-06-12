"""This program is about creating a cafe interface for students to make orders and the cafe manager to track student orders"""

from tkinter import *
from tkinter.scrolledtext import *


class CafeInterface:
    def __init__(self, parent):

        self.fCoffee = Frame(parent, height = 600, width = 1000)
        self.fCoffee.grid(column = 0, row = 0)
        self.fCoffee.grid_propagate(0)

        self.f1 = Frame(self.fCoffee, height = 600, width = 300, bg = "#e3cbb3")
        self.f1.grid(column = 0, row = 0)
        self.f1.grid_propagate(0)

        self.menuslides = []

        myfile = open("cafeList.txt")
        self.lines = myfile.readlines()

        for line in self.lines[0:4]:
            words = line.split(";")   
            self.menuslides.append(CafeOrders(words[0], words[1], words[2], words[3]))

        self.c1 = Canvas(self.f1, height = 50, width = 300, bg = "#e3cbb3", highlightthickness = 0)
        self.c1.grid(column = 0, row = 0)

        self.c1.cafe = PhotoImage(file = "cafeImages/logo2.png")
        self.c1.create_image(0, 0, anchor = NW, image = self.c1.cafe)

        self.l1 = Label(self.f1, text = "Orders:", bg = "#e3cbb3", font = "None, 20")
        self.l1.grid(column = 0, row = 1, sticky = W, padx = 30, pady = (20, 5))

        self.orderDisplay = ScrolledText(self.f1, height = 27, width = 30)
        self.orderDisplay.grid(column = 0, row = 2, sticky = W, padx = 30)

        self.l2 = Label(self.f1, text = "Total: $_____", bg = "#e3cbb3", font = "None, 15")
        self.l2.grid(column = 0, row = 3, sticky = E, padx = 30, pady = (5, 0))

        self.b1 = Button(self.f1, text = "Confirm")
        self.b1.grid(column = 0, row = 4, sticky = W, padx = 30, pady = (30, 5))
        self.b2 = Button(self.f1, text = "Reset Orders")
        self.b2.grid(column = 0, row = 5, sticky = W, padx = 30)

        self.target = 0

        self.c2 = Canvas(self.fCoffee, height = 152, width = 700, highlightthickness = 0)
        self.c2.grid(column = 1, row = 0, sticky = N)

        self.c2.mainbanner = PhotoImage(file = self.menuslides[0].banner)
        self.c2.create_image(0, 0, anchor = NW, image = self.c2.mainbanner)

        self.c3 = Canvas(self.fCoffee, height = 448, width = 700, highlightthickness = 0)
        self.c3.place(x = 300, y = 152)

        self.c3.mainheader = PhotoImage(file = self.menuslides[0].header)
        self.c3.create_image(30, 50, anchor = NW, image = self.c3.mainheader)

        self.f2 = Frame(self.c3, height = 100, width = 300)
        self.f2.place(x = 35, y = 180)

        self.l2 = Label(self.f2, text = "Coffees", font = "None 12 underline")
        self.l2.grid(column = 0, row = 0, sticky = NW, pady = 5)

        self.l3 = Label(self.f2, text = "Sandwiches", font = "None 12 underline")
        self.l3.grid(column = 0, row = 1, sticky = NW, pady = 5)

        self.l4 = Label(self.f2, text = "Desserts", font = "None 12 underline")
        self.l4.grid(column = 0, row = 2, sticky = NW)

        self.l5 = Label(self.f2, text = "Sides", font = "None 12 underline")
        self.l5.grid(column = 0, row = 3, sticky = NW, pady = 5)

        self.f3 = Frame(self.c3, height = 300, width = 250)
        self.f3.place(x = 320, y = 100)

        self.l6 = Label(self.c3, text = "$", font = "None 15")
        self.l6.place(x = 590, y = 80)

        self.l7 = Label(self.c3, text = "Qty:", font = "None 15")
        self.l7.place(x = 640, y = 80)

        self.coffeeList = []
        self.coffee = self.menuslides[0].orders
        self.coffees = self.coffee.split(",")
        for item in self.coffees:
            self.coffeeList.append(item)
            
        self.v = StringVar()
        self.v.set("0")
        self.coffeemenu = self.coffeeList
        self.cb1 = []
        for i in range(len(self.coffeemenu)):
            self.cb1.append(Checkbutton(self.f3, variable = self.v, text = self.coffeemenu[i]))
            self.cb1[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)

        self.f4 = Frame(self.c3)
        self.f4.place(x = 570, y = 100)

        self.costList = []
        self.cost = self.menuslides[0].prices
        self.costs = self.cost.split(",")
        for item2 in self.costs:
            self.costList.append(item2)

        self.coffeeprices = self.costList
        self.pricelabels = []
        for i in range(len(self.coffeeprices)):
            self.pricelabels.append(Label(self.f4, text = self.coffeeprices[i]))
            self.pricelabels[i].grid(column = 0, sticky = NE, ipadx = 10, ipady = 4)
        
        self.f5 = Frame(self.c3)
        self.f5.place(x = 640, y = 100)
        
        self.v2 = StringVar()
        self.v2.set("")
        self.e1 = []
        for i in range(8):
            self.e1.append(Entry(self.f5, width = 1, bg = "#e3cbb3", font = "None, 12"))
            self.e1[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 2)

        self.b1 = Button(self.c3, text = ">")
        self.b1.place(x = 350, y = 400)

        self.b2 = Button(self.c3, text = "<")
        self.b2.place(x = 330, y = 400)


class CafeOrders:
    def __init__(self, banner, header, orders, prices):
        self.banner = banner
        self.header = header
        self.orders = orders
        self.prices = prices
    



#Main Routine
if __name__ == "__main__":                        
    root = Tk()
    CafeInterface(root)
    root.title("Cafe Interface")
    root.mainloop()