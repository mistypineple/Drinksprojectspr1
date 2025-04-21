class Drink:
    # class variables stored (flavors and bases)
    _vaild_bases = {"water","milk","Thai tea", "green tea", "coffee", "mineral water",}
    _valid_flavors = {"leche cubes", "vanilla", "coconut", "cocoa", "lemon", "lime",}
    
    def __init__(self, base):
        if base not in self.valid_bases:
            raise ValueError(f"Invalid base: {base}, Valid bases are: {self.valid_bases}")
        self._base = base
        self._flavors = set()
        
    def get_base(self):
        return self._base
    
    def get_flavors(self):
        return self._flavors
    
    def get_num_flavors(self):
        return len(self._flavors)
    
    def set_base(self,base):
        if base in self._vaild_bases:
            self._base = base
        else:
            raise ValueError(f"Invalid base: {base}")
    
    def add_flavor(self,flavor):
        if flavor in self._valid_flavors:
           print(f"Flavor {flavor} already added")
        elif flavor not in self._valid_flavors:
            print (f"Invaild flavor: {flavor}. Valid flavors are: {self.valid_flavors}")
        else:
            self._flavors.append(flavor)
            
    def set_flavors(self, flavors):
        for flavor in flavors:
            if flavor not in self._valid_flavors:
                raise ValueError(f"Invalid flavor: {flavor}") 
        self._flavors = set(flavors)
        
    def _str__(self):
        return f"Drink(base={self._base}, flavors={self._flavors})"
    
    
    
class Order:
    def _init__(self):
        self._items = []
        
    def get_items(self):
        return self._items
    
    def get_total(self):
        return len(self._items)
    
    def get_receipt(self):
        for i, drink in enumerate(self._items):
            base = drink.get_base()
            flavors = ",".join(drink.get_flavors())
            receipt += f"{i + 1}: base - {base}, Flavors - {flavors}\n"
        return receipt
    
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
            
    
        