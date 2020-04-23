from student import Student
from faculty import Faculty
from datetime import date
import pickle
count_s=0
count_f=0
l=[]
def add_student():
    global count_s
    
    print(count_s)
    name=input("Enter the name of the student:")
    add_year=input("Enter the addmission year:")
    
    while True:
        if int(add_year) > date.today().year:
            print("Invalid Year!!")
            add_year=input("Enter the addmission year:")
        else:
            break
    
    ad_id_no=input("Enter the addmission id number:")
    
    while True:
        if len(ad_id_no)!=4:
            print("Invalid Admission Id!!")
            ad_id_no=input("Enter the addmission id number:")
        else:
            break
    
    branch=input("Enter the branch:")
    r_no="0187"+branch+add_year+ad_id_no
    
    if count_s==0:
        
        s=Student(name,add_year,branch,ad_id_no,r_no)
        l.append(s)
        print(l[count_s].name)
        with open("student_record.pkl","wb") as f:
            pickle.dump(l,f)
        count_s+=1
    elif(check_student(r_no)):
            print("Student already exists!!")
    else:
        
        
        s=Student(name,add_year,branch,ad_id_no,r_no)
        l.append(s)
        #print(l[count_s-1].name)
        count_s+=1
        with open("student_record.pkl","wb") as f:
            pickle.dump(l,f)    
    
    
def check_student(r_no):
    with open("student_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].r_no==r_no:
                    return True
                i+=1
            except (EOFError,IndexError):
                return False
    
import pickle
def print_srecord():
    with open("student_record.pkl","rb") as f:
            obj=pickle.load(f)
            i=0
            while True:
                try:
                    #display(obj[i])
                    print(f"Name:{obj[i].name}\nAdmission Year:{obj[i].add_year}\nBranch:{obj[i].branch}")
                    print(f"Admission Id:{obj[i].ad_id_no}\nRoll No.:{obj[i].r_no}")
                    print(f"Books Issued:{obj[i].book_issued}")

                    i+=1
                except (EOFError,IndexError):
                    print("end")
                    break


from faculty import Faculty
import pickle
count_f=0
l2=[]
def add_faculty():
    global count_f
    count_f+=1
    print(count_f)
    name=input("Enter the name of the Faculty:")
    
    fac_id=input("Enter the Faculty Id:")
    
    while True:
        if len(fac_id)!=5:
            print("Invalid Faculty Id!!")
            fac_id=input("Enter the Faculty Id:")
        else:
            break
    
    if count_f==1:
        fac=Faculty(name,fac_id)
        l2.append(fac)
        with open("faculty_record.pkl","wb") as f:
            pickle.dump(l2,f)
    elif(check_faculty(fac_id)):
            print("Faculty already exists!!")
    else:
        fac=Faculty(name,fac_id)
        l2.append(fac)
        with open("faculty_record.pkl","wb") as f:
            pickle.dump(l2,f)    
    
    
    
import pickle
def check_faculty(fac_id):
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].fac_id==fac_id:
                    return True
                i+=1
            except (EOFError,IndexError):
                return False

import pickle
def print_frecord():
    with open("faculty_record.pkl","rb") as f:
            obj=pickle.load(f)
            i=0
            while True:
                try:
                    #display(obj[i])
                    print(f"Name:{obj[i].name}\nEmployee Id:{obj[i].fac_id}")
                    print(obj[i].book_issued)
                    i+=1
                except (EOFError,IndexError):
                    print("end")
                    break

