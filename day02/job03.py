class Book:
    def __init__(self,title,author,page_number):
        self.__title=title
        self.__author=author
        self.__page_number=page_number
        self.__available=True
    
    def get_title(self):
      return self.__title
   
    def set_title(self,new_title):
      self.__title=new_title

    def get_author(self):
       return self.__author

    def set_author(self,new_author):
       self.__author=new_author

    def get_page_number(self):
       return self.__page_number
       
    def set_page_number(self,new_page_number):
       if not isinstance(new_page_number,int):
          print("error, integer numbers only!")
       elif new_page_number<0:
          print("error! must be a positive number!")
       else:
          self.__page_number=new_page_number
    
    def get_available(self):
       return self.__available
    
    def set_available(self, new_available):
       self.__available=new_available

    def verification(self):
       if self.__available==True:
          return True
       return False
    
    def borrow(self):
       if self.verification():
        self.set_available(False)
       else:
          print("that book is already borrowed!")
    
    def returning(self):
       if not self.verification():
          self.set_available(True)
          
        
    
          

       
    

       

    