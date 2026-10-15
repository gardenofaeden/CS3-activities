class Publication:
    def __init__(title,author):
        self.title = title
        self.author = author
        
    def get_title():
        
        
    def get_author():
    def set_title(title):
    def set_author(author):
    def display_info():

class Book:
    def __init__(title,author,number_pages):
        self.title = title
        self.author = author
        self.number_pages = number_pages
        
    def get_number_of_pages(self):
    def set_number_of_pages(self,value):
        if value > 0:
            self.number_pages = value
        else:
            print("The number of pages must be positive")


    

class Magazine:
    def __init__(title,author,issue_number):
        self.title = title
        self.author = author
        self.issue_number = issue_number
    def get_issue_number(self):
        
    def set_issue_number(self,value):
        if value > 0:
            self.issue_number = issue_number
        else:
            print("The number of pages must be positive")

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1,get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
