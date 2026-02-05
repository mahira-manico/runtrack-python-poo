class Book:
    
    def __init__(self,title,author,page_number):
        self.__title=title #Store book title
        self.__author=author #Store author name
        self.__page_number=page_number #Store page count
    
    #Initializing of getters and setters
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
       #Verify if new page number is a valid integer
       if not isinstance(new_page_number,int):
          print("error, integer numbers only!")
       elif new_page_number<0:
          print("error! must be a positive number!")
       else:
          self.__page_number=new_page_number