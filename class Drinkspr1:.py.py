class Drink:
# class variables stored (flavors and bases)
    _valid_bases = {"water","milk","Thai tea", "green tea", "coffee", "mineral water",}
    _valid_flavors = {"leche cubes", "vanilla", "coconut", "cocoa", "lemon", "lime",}
    
    
#base prices 
    _size_costs = {
        
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "extra large": 2.15,
        
    }
    
    def _inti_(self, size):
        self._base = None
        self._flavors = set()
        self._size = None
        self._cost = 0.00
        self._set_size(size)
        
#each flavor price addition $0.15
#wondering if having all flavors set at .15 is necessary or having it set to all the same?
#wondering if flavor prices is not necessary to list or if listed needs a def inti method code?
    _flavor_prices = {
        "leche cubes": 0.15,
        "vanilla": 0.15,
        "coconut": 0.15,
        "cocoa": 0.15,
        "lemon": 0.15,
        "lime": 0.15,
    }
    
    def __init__(self, size):
        
##not sure if what is not in color the right callout method(might reveal error going forward)   
     def __init__(self, base):
        if base not in self._valid_bases:
            raise ValueError(f"Invalid base: {base}, Valid bases are: {self._valid_bases}")
        self._base = base
        self._flavors = set()
        
#getters for bases and flavors
    def get_base(self):
        return self._base
    
    def get_flavors(self):
        return list(self._flavors)
    
    def get_num_flavors(self):
        return len(self._flavors)
    
    def get_total( self):
        return self._cost
    
#setters for base    
    def set_base(self,base):
        if base in self._vaild_bases:
            self._base = base
        else:
            raise ValueError(f"Invalid base: {base}")
        
#add valid flavors
    def add_flavor(self,flavor):
        if flavor in self._valid_flavors:
            if flavor not in self._flavors:
                self._cost += 0.15
            self._flavors.add(flavor)
        else:
            raise ValueError(f"Invalid flavor: {flavor}. Valid flavors are: {self._valid_flavors}"
            )
    #adding flavor total to tax rate added to order       
    def set_flavors(self, flavors):
        if all(flavor in self._valid_flavors for flavor in flavors):
           new_flavors = set(flavors) - self._flavors
           self._cost += 0.15 * len(new_flavors)
           self._flavors = set(flavors)
        else:
            invalid_flavors = [flavor for flavor in flavors if flavor not in self._valid_flavors]
            raise ValueError(f"Invalid flavor: {flavors}. choose different flavor from{self._valid_flavors}")
                
#accessor  
    def set_size(self, size):
        size = size.lower()
        if size in self._size_costs:
            self._size = size
#Tax rate added to order
            self._cost = self._size_costs[size] + 0.15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid flavors: {size}, choose different flavor from: {list(self._size_costs.keys())}.")
    
    def _str__(self):
        return f"Drink(base={self._base}, flavors={self._flavors})"
    
    
class Order:
#tax rate
    _tax_rate = 0.0725
    
    def _init__(self):
        self._items = []
        
#getters for order
    def get_items(self):
        return self._items
    
    def get_total(self):
        return len(self._items)
       
       
    def get_num_items(self):
        return len(self._items)
    
#accessors
    def get_total(self):
       return sum(drink.get_total() for drink in self._items)
   
    def get_tax(self):
       return self.get_total() * (1 + self._tax_rate)

#not getting the code to print the receipt without print statement
#def receipt might need to be changed to run the code
#order receipt 
    def get_receipt(self):
        receipt_data = {
            "number_drinks": self.get_num_items(),
            "drinks": [],
            "subtotal": self.get_total(),
            "tax":self.get_total() * self._tax_rate,
            "grand total": self.get_total()
        }
        for i, drink in enumerate(self._items):
            base = drink.get_base()
            flavors = ",".join(drink.get_flavors())
            receipt += f"{i + 1}. Base - {base}, Flavors - {flavors}\n"
        return receipt
     
#def adding and removing items to the order
    def add_item(self, drink):
            if isinstance(drink, Drink):
                self._items.append(drink)
            else:
                raise TypeError("Item can only be a drinks")
        
        
    def remove_item(self, index):
            if 0 <= index < len(self._items):
             self._items.pop(index)
            else:
               raise IndexError("Invalid")
            
    
        