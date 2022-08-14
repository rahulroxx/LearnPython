# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from abc import abstractmethod

class Print:
    @abstractmethod
    def print_itself(self):
        ''' this method prints '''
        pass

class PrintInvoice(Print):
    def print_itself(self):
        ''' this function prints the invoice '''
        print("print invoice only")

class Save:
    @abstractmethod
    def save(self):
        ''' this method saves '''
        pass

class SaveToFile(Save):
    def save(self):
        print('saving to file')

class Drive:
    @abstractmethod
    def upload(self):
        pass
    
class SaveToGoogle(Drive):
    def upload(self):
        ''' this function uploads to drive '''
        print('Save to google drive')

class SaveToOneDrive(Drive):
    def upload(self):
        ''' this function uploads to microsoft one drive'''
        print('Save to microsoft onedrive ')
        
class Book:
    def __init__(self, price: float):
        self.price = price

class Invoice:
    def __init__(self, book: Book, quantity: int, discount_rate: float, tax_rate: float, save_to_file: Save, save_to_google: Drive,  print_it: Print):
        self.book = book
        self.quantity = quantity
        self.discount_rate = discount_rate
        self.tax_rate = tax_rate
        self.print_it = print_it
        self.save_to_file = save_to_file
        self.save_to_google = save_to_google
        self.print_it = print_it
        
    def calculate_total(self, final_prices: float = 100.0):
        return final_prices
    
    def save_file(self):
        return self.save_to_file.save()
    
    def print_invoice(self):
        return self.print_it.print_itself()


b = Book(500)
save_to_file = SaveToFile()
save_to_google = SaveToGoogle()
save_to_onedrive = SaveToOneDrive()
print_invoice = PrintInvoice()
i = Invoice(b, 2, 0.10, 33.33, save_to_file, save_to_google, print_invoice)
i.save_file() 
i.print_invoice()
