class Library:
    def __init__(self, list, name): #function 1
        self.booksList = list
        self.name = name
        self.lendDict = {} 
    def displayBooks(self):         #function 2
        print(f"The following books are available in the Library: {self.name}")
        for book in self.booksList:
            print(book)
    def lendBook(self, user, book): #function3
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("The Lender-Book database has been updated. You can issue the book now.")
        else:
            print(f"Book has been already issued by {self.lendDict[book]}")
    def addBook(self, book):        #function4
        self.booksList.append(book)
        print("Book has been added to the books list")
    def returnBook(self, user, book): #function 5
        self.lendDict.pop(book)
        print("Thank you for returning the book!")
if __name__ == '__main__':
    sgsits = Library(['Balaguruswamy', 'B.S. Grewal', 'Harry Potter', 'Inferno', 'Alchemist'], "SGSITS")
    while(True):
        print(f"Welcome to {sgsits.name} library. Enter your choice to continue:")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Invalid option")
            print("Enter a valid option")
            continue
        else:
            user_choice = int(user_choice)
        if user_choice == 1:
            sgsits.displayBooks()
        elif user_choice == 2:
            book = input("Enter name of the book you want to lend:")
            user = input("Enter your name:")
            enr = input("Enter your enrollment number:")
            sgsits.lendBook(user, book)
        elif user_choice == 3:
            book = input("Enter name of the book you want to add:")
            sgsits.addBook(book)
        elif user_choice == 4:
            book = input("Enter name of the book you want to return:")
            user = input("Enter your name:")
            enr = input("Enter your enrollment number:")
            sgsits.returnBook(user,book)
        else:
            print("Invalid Option")
        print("Press e to exit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="e"):
            user_choice2 = input()
            if user_choice2 == "e":
                exit()
            elif user_choice2 == "c":
                continue

