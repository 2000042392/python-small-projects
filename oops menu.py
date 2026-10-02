# class  InsufficientBalance(Exception):
#     pass
#
# class Bank:
#     def __init__(self):
#         self.acctno = int(input("Enter Account Number: "))
#         self.balance = int(input("Enter Balance: "))
#
#     def withdraw(self):
#         amount = int(input("Enter amount to withdraw: "))
#         try:
#             if amount > self.balance:
#                 raise InsufficientBalance("Insufficient Balance")
#             self.balance -= amount
#             print("Withdrawal Successful")
#             print("Remaining Balance:", self.balance)
#         except InsufficientBalance as e:
#             print(e)
#
#     def deposit(self):
#         amount = int(input("Enter amount to deposit: "))
#         self.balance += amount
#         print("Remaining Balance:", self.balance)
#
#     def check_balance(self):
#         print("Current Balance:", self.balance)
#
#
# l = []
#
# while True:
#     print("\n1. Create Account")
#     print("2. Withdraw")
#     print("3. Deposit")
#     print("4. Check Balance")
#     print("5. Exit")
#
#     choice = int(input("Enter your choice: "))
#
#     if choice == 1:
#         b = Bank()
#         l.append(b)
#
#     elif choice == 2:
#         acctno = int(input("Enter Account Number: "))
#         for i in l:
#             if i.acctno == acctno:
#                 i.withdraw()
#                 break
#         else:
#             print("Invalid Account Number")
#
#     elif choice == 3:
#         acctno = int(input("Enter Account Number: "))
#         for i in l:
#             if i.acctno == acctno:
#                 i.deposit()
#                 break
#         else:
#             print("Invalid Account Number")
#
#     elif choice == 4:
#         acctno = int(input("Enter Account Number: "))
#         for i in l:
#             if i.acctno == acctno:
#                 i.check_balance()
#                 break
#         else:
#             print("Invalid Account Number")
#
#     elif choice == 5:
#         print("Thank You for choosing us")
#         break
#
#     else:
#         print("Invalid Choice")
# 1. Add Book
# 2. View Books
# 3. Issue Book
# 4. Remove Book
# 5. Exit
class booknotavailable(Exception):
    pass


class book:
    def __init__(self):
        self.name = input("Enter book name: ")
        self.bookno = int(input("Enter book number: "))

    def display(self):
        print("Book Name:", self.name)
        print("Book Number:", self.bookno)

    def issue(self):
        print("Book issued successfully")

    def remove(self):
        print("Book removed successfully")


l = []

while True:
    print("\n1. Add book")
    print("2. Display books")
    print("3. Issue book")
    print("4. Remove book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        b = book()
        l.append(b)
        print("Book added successfully")

    elif choice == 2:
        if len(l) == 0:
            print("No books available")
        else:
            for i in l:
                i.display()

    elif choice == 3:
        bookno = int(input("Enter book number: "))

        for i in l:
            if i.bookno == bookno:
                i.issue()
                break
        else:
            try:
                raise booknotavailable("Book not available")
            except booknotavailable as e:
                print(e)

    elif choice == 4:
        bookno = int(input("Enter book number: "))

        for i in l:
            if i.bookno == bookno:
                l.remove(i)
                print("Book removed successfully")
                break
        else:
            print("Book not available")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
