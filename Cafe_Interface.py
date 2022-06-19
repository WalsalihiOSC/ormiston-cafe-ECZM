"""This program is about creating a cafe interface for students to make orders and the cafe manager to track student orders"""

from tkinter import *
import tkinter
from tkinter.scrolledtext import *
import tkinter as tk

class CafeInterface:
    def __init__(self, parent):
        self.DailyOrders = []

        """Main frame of the cafe interface"""
        self.main_cafeFrame = Frame(parent, height = 600, width = 1000)
        self.main_cafeFrame.grid(column = 0, row = 0)
        self.main_cafeFrame.grid_propagate(0)

        self.ormistonCafe()
        
        """Creating menu for switching between Student Tracking Orders and Ormiston Cafe"""
        my_menu = Menu()
        root.configure(menu = my_menu)

        options_menu = Menu(my_menu, tearoff = False)
        my_menu.add_cascade(label = "Cafe Manager", menu = options_menu)
        options_menu.add_command(label = "Student Tracking Orders", command = self.studentTrackingOrders)
        options_menu.add_command(label = "Ormiston Cafe", command = self.ormistonCafe)

    def ormistonCafe(self):
        """Creating frames for each menu category"""
        self.cafeFrame = Frame(self.main_cafeFrame, height = 600, width = 1000)

        self.main_menuFrame = Frame(self.cafeFrame, height = 600, width = 700)
        self.main_menuFrame.grid(column = 1, row = 0)

        self.coffeeFrame = Frame(self.main_menuFrame, height = 600, width = 700)
        self.sandwichFrame = Frame(self.main_menuFrame, height = 600, width = 700)
        self.dessertFrame = Frame(self.main_menuFrame, height = 600, width = 700)
        self.sidesFrame = Frame(self.main_menuFrame, height = 600, width = 700)

        for frame in (self.cafeFrame, self.coffeeFrame, self.sandwichFrame, self.dessertFrame, self.sidesFrame):
            frame.grid(column = 0, row = 0, sticky = NSEW)
            
        self.show_frame(self.cafeFrame)

        """Order selecting frame will be on top of the main cafe frame"""
        self.orderSelecting_Frame = Frame(self.cafeFrame, height = 600, width =300, bg = "#e3cbb3")
        self.orderSelecting_Frame.grid(column = 0, row = 0)
        self.orderSelecting_Frame.grid_propagate(0)

        """Reading from files for cafe menu details - images, foods, prices"""
        self.menuslides = []

        myfile = open("cafeList.txt")
        self.lines = myfile.readlines()
        """Appending to the CafeMenuDetails class"""
        for line in self.lines[0:4]:
            words = line.split(";")   
            self.menuslides.append(CafeMenuDetails(words[0], words[1], words[2], words[3]))

        """Creating a canvas for the cafe logo to put on"""
        self.logo_img = Canvas(self.orderSelecting_Frame, height = 50, width = 300, bg = "#e3cbb3", highlightthickness = 0)
        self.logo_img.grid(column = 0, row = 0)

        self.logo_img.cafe = PhotoImage(file = "cafeImages/logo2.png")
        self.logo_img.create_image(0, 0, anchor = NW, image = self.logo_img.cafe)

        """Creating widgets for the order selecting frame"""
        self.l1 = Label(self.orderSelecting_Frame, text = "Orders:", bg = "#e3cbb3", font = "None, 20")
        self.l1.grid(column = 0, row = 1, sticky = W, padx = 30, pady = (20, 5))

        self.ordersDisplay = ScrolledText(self.orderSelecting_Frame, height = 27, width = 30)
        self.ordersDisplay.grid(column = 0, row = 2, sticky = W, padx = 30)

        self.l2 = Label(self.orderSelecting_Frame, text = "Total: $_____", bg = "#e3cbb3", font = "None, 15")
        self.l2.grid(column = 0, row = 3, sticky = E, padx = 30, pady = (5, 0))

        self.b1 = Button(self.orderSelecting_Frame, text = "Append Orders", command = lambda: self.append_orders(self.order1, self.order2, self.order3, self.order4, self.e1, self.e2, self.e3, self.e4))
        self.b1.grid(column = 0, row = 4, sticky = W, padx = 30)

        self.b2 = Button(self.orderSelecting_Frame, text = "Confirm Order Details", state = "disabled", command = self.append_to_orderDetails)
        self.b2.grid(column = 0, row = 5, sticky = W, padx = 30, pady = (5, 5))

        self.b3 = Button(self.orderSelecting_Frame, text = "Reset Orders", command = self.resetOrders)
        self.b3.grid(column = 0, row = 6, sticky = W, padx = 30)

        #---------------------------------------------------------------------------------------------------------------

        """"""""""""""""""""""""""""""""""""""""""""""""
        """ Creating widgets for each category frame """  
        """"""""""""""""""""""""""""""""""""""""""""""""
        """Creating widgets for coffee frame"""         
        self.coffeebanner = Canvas(self.coffeeFrame, height = 152, width = 700, highlightthickness = 0)
        self.coffeebanner.grid(column = 0, row = 0, sticky = N)

        self.coffeebanner.c_banner = PhotoImage(file = self.menuslides[0].banner)
        self.coffeebanner.create_image(0, 0, anchor = NW, image = self.coffeebanner.c_banner)

        self.coffeeheader = Canvas(self.coffeeFrame, height = 448, width = 700, highlightthickness = 0)
        self.coffeeheader.grid(column = 0, row = 1)

        self.coffeeheader.c_header = PhotoImage(file = self.menuslides[0].header)
        self.coffeeheader.create_image(30, 50, anchor = NW, image = self.coffeeheader.c_header)

        self.sub_headers = Frame(self.coffeeheader, height = 100, width = 300)
        self.sub_headers.place(x = 35, y = 180)

        self.sh_s = Button(self.sub_headers, text = "Sandwiches", font = "None 12 underline", command = lambda: self.show_frame(self.sandwichFrame))
        self.sh_s.grid(column = 0, row = 0, sticky = NW, pady = 5)
        
        self.sh_d = Button(self.sub_headers, text = "Desserts", font = "None 12 underline", command = lambda: self.show_frame(self.dessertFrame))
        self.sh_d.grid(column = 0, row = 1, sticky = NW, pady = 5)

        self.sh_si = Button(self.sub_headers, text = "Sides", font = "None 12 underline", command = lambda: self.show_frame(self.sidesFrame))
        self.sh_si.grid(column = 0, row = 2, sticky = NW)

        self.f1 = Frame(self.coffeeheader, height = 300, width = 250)
        self.f1.place(x = 320, y = 100)

        self.l3 = Label(self.coffeeheader, text = "$", font = "None 15")
        self.l3.place(x = 590, y = 80)

        self.l4 = Label(self.coffeeheader, text = "Qty:", font = "None 15")
        self.l4.place(x = 640, y = 80)

        self.coffeeList = []
        self.coffee = self.menuslides[0].category
        self.coffees = self.coffee.split("#")
        for item in self.coffees:
            self.coffeeList.append(item)

        self.order1 = []  
        self.cb1 = []
        for i in range(len(self.coffeeList)):
            self.v = IntVar()
            self.v.set("0")
            self.cb1.append(Checkbutton(self.f1, text = self.coffeeList[i], variable = self.v, onvalue = 1, offvalue = 0))
            self.cb1[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)
            self.order1.append(self.v)

        self.f2 = Frame(self.coffeeheader)
        self.f2.place(x = 570, y = 100)

        self.costList = []
        self.cost = self.menuslides[0].prices
        self.costs = self.cost.split("#")
        for item2 in self.costs:
            self.costList.append(item2)
        
        self.pricelabels = []
        for i in range(len(self.costList)):
            self.pricelabels.append(Label(self.f2, text = self.costList[i]))
            self.pricelabels[i].grid(column = 0, sticky = NE, ipadx = 10, ipady = 4)
        
        self.f3 = Frame(self.coffeeheader)
        self.f3.place(x = 640, y = 100)
        
        self.v2 = StringVar()
        self.v2.set("")

        self.e1 = []
        for i in range(8):
            self.e1.append(Entry(self.f3, width = 1, bg = "#e3cbb3", font = "None, 12"))
            self.e1[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 2)
        
        self.next_btn = Button(self.coffeeheader, text = ">", command = lambda: self.show_frame(self.sandwichFrame))
        self.next_btn.place(x = 360, y = 400)

        self.previous_btn = Button(self.coffeeheader, text = "<", command = lambda: self.show_frame(self.sidesFrame))
        self.previous_btn.place(x = 340, y = 400)

        self.show_frame(self.coffeeFrame)

        """Creating widgets for sandwich frame"""
        self.sandwichbanner = Canvas(self.sandwichFrame, height = 152, width = 700, highlightthickness = 0)
        self.sandwichbanner.grid(column = 0, row = 0, sticky = N)

        self.sandwichbanner.s_banner = PhotoImage(file = self.menuslides[1].banner)
        self.sandwichbanner.create_image(0, 0, anchor = NW, image = self.sandwichbanner.s_banner)

        self.sandwichheader = Canvas(self.sandwichFrame, height = 448, width = 700, highlightthickness = 0)
        self.sandwichheader.grid(column = 0, row = 1)

        self.sandwichheader.s_header = PhotoImage(file = self.menuslides[1].header)
        self.sandwichheader.create_image(30, 50, anchor = NW, image = self.sandwichheader.s_header)

        self.sub_headers = Frame(self.sandwichheader, height = 100, width = 300)
        self.sub_headers.place(x = 35, y = 180)

        self.sh_c = Button(self.sub_headers, text = "Coffees", font = "None 12 underline", command = lambda: self.show_frame(self.coffeeFrame))
        self.sh_c.grid(column = 0, row = 0, sticky = NW, pady = 5)

        self.sh_d = Button(self.sub_headers, text = "Desserts", font = "None 12 underline", command = lambda: self.show_frame(self.dessertFrame))
        self.sh_d.grid(column = 0, row = 1, sticky = NW, pady = 5)

        self.sh_si = Button(self.sub_headers, text = "Sides", font = "None 12 underline", command = lambda: self.show_frame(self.sidesFrame))
        self.sh_si.grid(column = 0, row = 2, sticky = NW)

        self.f1 = Frame(self.sandwichheader, height = 300, width = 250)
        self.f1.place(x = 320, y = 100)

        self.l3 = Label(self.sandwichheader, text = "$", font = "None 15")
        self.l3.place(x = 590, y = 80)

        self.l4 = Label(self.sandwichheader, text = "Qty:", font = "None 15")
        self.l4.place(x = 640, y = 80)

        self.sandwichList = []
        self.sandwich = self.menuslides[1].category
        self.sandwiches = self.sandwich.split("#")
        for item in self.sandwiches:
            self.sandwichList.append(item)
            
        self.order2 = []
        self.cb2 = []
        for i in range(len(self.sandwichList)):
            self.v2 = IntVar()
            self.v2.set("0")
            self.cb2.append(Checkbutton(self.f1, text = self.sandwichList[i], variable = self.v2, onvalue = 1, offvalue = 0))
            self.cb2[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)
            self.order2.append(self.v2)

        self.f2 = Frame(self.sandwichheader)
        self.f2.place(x = 570, y = 100)

        self.costList2 = []
        self.cost = self.menuslides[1].prices
        self.costs = self.cost.split("#")
        for item2 in self.costs:
            self.costList2.append(item2)
        
        self.pricelabels = []
        for i in range(len(self.costList2)):
            self.pricelabels.append(Label(self.f2, text = self.costList2[i]))
            self.pricelabels[i].grid(column = 0, sticky = NE, ipadx = 10, ipady = 4)
        
        self.f3 = Frame(self.sandwichheader)
        self.f3.place(x = 640, y = 100)
        
        self.v2 = StringVar()
        self.v2.set("")
        self.e2 = []
        for i in range(8):
            self.e2.append(Entry(self.f3, width = 1, bg = "#e3cbb3", font = "None, 12"))
            self.e2[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 2)

        self.next_btn = Button(self.sandwichheader, text = ">", command = lambda: self.show_frame(self.dessertFrame))
        self.next_btn.place(x = 360, y = 400)

        self.previous_btn = Button(self.sandwichheader, text = "<", command = lambda: self.show_frame(self.coffeeFrame))
        self.previous_btn.place(x = 340, y = 400)
        
        """Creating widgets for dessert frame"""
        self.dessertbanner = Canvas(self.dessertFrame, height = 152, width = 700, highlightthickness = 0)
        self.dessertbanner.grid(column = 0, row = 0, sticky = N)

        self.dessertbanner.d_banner = PhotoImage(file = self.menuslides[2].banner)
        self.dessertbanner.create_image(0, 0, anchor = NW, image = self.dessertbanner.d_banner)

        self.dessertheader = Canvas(self.dessertFrame, height = 448, width = 700, highlightthickness = 0)
        self.dessertheader.grid(column = 0, row = 1)

        self.dessertheader.d_header = PhotoImage(file = self.menuslides[2].header)
        self.dessertheader.create_image(30, 50, anchor = NW, image = self.dessertheader.d_header)

        self.sub_headers = Frame(self.dessertheader, height = 100, width = 300)
        self.sub_headers.place(x = 35, y = 180)

        self.sh_c = Button(self.sub_headers, text = "Coffees", font = "None 12 underline", command = lambda: self.show_frame(self.coffeeFrame))
        self.sh_c.grid(column = 0, row = 0, sticky = NW, pady = 5)

        self.sh_s = Button(self.sub_headers, text = "Sandwiches", font = "None 12 underline", command = lambda: self.show_frame(self.sandwichFrame))
        self.sh_s.grid(column = 0, row = 1, sticky = NW, pady = 5)

        self.sh_si = Button(self.sub_headers, text = "Sides", font = "None 12 underline", command = lambda: self.show_frame(self.sidesFrame))
        self.sh_si.grid(column = 0, row = 2, sticky = NW)

        self.f1 = Frame(self.dessertheader, height = 300, width = 250)
        self.f1.place(x = 320, y = 100)

        self.l3 = Label(self.dessertheader, text = "$", font = "None 15")
        self.l3.place(x = 590, y = 80)

        self.l4 = Label(self.dessertheader, text = "Qty:", font = "None 15")
        self.l4.place(x = 640, y = 80)

        self.dessertList = []
        self.dessert = self.menuslides[2].category
        self.desserts = self.dessert.split("#")
        for item in self.desserts:
            self.dessertList.append(item)
        
        self.order3 = []
        self.cb3 = []
        for i in range(len(self.dessertList)):
            self.v3 = IntVar()
            self.v3.set("0")
            self.cb3.append(Checkbutton(self.f1, text = self.dessertList[i], variable = self.v3, onvalue = 1, offvalue = 0))
            self.cb3[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)
            self.order3.append(self.v3)

        self.f2 = Frame(self.dessertheader)
        self.f2.place(x = 570, y = 100)

        self.costList3 = []
        self.cost = self.menuslides[2].prices
        self.costs = self.cost.split("#")
        for item2 in self.costs:
            self.costList3.append(item2)
        
        self.pricelabels = []
        for i in range(len(self.costList3)):
            self.pricelabels.append(Label(self.f2, text = self.costList3[i]))
            self.pricelabels[i].grid(column = 0, sticky = NE, ipadx = 10, ipady = 4)
        
        self.f3 = Frame(self.dessertheader)
        self.f3.place(x = 640, y = 100)
        
        self.v2 = StringVar()
        self.v2.set("")
        self.e3 = []
        for i in range(8):
            self.e3.append(Entry(self.f3, width = 1, bg = "#e3cbb3", font = "None, 12"))
            self.e3[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 2)
        
        self.next_btn = Button(self.dessertheader, text = ">", command = lambda: self.show_frame(self.sidesFrame))
        self.next_btn.place(x = 360, y = 400)

        self.previous_btn = Button(self.dessertheader, text = "<", command = lambda: self.show_frame(self.sandwichFrame))
        self.previous_btn.place(x = 340, y = 400)

        """Creating widgets for sides frame"""
        self.sidesbanner = Canvas(self.sidesFrame, height = 152, width = 700, highlightthickness = 0)
        self.sidesbanner.grid(column = 0, row = 0, sticky = N)

        self.sidesbanner.d_banner = PhotoImage(file = self.menuslides[3].banner)
        self.sidesbanner.create_image(0, 0, anchor = NW, image = self.sidesbanner.d_banner)

        self.sidesheader = Canvas(self.sidesFrame, height = 448, width = 700, highlightthickness = 0)
        self.sidesheader.grid(column = 0, row = 1)

        self.sidesheader.si_header = PhotoImage(file = self.menuslides[3].header)
        self.sidesheader.create_image(30, 50, anchor = NW, image = self.sidesheader.si_header)

        self.sub_headers = Frame(self.sidesheader, height = 100, width = 300)
        self.sub_headers.place(x = 35, y = 180)

        self.sh_c = Button(self.sub_headers, text = "Coffees", font = "None 12 underline", command = lambda: self.show_frame(self.coffeeFrame))
        self.sh_c.grid(column = 0, row = 0, sticky = NW, pady = 5)

        self.sh_s = Button(self.sub_headers, text = "Sandwiches", font = "None 12 underline", command = lambda: self.show_frame(self.sandwichFrame))
        self.sh_s.grid(column = 0, row = 1, sticky = NW, pady = 5)

        self.sh_d = Button(self.sub_headers, text = "Desserts", font = "None 12 underline", command = lambda: self.show_frame(self.dessertFrame))
        self.sh_d.grid(column = 0, row = 2, sticky = NW)

        self.f1 = Frame(self.sidesheader, height = 300, width = 250)
        self.f1.place(x = 320, y = 100)

        self.l3 = Label(self.sidesheader, text = "$", font = "None 15")
        self.l3.place(x = 590, y = 80)

        self.l4 = Label(self.sidesheader, text = "Qty:", font = "None 15")
        self.l4.place(x = 640, y = 80)

        self.sidesList = []
        self.side = self.menuslides[3].category
        self.sides = self.side.split("#")
        for item in self.sides:
            self.sidesList.append(item)
            
        self.order4 = []
        self.cb4 = []
        for i in range(len(self.sidesList)):
            self.v4 = IntVar()
            self.v4.set("0")
            self.cb4.append(Checkbutton(self.f1, text = self.sidesList[i], variable = self.v4, onvalue = 1, offvalue = 0))
            self.cb4[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)
            self.order4.append(self.v4)

        self.f2 = Frame(self.sidesheader)
        self.f2.place(x = 570, y = 100)

        self.costList4 = []
        self.cost = self.menuslides[3].prices
        self.costs = self.cost.split("#")
        for item2 in self.costs:
            self.costList4.append(item2)
        
        self.pricelabels = []
        for i in range(len(self.costList4)):
            self.pricelabels.append(Label(self.f2, text = self.costList4[i]))
            self.pricelabels[i].grid(column = 0, sticky = NE, ipadx = 10, ipady = 4)
        
        self.f3 = Frame(self.sidesheader)
        self.f3.place(x = 640, y = 100)
        
        self.v2 = StringVar()
        self.v2.set("")
        self.e4 = []
        for i in range(8):
            self.e4.append(Entry(self.f3, width = 1, bg = "#e3cbb3", font = "None, 12"))
            self.e4[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 2)
        
        self.next_btn = Button(self.sidesheader, text = ">", command = lambda: self.show_frame(self.coffeeFrame))
        self.next_btn.place(x = 360, y = 400)

        self.previous_btn = Button(self.sidesheader, text = "<", command = lambda: self.show_frame(self.dessertFrame))
        self.previous_btn.place(x = 340, y = 400)
    
    def append_to_orderDetails(self):
        """Order details frame - for gathering information from students and doing payment"""
        self.orderDetails = Frame(self.cafeFrame, height = 600, width = 1000, bg = "#ede0d4")
        self.orderDetails.grid(column = 0, row = 0)
        self.orderDetails.grid_propagate(0)

        self.obanner = Canvas(self.orderDetails, height = 180, width = 1000, bg = "#ede0d4", highlightthickness = 0)
        self.obanner.grid(columnspan = 4, row = 0)

        self.obanner.oimage = PhotoImage(file = "cafeImages/orderdetails.png")
        self.obanner.create_image(0, 0, anchor = NW, image = self.obanner.oimage)

        self.Fname = Label(self.orderDetails, text = "First Name:", font = "None 12 bold", bg = "#ede0d4")
        self.Fname.grid(column = 0, row = 1, sticky = NW, padx = (65, 10), pady = (20, 0))

        self.Lname = Label(self.orderDetails, text = "Last Name:", font = "None 12 bold", bg = "#ede0d4")
        self.Lname.grid(column = 1, row = 1, sticky = NW, pady = (20, 0))

        self.yrlvl = Label(self.orderDetails, text = "Year Level:", font = "None 12 bold", bg = "#ede0d4")
        self.yrlvl.grid(column = 2, row = 1, sticky = NW, pady = (20, 0))

        self.contact = Label(self.orderDetails, text = "Contact Detail - Email:", font = "None 12 bold", bg = "#ede0d4")
        self.contact.grid(column = 3, row = 1, sticky = NW, pady = (20, 0))

        self.first_name = Entry(self.orderDetails)
        self.first_name.grid(column = 0, row = 2, sticky = NW, padx = (65, 0))

        self.last_name = Entry(self.orderDetails)
        self.last_name.grid(column = 1, row = 2, sticky = NW)

        self.year_level = Entry(self.orderDetails, width = 10)
        self.year_level.grid(column = 2, row = 2, sticky = NW)
        
        self.contactdetail = Entry(self.orderDetails)
        self.contactdetail.grid(column = 3, row = 2, sticky = NW)

        self.l1 = Label(self.orderDetails, text = "", bg = "#ede0d4")
        self.l2 = Label(self.orderDetails, text = "", bg = "#ede0d4")
        self.l3 = Label(self.orderDetails, text = "", bg = "#ede0d4")
        self.l4 = Label(self.orderDetails, text = "", bg = "#ede0d4")

        self.Label_1 = Label(self.orderDetails, text = "Orders:", font = "None 12 underline", bg = "#ede0d4")
        self.Label_1.grid(column = 0, row = 3, sticky = NW, padx = (65, 0), pady = (20, 7))

        #-----
        self.f4 = Frame(self.orderDetails, height = 200, width = 615, bg = "#ede0d4")
        self.f4.grid(columnspan = 4, row = 4, sticky = NW, padx = (65, 0))
        self.f4.grid_propagate(0)

        """Quantities"""
        self.f5 = Frame(self.f4, height = 200, width = 100, bg = "#ede0d4")
        self.f5.grid(column = 0, row = 0, sticky = NW, padx = (0, 10))
        self.f5.grid_propagate(0)

        """Orders"""
        self.f6 = Frame(self.f4, height = 200, width = 200, bg = "#ede0d4")
        self.f6.grid(column = 1, row = 0, sticky = NW, padx = (10, 0))
        self.f6.grid_propagate(0)

        """Costs"""
        self.f7 = Frame(self.f4, height = 200, width = 55, bg = "#ede0d4")
        self.f7.grid(column = 2, row = 0, sticky = NE, padx = (240, 0))
        self.f7.grid_propagate(0)

        """Other widgets on the payment frame"""
        self.l5 = Label(self.orderDetails, text = "Total Cost: $" + str(total_price), font = "None 12 bold", bg = "#ede0d4")
        self.l5.place(x = 550, y = 500)

        self.l6 = Label(self.orderDetails, text = "Amount Paying:", font = "None 12 bold", bg = "#ede0d4")
        self.l6.place(x = 830, y = 300)

        self.amount = Entry(self.orderDetails, width = 5)
        self.amount.place(x = 880, y = 325)

        self.l7 = Label(self.orderDetails, text = "", bg = "#ede0d4")

        self.l8 = Label(self.orderDetails, text = "$:", bg = "#ede0d4")
        self.l8.place(x = 855, y = 327)

        self.confirmPayment = Button(self.orderDetails, text = "Confirm Payment", command = self.confirmOrder)
        self.confirmPayment.place(x = 825, y = 360)

        self.exchange = Label(self.orderDetails, text = "Exchanges: $", font = "None 12 underline", bg = "#ede0d4")
        self.exchange.grid(column = 3, row = 4)

        self.newOrder = Button(self.orderDetails, text = "New Order", command = self.back_to_menu)
        self.newOrder.place(x = 870, y = 500)

        self.l9 = Label(self.orderDetails, text = "", bg = "#ede0d4")
        self.l9.place(x = 550, y = 520)
        
        self.print_order_details()
    
    def studentTrackingOrders(self):
        """Student tracking orders for cafe manager to view each student orders"""
        self.trackingFrame = Frame(self.cafeFrame, height = 600, width = 1000, bg = "#ede0d4")
        self.trackingFrame.grid(column = 0, row = 0)
        self.trackingFrame.grid_propagate(0)

        self.sto_banner = Canvas(self.trackingFrame, height = 180, width = 1000, highlightthickness = 0)
        self.sto_banner.grid(column = 0, row = 0, sticky = NW)

        self.sto_banner.main_sto_banner = PhotoImage(file = "cafeImages/studentTracking.png")
        self.sto_banner.create_image(0, 0, anchor = NW, image = self.sto_banner.main_sto_banner)

        self.sto_Label = Label(self.trackingFrame, text = "Student Tracking Orders", font = "None 15 bold", bg = "#ede0d4")
        self.sto_Label.grid(column = 0, row = 1, sticky = NW, padx = 65, pady = 20)

        self.listFrame = Frame(self.trackingFrame, height = 300, width = 860, bg = "#ede0d4")
        self.listFrame.grid(column = 0, row = 2)
        self.listFrame.grid_propagate(0)

        self.row_num = Label(self.listFrame, text = "", font = "None 13 underline", bg = "#ede0d4")
        self.row_num.grid(column = 0, row = 0, sticky = W)

        self.l1 = Label(self.listFrame, text = "Student Name:", font = "None 13 underline bold", bg = "#ede0d4")
        self.l1.grid(column = 1, row = 0, padx = (50, 150), sticky = W)

        self.l2 = Label(self.listFrame, text = "Orders:", font = "None 13 underline bold", bg = "#ede0d4")
        self.l2.grid(column = 2, row = 0, sticky = W)

        self.l3 = Label(self.listFrame, text = "Qty:", font = "None 13 underline bold", bg = "#ede0d4")
        self.l3.grid(column = 3, row = 0, padx = 150, sticky = E)

        self.l4 = Label(self.listFrame, text = "Total Cost:", font = "None 13 underline bold", bg = "#ede0d4")
        self.l4.grid(column = 4, row = 0, sticky = E)

        self.append_to_trackingOrders()
    
    def show_frame(self, frame):
        """Displaying each frames"""
        frame.tkraise()
    
    def back_to_menu(self):
        """Back to menu frame"""
        self.ormistonCafe()
        self.resetOrders()   
    
    def resetOrders(self):
        """Deselecting checkbuttons when back to menu frame"""
        self.ordersDisplay.delete("1.0", tkinter.END)
        self.b2.configure(state = "disabled")

        for widget in self.cb1:
            widget.deselect()
        
        for widget in self.cb2:
            widget.deselect()

        for widget in self.cb3:
            widget.deselect()

        for widget in self.cb4:
            widget.deselect()
        
        for entry in self.e1:
            entry.delete(0, END)
        
        for entry in self.e2:
            entry.delete(0, END)

        for entry in self.e3:
            entry.delete(0, END)
        
        for entry in self.e4:
            entry.delete(0, END)
        
        self.show_frame(self.cafeFrame)

    def append_orders(self, orders_coffee, orders_sandwich, orders_dessert, orders_sides, qty_coffee, qty_sandwich, qty_dessert, qty_sides):
        """Getting orders from each category frame and append to total list"""
        global orders, prices, quantities
        
        self.ordersDisplay.delete("1.0", tkinter.END)

        orders = []
        prices = []
        quantities = []
        self.totalOrders = []

        """Appending coffees"""
        p = []
        for order in orders_coffee:
            if order.get() == 1:
                p.append(orders_coffee.index(order))
        for i in p:
            orders.append(self.coffeeList[i])
            prices.append(self.costList[i])

        self.q = []
        for quantity in qty_coffee:
            self.q.append(quantity.get())
        for i in self.q:
            if len(i) > 0:
                quantities.append(i)
        
        """Appending sandwiches"""
        p2 = []
        for order in orders_sandwich:
            if order.get() == 1:
                p.append(orders_sandwich.index(order))
        for i in p2:
            orders.append(self.sandwichList[i])
            prices.append(self.costList2[i])

        q2 = []
        for quantity in qty_sandwich:
            q2.append(quantity.get())
        for i in q2:
            if len(i) > 0:
                quantities.append(i)
        
        """Appending desserts"""
        p3 = []
        for order in orders_dessert:
            if order.get() == 1:
                p.append(orders_dessert.index(order))
        for i in p3:
            orders.append(self.dessertList[i])
            prices.append(self.costList3[i])

        q3 = []
        for quantity in qty_dessert:
            q3.append(quantity.get())
        for i in q3:
            if len(i) > 0:
                quantities.append(i)
        
        """Appending sides"""
        p4 = []
        for order in orders_sides:
            if order.get() == 1:
                p.append(orders_sides.index(order))
        for i in p4:
            orders.append(self.sidesList[i])
            prices.append(self.costList4[i])

        q4 = []
        for quantity in qty_sides:
            q4.append(quantity.get())
        for i in q4:
            if len(i) > 0:
                quantities.append(i)
        
        self.check_value()
        self.check_index()

    def check_index(self):
        """
        Checking for each orders are entered for a quantity
        Displaying orders on scroll text bar
        """

        self.check_value()
        
        if len(quantities) < len(orders):
            self.ordersDisplay.insert(tkinter.END, "You have not enter the amount of quantites for every orders you want.")
            self.ordersDisplay.insert(tkinter.END, "\n")
            self.ordersDisplay.insert(tkinter.END, "Please enter the amount for each orders.")
        else:
            if len(quantities) == len(orders):
                for i in range(len(orders)):
                    self.totalOrders.append([quantities[i], orders[i], prices[i]])
    
    def check_value(self):
        """Checking for integers only on entering quantities for orders"""
        global total_price

        self.check_index()

        for i in quantities:
            try:
                t = []
                for i in range(len(orders)):
                    a = int(float(prices[i]))
                    b = int(quantities[i])
                    t.append(a * b)
                total_price = "{:.2f}".format(sum(t))
                self.l2.configure(text = "Total: $" + str(total_price))

                """Displaying on order displaying frame - ScrollTextBar"""
                for i in range(len(orders)):
                    self.ordersDisplay.insert(tkinter.END, quantities[i] + "x " + orders[i] + " $" + prices[i])
                    self.ordersDisplay.insert(tkinter.END, "\n")
                    
                self.b2.configure(state = "normal")
                
            except ValueError:
                self.ordersDisplay.insert(tkinter.END, "Invalid input for quantities")
                self.ordersDisplay.insert(tkinter.END, "\n")
                self.ordersDisplay.insert(tkinter.END, "Please enter integers only for quantities wanted.")
    
    def check_int(self, entry):
        """Checking for string values only"""
        while entry.isdigit():
            if True:
                self.l9.configure(text = "*String values only")
            break
    
    def check_str(self, entry):
        """Checking for integers only"""
        if entry.isdigit():
            pass
        else:
            self.l9.configure(text = "*Integer values only")
    
    def check_amount(self):
        """Checking if money inputted is integer"""
        while True:
            if self.amount.get().isdigit():
                break
            else:
                self.l9.configure(text = "*Integers only")

    def print_order_details(self):
        """Displaying orders on order detail frame"""
        order_count = 0
        while order_count < len(self.totalOrders):
            Label(self.f5, text = (self.totalOrders[order_count][0] + "x"), bg = "#ede0d4").grid(column = 0, row = order_count, sticky = W)
            Label(self.f6, text = (self.totalOrders[order_count][1]), bg = "#ede0d4").grid(column = 0, row = order_count, sticky = W) 
            Label(self.f7, text = "$" + (self.totalOrders[order_count][2]), bg = "#ede0d4").grid(column = 0, row = order_count, sticky = W)  
            order_count +=  1
    
    def confirmOrder(self):
        """Checking values for each student detail entry"""
        self.check_int(self.first_name.get())
        self.check_int(self.last_name.get())
        self.check_int(self.contactdetail.get())
        self.check_str(self.year_level.get())

        """Appending to CafeOrders class as a list - DailyOrders)"""
        self.cafeDailyOrders = CafeOrders(self.first_name.get().capitalize(), self.last_name.get().capitalize(), self.year_level.get(), self.contactdetail.get(), orders, prices, quantities, total_price, self.totalOrders)
        self.DailyOrders.append(self.cafeDailyOrders)

        self.check_amount()

        """
        Checking if user has enter enough money
        Calculating exchanges and displaying it
        """
        while True:
            if int(float(self.amount.get())) >= int(float(total_price)):
                exchange = int(float(self.amount.get())) - int(float(total_price))
                self.l6.configure(text = "Amount Paid:")
                self.l7.place(x = 880, y = 325)
                self.l7.configure(text = "$" + self.amount.get())
                self.l8.destroy()
                
                self.exchange.configure(text = "Exchanges: $" + "{:.2f}".format(int(exchange)))
                self.append_to_file()
                self.print_student_detail()
                self.amount.destroy()
                self.confirmPayment.destroy()
                break
            else:
                self.exchange.configure(text = "* You have not paid enough")

    def print_student_detail(self):
        """Printing final order details"""
        self.l1.grid(column = 0, row = 2, sticky = NW, padx = (65, 0))
        self.l2.grid(column = 1, row = 2, sticky = NW)
        self.l3.grid(column = 2, row = 2, sticky = NW)
        self.l4.grid(column = 3, row = 2, sticky = NW)

        self.l1.configure(text = self.first_name.get())
        self.l2.configure(text = self.last_name.get())
        self.l3.configure(text = self.year_level.get())
        self.l4.configure(text = self.contactdetail.get())

        self.first_name.destroy()
        self.last_name.destroy()
        self.year_level.destroy()
        self.contactdetail.destroy()
    
    def append_to_file(self):
        """Appending to cafeDailyOrders file to keep track of student orders"""
        order_count = 0
        while order_count < len(self.DailyOrders):
            storing_orders = open("cafeDailyOrders.txt", "a")
            storing_orders.write("{}, {}, {}, {}, {}, {}, {}, {}".format(self.DailyOrders[order_count].fName, self.DailyOrders[order_count].lName, self.DailyOrders[order_count].year, self.DailyOrders[order_count].contact, self.DailyOrders[order_count].order, self.DailyOrders[order_count].price, self.DailyOrders[order_count].quantity, self.DailyOrders[order_count].totalPrice))
            storing_orders.write("\n")
            order_count += 1
    
    def append_to_trackingOrders(self):
        """Displaying each student's order details on student tracking orders frame"""
        order_count = 0
        row_num = 0
        while order_count < len(self.DailyOrders):
            Label(self.listFrame, text = order_count, bg = "#ede0d4").grid(column = 0, row = order_count + 1 + row_num) 
            Label(self.listFrame, text = (self.DailyOrders[order_count].fName + " " + self.DailyOrders[order_count].lName), bg = "#ede0d4").grid(column = 1, row = order_count + 1 + row_num, sticky = W, padx = (50, 150))
            for i in range(len(self.DailyOrders[order_count].order)):
                Label(self.listFrame, text = (self.DailyOrders[order_count].order[i]), bg = "#ede0d4").grid(column = 2, row = order_count + 1 + i + row_num, sticky = W) 
                Label(self.listFrame, text = (self.DailyOrders[order_count].quantity[i]), bg = "#ede0d4").grid(column = 3, row = order_count + 1 + i + row_num, sticky = E, padx = 150)
            Label(self.listFrame, text = "$" + (self.DailyOrders[order_count].totalPrice), bg = "#ede0d4").grid(column = 4, row = order_count + len(self.DailyOrders[order_count].order) + row_num, sticky = E)
            Label(self.listFrame, text = "------------------------------------------------------------------------------------------------------------------------------------------", bg = "#ede0d4").grid(columnspan = 5, column = 0, row = order_count + 1 + len(self.DailyOrders[order_count].order) + row_num, sticky = W)
            row_num += len(self.DailyOrders[order_count].order)
            order_count +=  1 
    

class CafeMenuDetails:
    def __init__(self, banner, header, category, prices):
        self.banner = banner
        self.header = header
        self.category = category
        self.prices = prices
    
class CafeOrders:
    def __init__(self, fName, lName, year, contact, order, price, quantity, totalPrice, totalOrders):
        self.fName = fName
        self.lName = lName
        self.year = year
        self.contact = contact
        self.order = order
        self.price = price
        self.quantity = quantity
        self.totalPrice = totalPrice
        self.totalOrders = totalOrders

#Main Routine
if __name__ == "__main__":                        
    root = tk.Tk()
    CafeInterface(root)
    root.title("Cafe Interface")
    root.mainloop()