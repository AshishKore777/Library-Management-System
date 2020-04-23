from func1 import *
import sys
import getpass
a=3

while a!=0:

    passw = getpass.getpass("Enter the password:")
    if passw =="12345":
        print("**********WELCOME TO THE LIBRARY**********")
        while True:


            print('Press 1 : Student related Functionalities')

            print('Press 2 : Faculty related Functionalities')

            print('Press 3 : Book related Functionalities')

            print('Press 4 : Exit')

            choice = int(input('Enter Your Choice: '))

            if choice == 1:
                while True:
                    print('*'*38)

                    print('Press 1 : Add Student')

                    print('Press 2 : Display Student list')

                    print('Press 3 : Issue Book')

                    print('Press 4 : Return Book')

                    print('Press 5 : Main Menu')

                    ch = int(input('Enter Your Choice: '))

                    if ch == 1:

                        add_student()

                    elif ch == 2:

                        print_srecord()

                    elif ch == 3:

                        issue_book_student()

                    elif ch == 4:

                        return_book_student()

                    elif ch == 5:

                        break

            elif choice == 2:
                while True:
                    print('*'*38)

                    print('Press 1 : Add Faculty ')

                    print('Press 2 : Display Faculty list')

                    print('Press 3 : Issue Book')

                    print('Press 4 : Return Book')

                    print('Press 5 : Main Menu')

                    ch = int(input('Enter Your Choice: '))

                    if ch == 1:

                        add_faculty()

                    elif ch == 2:

                        print_frecord()

                    elif ch == 3:

                        issue_fac()

                    elif ch == 4:

                        return_fac()

                    elif ch == 5:

                        break

            elif choice == 3:
                while True:
                    print('*'*38)

                    print('Press 1 : Add Book to Library')

                    print('Press 2 : Display List of Books')
                    
                    print('Press 3 : Search Book')

                    print('Press 4 : Main Menu')

                    ch = int(input('Enter Your Choice: '))

                    if ch == 1:

                        add_book()

                    elif ch == 2:

                        print_brecord()
                        
                    elif ch == 3:

                        search()
                        
                    elif ch == 4:

                        break

            else:

                sys.exit(0)

    a=a-1
    print(a,'attempts left')