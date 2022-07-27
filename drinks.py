class Drink:
    def __init__(self, name):
        self.name = name

    def repeat_order(self):
        return "Please order a drink" + ", " + self.name

    def make_order(self):
        pass

    def info(self):
        return "A drink is a liquid consumed to prevent death"

    def __str__(self):
        return self.name


class Milkshake(Drink):
    def __init__(self, count):
        super().__init__("Milkshake")
        self.count = count

    def repeat_order(self):
        if self.count == 1:
            return "1 milkshake"
        else:
            return "So that's " + str(self.count) + " " + "milkshakes"

    def make_order(self):
        pass

    def info(self):
        return "A milkshake is a cold drink made of milk, a sweet flavouring such as fruit or chocolate, " \
               "and typically ice cream, whisked until it is frothy"


class Smoothie(Drink):
    def __init__(self, count):
        super().__init__("Smoothie")
        self.count = count

    def repeat_order(self):
        if self.count == 1:
            return "1 smoothie"
        else:
            return "So that's " + str(self.count) + " " + "smoothies"

    def make_order(self):
        pass

    def info(self):
        return "A smoothie is a thick, smooth drink of fresh fruit pureed with milk, yogurt, or ice cream"


class IcedTea(Drink):
    def __init__(self, count):
        super().__init__("Iced tea")
        self.count = count

    def repeat_order(self):
        if self.count == 1:
            return "1 iced tea"
        else:
            return "So that's " + str(self.count) + " " + "iced teas"

    def make_order(self):
        pass

    def info(self):
        return "Iced tea is a chilled drink of sweetened tea without milk, typically flavoured with lemon"

