"""Classes for melon orders."""

import random

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    order_type = None
    tax = 0

    def __init__(self, species, qty, country_code, shipped):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
    
    def get_base_price(self, random_num):

        random_num = random.randint(5, 9) # base price
        random_base_price = random_num
        
        # if it is not the rush hour, then we don't add the 4 dollars
        # but if it's from 8-11 am, M-F, we add an extra $4- when call = int(), 
        #parameter (24_hour_day, day_of_week)


    def get_total(self):
        """Calculate price, including tax."""

        # christmas melons is in species as an attribute

        # print_this = get_base_price(self)
        # base_price = 5
        base_price = self.get_base_price()  

        #if christmas_melon

        if self.species == "Christmas melons":
            base_price = base_price * 1.5

        #then bas_price = 5(1.5)
        total = (1 + self.tax) * self.qty * base_price
        #add on flat fee after total

        # 1 + 0.17
        if self.order_type == "international" and self.qty < 10:
            total = total + 3
        
        # https://www.codespeedy.com/how-to-call-method-of-another-class-in-python/
        # AbstractMelonOrder.get_base_price(self)
        # self.get_base_price(self)
        # https://devnote.in/how-to-call-one-method-from-another-within-the-same-class-in-python/
        
        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
 

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    # def __init__(self, species, qty):
    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty, shipped):
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        
        super().__init__(species, qty, 'USA', shipped)

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
 
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code, shipped):
        """Initialize melon order attributes."""
        # self.order_type = "international"
        # self.tax = 0.17
        super().__init__(species, qty, country_code, shipped)

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    
    #passed_inspection = False

    def __init__(self, species, qty, country_code, shipped):
        self.passed_inspection = False
        super().__init__(species, qty, country_code, shipped)

    def marked_inspection(self, passed):
        if self.passed_inspection != passed:
            self.passed_inspection = True
        return self.passed_inspection

# is_passed = GovermentMelonOrder(passed)
# order1 = DomesticMelonOrder("cantaloupe", 8)
# >>> order1.get_total()
