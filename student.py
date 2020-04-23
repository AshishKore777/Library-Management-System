class Student:
    def __init__(self,name,add_year,branch,ad_id_no,r_no):
        self.name=name
        self.add_year=add_year
        self.branch=branch
        self.ad_id_no=ad_id_no
        self.r_no=r_no
        self.num_books_issued=0
        self.book_issued={}
        
        