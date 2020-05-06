class Polo():
    def __init__(self, color, size, price=99.00, style=None):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    def wash(self):
        print("Wash this shit {self.size} {self.color}")

    
    def fold(self):
        print("fold this shit")


if __name__ == "__main__":

    #df = DataFrame(...)
    # df.head()
    polo1 = Polo(color="Blue", size="L", price=4.99)
    print(polo1.color)
    print(polo1.price)
    print(polo1.fullname)
    polo1.wash()

    polo2 = Polo(color="Yello", size="Small")
    print(polo2.color)
    print(polo2.price)
    polo2.fold()