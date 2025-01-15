class temp:
    def __init__(self):
        self.name = "temp"

    def my_func(self):
        print("my_func:temp")

class bump:
    def __init__(self):
        self.name = "bump"

    def my_func(self):
        print("my_func:bump")

class TempBump(temp,bump):
    def my_func1(self):
        print("my_func:TempBump")

tb = TempBump()
tb.my_func()
