class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lenddict={}
    def displaybook(self):
        print("We have the following book in our ",{self.name})
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-Book database has been update you can take the book now")
        else:
            print("The book has been already occupied by",{self.lenddict[book]})

    def addBook(self,book):

        self.booklist.append(book)
        print("Your Book has been Updated Enjoy your day")

    def returnBook(self,book):
        self.lendBook.remove(book)
if __name__=='__main__':
    ankur=Library(["Ank","bnk","cnk","dnk","enk"],"Ankurlibrary")
    while True:
        print("Welcome to " + ankur.name + "\nWhat Action You want to perform:\n1 : Display Book\n2 : Lend Book\n3 : Add Book\n4 : Return Book")
        user_choise=int(input())
        if(user_choise==1):
            ankur.displaybook()
        elif (user_choise == 2):
            user=input("Enter your name")
            book=input("Enter book name")
            ankur.lendBook(user,book)
        elif (user_choise == 3):
            book=input("Enter book Name to ADD")
            ankur.addBook(book)

        elif (user_choise == 4):
            book=input("Enter book you want to return")
            ankur.returnBook(book)
        else:
            print("Not a valid option")
        print("Press q to continue or c to quit")
        user_choice2 = input()
        if(user_choice2=="q"):
            continue
        else:
            break