from book import Book
import pickle
count_b=0
l3=[]
def add_book():
    global count_b
    title=input("Enter the Title:")
    author=input("Enter Author name:")
    isbn=input("Enter the ISBN number:")
    while True:
        if len(isbn)!=13:
            print("Invalid ISBN!!")
            isbn=input()
        else:
            break
    no_copies=int(input())
    
    
    if count_b==0: 
        b=Book(title,author,isbn,no_copies)
        l3.append(b)
        with open("book_record.pkl","wb") as f:
            pickle.dump(l3,f)
            count_b+=1
    elif check_book(isbn):
        a=check_book(isbn)
        with open("book_record.pkl","rb") as f:
            obj=pickle.load(f)
        with open("book_record.pkl","wb") as f:
            obj[a].no_copies+=no_copies
            
            pickle.dump(obj,f)

    else:
        b=Book(title,author,isbn,no_copies)
        l3.append(b)
        with open("book_record.pkl","wb") as f:
            pickle.dump(l3,f) 
            count_b+=1
        
def check_book(isbn):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    return i
                i+=1
            except :
                return False
    
import pickle
def print_brecord():
    with open("book_record.pkl","rb") as f:
            obj=pickle.load(f)
            i=0
            while True:
                try:
                    #display(obj[i])title,author,isbn,no_copies
                    print(f"Name:{obj[i].title}\nAuthor:{obj[i].author}\nISBN:{obj[i].isbn}\nNumber of Copies:{obj[i].no_copies}")
                    i+=1
                except (EOFError,IndexError):
                    print("end")
                    break


def issue_fac():
    fac_id=input("Enter the id:")
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                
                if obj[i].fac_id==fac_id:
                        isbn=input("Enter ISBN No.:")
                        no_co=input("Enter the number of copies:")
                        #a=check_avail_book(isbn,no_co)
                        if check_avail_book(isbn,no_co):
                            modify_fac(i,isbn,no_co)
                            modify_book_issue(isbn,no_co) 
                            print(f'Book with {isbn} isbn has been issued to employee with eid :{fac_id}')
                            break
                        else:
                            print(f'Book with {isbn} is not available/Copies Exhausted. Cannot issue book!!') 
                            break
                    
                i+=1
            except :
                print(f'Employee with {fac_id} not present. Cannot issue book!!!')
                break

