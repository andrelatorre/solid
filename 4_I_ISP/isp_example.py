from abc import ABC, abstractmethod
 
#Generic
class Documents(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def calculate(self): pass

#ISP
class DocumentPDF:
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass    

class DocumentTXT:    
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def format(self): pass

class DocumentEXCEL:    
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass

class PDF(Documents):
    def load(self) :
        print("load in pdf")
    
    def view(self) :
        print("view informations")