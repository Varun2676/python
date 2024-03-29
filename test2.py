class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}
    def displayBooks(self):
        print(f"The following books are available in the Library: {self.name}")
        for book in self.booksList:
            print(book)
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the books list")
    def returnBook(self, user, book):
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
        print("Press e to exit or c to continue")
        user_choice = input()
        if user_choice not in ['1','2','3','4','c','e']:
            print("Invalid Option")
            print("Enter a valid option")
            continue
        else:
            if int(user_choice) == 1:
                sgsits.displayBooks()
            elif int(user_choice) == 2:
                book = input("Enter name of the book you want to lend:")
                user = input("Enter your name:")
                enr = input("Enter your enrollment number:")
                sgsits.lendBook(user, book)
            elif int(user_choice) == 3:
                book = input("Enter name of the book you want to add:")
                sgsits.addBook(book)
            elif int(user_choice) == 4:
                book = input("Enter name of the book you want to return:")
                user = input("Enter your name:")
                enr = input("Enter your enrollment number:")
                sgsits.returnBook(user,book)
            else:
                if user_choice == "e":
                    exit()
                elif user_choice == "c":
                    continue
