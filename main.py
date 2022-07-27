
from gui import *

if __name__ == '__main__':
    b = Drink("Cassie")
    print(b.repeat_order())
    root = Tk()
    app = Window(root)
    root.wm_title("Ye Olde Drinks Shop")
    root.geometry("320x200")
    root.mainloop()

