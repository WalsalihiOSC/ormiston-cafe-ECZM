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

        """Order selecting frame will be on top of the main cafe frame"""
        self.orderSelecting_Frame = Frame(self.main_cafeFrame, height = 600, width =300, bg = "#e3cbb3")
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

        self.b1 = Button(self.orderSelecting_Frame, text = "Append Orders", command = lambda: self.append_orders(self.selected_coffee, self.selected_sandwich, self.selected_dessert, self.selected_sides, self.e1, self.e2, self.e3, self.e4))
        self.b1.grid(column = 0, row = 4, sticky = W, padx = 30)

        self.b2 = Button(self.orderSelecting_Frame, text = "Confirm Order Details", state = "disabled", command = self.append_to_orderDisplay)
        self.b2.grid(column = 0, row = 5, sticky = W, padx = 30, pady = (5, 5))

        self.b3 = Button(self.orderSelecting_Frame, text = "Reset Orders")
        self.b3.grid(column = 0, row = 6, sticky = W, padx = 30)

        #---------------------------------------------------------------------------------------------------------------
        """Creating frames for each menu category"""
        self.main_menuFrame = Frame(self.main_cafeFrame, height = 600, width = 700)
        self.main_menuFrame.grid(column = 1, row = 0)

        self.coffeeFrame = Frame(self.main_menuFrame, height = 600, width = 700)
        self.sandwichFrame = Frame(self.main_menuFrame, height = 600, width = 700)
        self.dessertFrame = Frame(self.main_menuFrame, height = 600, width = 700)
        self.sidesFrame = Frame(self.main_menuFrame, height = 600, width = 700)

        for frame in (self.coffeeFrame, self.sandwichFrame, self.dessertFrame, self.sidesFrame):
            frame.grid(column = 0, row = 0, sticky = NSEW)

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

        ###still need to work on label event binding, if not then change label to button instead
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

        self.coffee_l = [str(x) for x in range(len(self.coffeeList))]
        self.selected_coffee = []
            
        self.cb1 = []
        for i in range(len(self.coffeeList)):
            self.coffee_l[i] = IntVar(0)
            self.cb1.append(Checkbutton(self.f1, text = self.coffeeList[i], variable = self.coffee_l[i], onvalue = 1, offvalue = 0, command = lambda x = self.coffeeList[i], y = self.coffee_l[i]: self.add_remove_coffee(x,y)))
            self.cb1[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)

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
            
        self.sandwich_l = [str(x) for x in range(len(self.sandwichList))]
        self.selected_sandwich = []
            
        self.cb1 = []
        for i in range(len(self.sandwichList)):
            self.sandwich_l[i] = IntVar(0)
            self.cb1.append(Checkbutton(self.f1, text = self.sandwichList[i], variable = self.sandwich_l[i], onvalue = 1, offvalue = 0, command = lambda x = self.sandwichList[i], y = self.sandwich_l[i]: self.add_remove_sandwich(x,y)))
            self.cb1[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)

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
            
        self.dessert_l = [str(x) for x in range(len(self.dessertList))]
        self.selected_dessert = []
            
        self.cb1 = []
        for i in range(len(self.dessertList)):
            self.dessert_l[i] = IntVar(0)
            self.cb1.append(Checkbutton(self.f1, text = self.dessertList[i], variable = self.dessert_l[i], onvalue = 1, offvalue = 0, command = lambda x = self.dessertList[i], y = self.dessert_l[i]: self.add_remove_dessert(x,y)))
            self.cb1[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)

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
            
        self.sides_l = [str(x) for x in range(len(self.sidesList))]
        self.selected_sides = []
            
        self.cb1 = []
        for i in range(len(self.sidesList)):
            self.sides_l[i] = IntVar(0)
            self.cb1.append(Checkbutton(self.f1, text = self.sidesList[i], variable = self.sides_l[i], onvalue = 1, offvalue = 0, command = lambda x = self.sidesList[i], y = self.sides_l[i]: self.add_remove_sides(x,y)))
            self.cb1[i].grid(column = 0, sticky = W, ipadx = 10, ipady = 5)

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
        
    def show_frame(self, frame):
        frame.tkraise()
    
    def append_to_orderDisplay(self):
        self.main_menuFrame.destroy()
        self.orderSelecting_Frame.destroy()

        self.orderDisplay = Frame(self.main_cafeFrame, height = 600, width = 1000, bg = "#ede0d4")
        self.orderDisplay.grid(column = 0, row = 0)
        self.orderDisplay.grid_propagate(0)

        self.obanner = Canvas(self.orderDisplay, height = 180, width = 1000, bg = "#ede0d4", highlightthickness = 0)
        self.obanner.grid(columnspan = 4, row = 0)

        self.obanner.oimage = PhotoImage(file = "cafeImages/orderdetails.png")
        self.obanner.create_image(0, 0, anchor = NW, image = self.obanner.oimage)

        self.Fname = Label(self.orderDisplay, text = "First Name:", font = "None 12 bold", bg = "#ede0d4")
        self.Fname.grid(column = 0, row = 1, sticky = NW, padx = (65, 10), pady = (20, 0))

        self.Lname = Label(self.orderDisplay, text = "Last Name:", font = "None 12 bold", bg = "#ede0d4")
        self.Lname.grid(column = 1, row = 1, sticky = NW, pady = (20, 0))

        self.yrlvl = Label(self.orderDisplay, text = "Year Level:", font = "None 12 bold", bg = "#ede0d4")
        self.yrlvl.grid(column = 2, row = 1, sticky = NW, pady = (20, 0))

        self.contact = Label(self.orderDisplay, text = "Contact Detail - Email:", font = "None 12 bold", bg = "#ede0d4")
        self.contact.grid(column = 3, row = 1, sticky = NW, pady = (20, 0))

        self.first_name = Entry(self.orderDisplay)
        self.first_name.grid(column = 0, row = 2, sticky = NW, padx = (65, 0))

        self.last_name = Entry(self.orderDisplay)
        self.last_name.grid(column = 1, row = 2, sticky = NW)

        self.year_level = Entry(self.orderDisplay, width = 10)
        self.year_level.grid(column = 2, row = 2, sticky = NW)
        
        self.contactdetail = Entry(self.orderDisplay)
        self.contactdetail.grid(column = 3, row = 2, sticky = NW)

        self.Label_1 = Label(self.orderDisplay, text = "Orders:", bg = "#ede0d4")
        self.Label_1.grid(column = 0, row = 3, sticky = NW, padx = (65, 0), pady = (20, 7))

        #-----
        self.f4 = Frame(self.orderDisplay, height = 200, width = 615, bg = "#ede0d4")
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
        self.l5 = Label(self.orderDisplay, text = "Total Cost: $", bg = "#ede0d4")
        self.l5.place(x = 550, y = 500)

        self.l6 = Label(self.orderDisplay, text = "Amount Paying:", bg = "#ede0d4")
        self.l6.place(x = 830, y = 300)

        self.amount = Entry(self.orderDisplay, width = 5)
        self.amount.place(x = 880, y = 325)

        self.l7 = Label(self.orderDisplay, text = "$:", bg = "#ede0d4")
        self.l7.place(x = 855, y = 327)

        self.confirmPayment = Button(self.orderDisplay, text = "Confirm Payment", command = self.confirmOrder)
        self.confirmPayment.place(x = 825, y = 360)

        self.exchange = Label(self.orderDisplay, text = "Exchanges: $", bg = "#ede0d4")
        self.exchange.grid(column = 3, row = 4)

        self.newOrder = Button(self.orderDisplay, text = "New Order")
        self.newOrder.place(x = 870, y = 500)

        self.cafeDailyOrders = CafeOrders(self.first_name.get(), self.last_name.get(), self.year_level.get(), self.contactdetail.get(), 0,0,0,0)

        self.DailyOrders.append(self.cafeDailyOrders)


class CafeMenuDetails:
    def __init__(self, banner, header, category, prices):
        self.banner = banner
        self.header = header
        self.category = category
        self.prices = prices
    
class CafeOrders:
    def __init__(self, fName, lName, year, contact, order, price, quantity, totalPrice):
        self.fName = fName
        self.lName = lName
        self.year = year
        self.contact = contact
        self.order = order
        self.price = price
        self.quantity = quantity
        self.totalPrice = totalPrice
    
#Main Routine
if __name__ == "__main__":                        
    root = tk.Tk()
    CafeInterface(root)
    root.title("Cafe Interface")
    root.mainloop()