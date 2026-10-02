class studentnotfoundexception(Exception):
    pass
class student:
     def __init__(self):
         self.name=""
         self.rollno=0
         self.mark=0
     def add(self):
        self.name=input("Enter your name: ")
        self.rollno=int(input("Enter your roll number: "))
        self.mark=int(input("Enter your marks: "))
     def display(self):
        print(self.name," ",self.rollno," ",self.mark)

l=[]
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        s=student()
        s.add()
        l.append(s)
    elif choice==2:
        for i in l:
            i.display()
    elif choice==3:
        try:
         for i in l:

            rollno=int(input("Enter your roll number: "))
            if rollno==i.rollno:

                print("student found")
                i.display()
                break
            else:
                raise studentnotfoundexception("student not found")
        except Exception as e:
            print(e)
    elif choice==4:
        for i in l:
            rollno=int(input("Enter your roll number: "))
            mark=int(input("Enter your  new marks: "))
            if rollno==i.rollno:
                print("student data update")
                break
            else:
                print("student not found")
    elif choice==5:
        for i in l:
            rollno=int(input("Enter your roll number: "))
            if rollno==i.rollno:
                 l.remove(i)
                 print("student delete")
                 break
            else:
             print("student not found")
    elif choice==6:
        print("exit")
    else:
        print("invalid choice")