def modify_book_issue(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    obj[i].no_copies-=int(copies)
                    with open("book_record.pkl","wb") as f:
                        pickle.dump(obj,f)
                    break
                i+=1
            except :
                pass#break
       
                            
                            
                        
def modify_fac(i,isbn,no_co):
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        obj[i].book_issued[isbn]=int(no_co)
        
        with open("faculty_record.pkl","wb") as f:
            pickle.dump(obj,f)
                
def check_avail_book(isbn,no_co):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if int(obj[i].isbn)==int(isbn)and int(obj[i].no_copies)>=int(no_co): 
                    return True#i
                i+=1
            except (EOFError,IndexError):
                return False
    
    
def issue_book_faculty():
    fac_id=input("Enter the id:")
    if check_faculty(fac_id):
        isbn=input("Enter the ISBN:")
        copies=int(input("Enter the number of copies:"))
        if check_avail_book(isbn,copies):
            with open("faculty_record.pkl","rb") as f:
                obj=pickle.load(f)
                i=0
                while True:
                    try:
                        if obj[i].eid==fac_id:
                            modify_fac(i,isbn,copies)
                            modify_book_issue(isbn,copies) 
                            print("Book Issued")
                            break
                        i+=1
                    except:
                        break
        else:
            print("Book does not found in the record")
    else:
        print("Faculty does not exist!!")

def modify_book_issue(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    with open("book_record.pkl","wb") as f:
                        obj[i].copies-=copies
                        pickle.dump(obj,f)
                    break
                i+=1
            except :
                pass

def modify_fac(i,isbn,copies):
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        if isbn in obj[i].fac_dict:
            with open("faculty_record.pkl","wb") as f:
                obj[i].fac_dict[isbn]+=copies
                pickle.dump(obj,f)
        else:
            with open("faculty_record.pkl","wb") as f:
                obj[i].fac_dict[isbn]=copies 
                pickle.dump(obj,f)
            
                
def check_avail_book(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn and obj[i].copies>=copies: 
                    return True
                i+=1
            except:
                return False

def return_fac():
    fac_id=input("Enter the Employee id:")
    if check_faculty(fac_id):
        isbn=input("Enter isbn:")
        if already_have_fac(isbn,fac_id):
            co=int(input("Enter the no. of copies you want to return"))
            modify_fac_return(fac_id,isbn,co)
            modify_book_return(isbn,co)
        else:
            print("Book with this isbn is not issued to this faculty")
    else:
        print("Faculty not found")
    

def modify_fac_return(fac_id,isbn,co):
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].fac_id==fac_id:
                    if obj[i].book_issued[isbn]==co:
                        del obj[i].book_issued[isbn]
                    elif co<obj[i].book_issued[isbn]:
                        obj[i].book_issued[isbn]-=co
                    with open("faculty_record.pkl","wb") as f:
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                break
def modify_book_return(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==str(isbn):
                    print(copies)
                    obj[i].no_copies+=int(copies)
                    with open("book_record.pkl","wb") as f:
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                break

def already_have_fac(isbn,fac_id):
    with open("faculty_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].fac_id==fac_id:
                    if isbn in obj[i].book_issued:
                        return True
                i+=1
            except (EOFError,IndexError):
                return False
            
#from datetime import date
import datetime
def issue_book_student():
    rollno=input("Enter the roll number:")
    if check_student(rollno):
        print("kj")
        if check_std_limit(rollno):
            isbn=input("Enter the isbn number of the book to be issued:")
            if not availability_of_book(isbn):
                print("Either book is not present or all copies are issued to others")
            elif already_have(isbn,rollno):
                print("This student already has the one copy of this book")
            else:
                l=datetime.date.today()
                modify_student_issue(rollno,isbn,l)
                modify_book_issue(isbn,1)
        else:
            print("Student has reached the book limit.Cannot issue the book")
    else:
        print("Student not found!! Cannot issue book")
def modify_student_issue(rollno,isbn,l):
    with open("student_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].r_no==rollno:
                    obj[i].book_issued[isbn]=l
                    with open("student_record.pkl","wb") as f:
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                break
def modify_book_issue(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    obj[i].no_copies-=copies
                    with open("book_record.pkl","wb") as f:
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                break

def check_std_limit(rollno):
    with open("student_record.pkl","rb") as f:
        l=pickle.load(f)
        i=0
        flag=False
        while True:
            try:
                if l[i].r_no==rollno and l[i].num_books_issued<5:
                    return True
                i+=1
            except:
                return False
            
def availability_of_book(isbn):
    with open("book_record.pkl","rb") as f:
        l=pickle.load(f)
        i=0
        flag=True
        while True:
            try:
                if l[i].isbn==isbn and l[i].no_copies>0:
                    break
                i+=1
            except:
                flag=False
    return flag  
def already_have(isbn,rollno):
    with open("student_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].r_no==rollno:
                    if isbn in obj[i].book_issued:
                        return True
                i+=1
            except:
                return False

def return_book_student():
    rollno=input("Enter the rollno of the student:")
    if check_student(rollno):
        isbn=input("Enter isbn:")
        if already_have(isbn,rollno):
            modify_student_return(rollno,isbn)
            modify_book_return(isbn,1)
        else:
            print("Book with this isbn is not issued to this student")
    else:
        print("Student not found")
    

def modify_student_return(rollno,isbn):
    with open("student_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].r_no==rollno:
                    with open("student_record.pkl","wb") as f:
                        del obj[i].book_issued[isbn]
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                break
def modify_book_return(isbn,copies):
    with open("book_record.pkl","rb") as f:
        obj=pickle.load(f)
        i=0
        while True:
            try:
                if obj[i].isbn==isbn:
                    with open("book_record.pkl","wb") as f:
                        obj[i].no_copies+=1
                        pickle.dump(obj,f)
                    break
                i+=1
            except:
                pass
    
   
    
    