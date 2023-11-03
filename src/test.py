class test1:
    def __init__(self):
        self.thislist = ["apple", "banana", "cherry"]

    def change_this_list(self):
        self.thislist.append("orange")

    def print_this_list(self):
        print(self.thislist)


class test2:
    def __init__(self):
        self.test = test1()
        self.test3 = test3(self.test)

    def change_this_list(self):
        self.test.change_this_list()
    
    def print_this_list(self):
        self.test.print_this_list()
    
    def print_this_list2(self):
        self.test3.print_this_list()

class test3:
    def __init__(self, test):
        self.test = test
    
    def print_this_list(self):
        self.test.print_this_list()

test = test2()
test.print_this_list()
test.print_this_list2()
test.change_this_list()
test.print_this_list()
test.print_this_list2()
