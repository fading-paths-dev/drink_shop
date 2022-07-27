from drinks import Drink, Milkshake, Smoothie, IcedTea
from tkinter import *

drink = Drink("Cassie")
milkshake = Milkshake(0)
smoothie = Smoothie(0)
iced_tea = IcedTea(0)


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link to function call
        exit_button = Button(self, text="Leave shop", command=self.click_exit_button)
        milkshake_button = Button(self, text="Milkshake", command=self.click_milkshake_button)
        smoothie_button = Button(self, text="Smoothie", command=self.click_smoothie_button)
        iced_tea_button = Button(self, text="Iced Tea", command=self.click_iced_tea_button)
        complete_order_button = Button(self, text="Complete Order", command=self.click_complete_order_button)
        info_button = Button(self, text="Info?", command=self.click_info_button)

        # place button
        exit_button.place(x=250, y=0)
        milkshake_button.place(x=40, y=50)
        smoothie_button.place(x=120, y=50)
        iced_tea_button.place(x=200, y=50)
        complete_order_button.place(x=100, y=150)
        info_button.place(x=130, y=100)

    def click_exit_button(self):
        exit()

    def click_milkshake_button(self):
        milkshake.count += 1
        print(milkshake.repeat_order())

    def click_smoothie_button(self):
        smoothie.count += 1
        print(smoothie.repeat_order())

    def click_iced_tea_button(self):
        iced_tea.count += 1
        print(iced_tea.repeat_order())

    def click_complete_order_button(self):
        print(f"Here is your {milkshake.count} milkshakes, {smoothie.count} smoothies and {iced_tea.count} iced teas")

    def click_info_button(self):
        print(drink.info())
        print(milkshake.info())
        print(smoothie.info())
        print(iced_tea.info())
