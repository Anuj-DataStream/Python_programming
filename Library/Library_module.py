class library:
        
    def __init__(self):
        self.list_books=[]
    def add(self,inbooks):
        self.list_books.append(inbooks)
    def show(self):
        x=0
        if len(self.list_books) == 0:
            print("Library is empty")
        for i in self.list_books:
            x+=1
            print(f"{x}.) {i}")
    def count(self):
        return len((self.list_books))

    def addlib(self):
        with open("library.txt", "a+") as file:
            for index, items in enumerate(self.list_books, 1):
                file.write(f"{index}. {items}\n")


if __name__ == "__main__":
    print("This will only run if Library_module.py is executed directly.")