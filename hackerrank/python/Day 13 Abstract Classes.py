# Task
# Given a Book class and a Solution class, write a MyBook class that does the following:

# Inherits from Book
# Has a parameterized constructor taking these 3 parameters:
# string TITLE 
# string AUTHOR
# int PRICE
# Implements the Book class' abstract display() method so it prints these 3 lines:
# TITLE:, a space, and then the current instance's TITLE.
# AUTHOR:, a space, and then the current instance's AUTHOR.
# PRICE, a space, and then the current instance's PRICE.
# Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.: public) when declaring MyBook or your code will not execute.


from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    
    @abstractmethod
    def display(self): 
        pass

class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price       
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
        
    
#Write MyBook class

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()