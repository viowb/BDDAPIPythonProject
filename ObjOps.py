class Ipad:
    size = 15
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def getData(self):
        print("Width:", self.width)
        print("Height:", self.height)
        print("X:", self.x)
        print("Y:", self.y)
        return (self.width, self.height)

    def setData(self, width, height):
        self.width = width
        self.height = height
        self.x = width
        self.y = height

print("QA automating from my Ipad")

#creating object for the class
#synthax to create objects in python
obj = Ipad(10, 20)  # pass required arguments
obj.getData()
print("Size:", obj.size)



