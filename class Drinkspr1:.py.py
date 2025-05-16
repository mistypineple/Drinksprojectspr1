

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
        self._base = None
        self._flavors = set()
        self._size = None
        self._cost = 0.00
        self.set_size(size)

    def set_base(self, base):
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
        if base in self._valid_bases:
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
            raise ValueError(f"Invalid flavor: {flavors}. Choose a different flavor from {self._valid_flavors}")
                
#accessor  
    def set_size(self, size):
        size = size.lower()
        if size in self._size_costs:
            self._size = size
#Tax rate added to order
            self._cost = self._size_costs[size] + 0.15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid flavors: {size}, choose different flavor from: {list(self._size_costs.keys())}.")
    
    def __str__(self):
        base = self.get_base() or "None"
        flavors = ", ".join(self.get_flavors()) or "None"
        size = self._size or "Unknown"
        cost = self.get_total()
        return f"Drink: Size - {size}, Base - {base}, Flavors - {flavors}, Cost: ${cost:.2f}"

#hungry-hungry-students
class Food:
#defining food and toppings
    _food_price = {
        "eggroll": 2.30,
        "ice cream": 2.00,
        "french fries":3.00,
        "onion rings": 1.75,
        "potato chips": 1.50,
        "chicken nuggets": 1.70,
        "chicken nachos": 1.90,
    }
    
    _topping_prices = {
        "salsa": 0.00,
        "guacamole": 0.30,
        "sour cream": 0.50,
        "cheese": 0.50,
        "ketchup": 0.00,
        "cherry": 0.00,
        "chocolate sauce": 0.00,
        "chili": 0.10,
        "mustard": 0.00,
        
    }
#initializing food type to price
    def __init__(self, food_type):
        if food_type.lower() not in self._food_price:
           raise ValueError(f" Invalid food type.")
        self.type = food_type.lower()
        self._base_price = self._food_price[self.type]
        self._toppings = set()
        
#accessor for the base price 
    def get_base_prices(self):
        return self._base_price
    
#accessor for food type       
    def get_type(self):
        return self.type
    
#add a topping
    def add_topping(self, topping):
        if str(topping).lower() not in self._topping_prices:
            raise ValueError(f" Invalid topping")
        self._toppings.add(topping.lower()) 
        
#acessor for toppings       
    def get_toppings(self):
        return list(self._toppings)
            
    def get_num_toppings(self):
        return len(self._toppings)
    
 #total add up for topping plus base total price   
    def get_total_price(self):
        toppings_cost = sum(self._topping_prices[topping] for topping in self._toppings)        
        return self._base_price + toppings_cost
            

class Order:
#tax rate
    _tax_rate = 0.0725
    
    def __init__(self):
        self._items = []
        
#getters for order
    def get_items(self):
        return self._items
    
       
    def get_total(self):
        return sum(
            item.get_total() if isinstance(item, Drink) else item.get_total_price() for item in self._items
        )
    
#accessors
    def get_total(self):
       return len(self.items)
   
    def get_tax(self):
       return self.get_total() * (1 + self._tax_rate)

#not getting the code to print the receipt without print statement
#def receipt might need to be changed to run the code
#order receipt 
#-HHS = receipt needs to be updated because of new food class aded to the order!
    def get_receipt(self):
        receipt = "Order Receipt:\n"
        total_cost = 0.0
        for i, item in enumerate(self._items):
            if isinstance(item, Drink):
                base = item.get_base()
                flavors = ", ".join(item.get_flavors())
                price = item.get_total()
                receipt += f"Drink {i + 1}: Base - {base}, Flavors - {flavors}, Price: ${price:.2f}\n"
                total_cost += price
            elif isinstance(item, Food):
                food_type = item.get_type()
                toppings = ", ".join(item.get_toppings()) or "None"
                price = item.get_total_price()
            elif isinstance(item, IceCream):
                flavor = item.get_flavor()
                toppings = ", ".join(item.get_toppings()) or "None"
                price = item.get_total_price()
                receipt += f"Ice Cream {i + 1}: Flavor - {flavor}, Toppings - {toppings}, Price: ${price:.2f}\n"
                total_cost += price
    
            return receipt
#adding icream to the order to be accessed 
    def add_item(self, item):
            if isinstance(item, (Drink, Food, IceCream)):
                self._items.append(item)
            else:
                raise TypeError("Item must be either a Drink, Food, or IceCream.")
        
        
    def remove_item(self, index):
            if 0 <= index < len(self._items):
             self._items.pop(index)
            else:
                raise IndexError("Invalid index. Cannot remove item.")
            
    
class IceCream:
# Ice Cream class with flavor and toppings
    valid_IceCream_flavors = {"vanilla", "chocolate", "Vanilla Bean", "Banana", "Butter PEecan", "S'mores"}
    valid_IceCream_toppings = {"Cherry", "Chocolate sauce", "Chocolate Sauce", "Storios", "Dig Dough", "T&T's", "cookie Dough", "Pecans",}
    
    valid_IceCream_flavors = {
        "mint chocolate chip": 4.00,
        "chocolate": 4.00,
        "vanilla bean": 3.00,
        "banana": 3.50,
        "butter pecan": 3.50,
        "s'mores": 4.00,
    }

    valid_IceCream_toppings = {
        "cherry": 0.00,
        "chocolate sauce": 0.50,
        "caramel sauce": 0.50,
        "storios": 1.00,
        "dig Dough": 1.00,
        "t&t's": 1.00,
        "cookie Dough": 1.00,
        "pecans": 0.50,
    }

    def __init__(self, flavor):
        # Initialize the ice cream with a flavor and an empty set of toppings
        if flavor.lower() not in self.valid_IceCream_flavors:
            raise ValueError(f"Invalid flavor: {flavor}. Valid flavors are: {list(self.valid_IceCream_flavors.keys())}")
        self._flavor = flavor.lower()
        self._toppings = set()

    # Getter for the flavor
    def get_flavor(self):
        return self._flavor

    # Getter for the toppings
    def get_toppings(self):
        return list(self._toppings)

    # Add a topping to the ice cream
    def add_topping(self, topping):
        if topping.lower() not in self.valid_IceCream_toppings:
            raise ValueError(f"Invalid topping: {topping}. Valid toppings are: {list(self.valid_IceCream_toppings.keys())}")
        self._toppings.add(topping.lower())

    # Calculate the total price of the ice cream
    def get_total_price(self):
        flavor_price = self.valid_IceCream_flavors[self._flavor]
        toppings_price = sum(self.valid_IceCream_toppings[topping] for topping in self._toppings)
        return flavor_price + toppings_price

    # String representation of the ice cream
    def __str__(self):
        toppings = ", ".join(self.get_toppings()) or "None"
        return f"Ice Cream: Flavor - {self.get_flavor()}, Toppings - {toppings}, Total Price: ${self.get_total_price():.2f}"