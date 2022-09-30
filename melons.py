"""Classes for melon orders."""
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
        

    def get_total(self):
        """Calculate price, including tax."""

        # christmas melons is in species as an attribute
        base_price = 5
        
        #if christmas_melon

        if self.species == "Christmas melons":
            base_price = base_price * 1.5

        #then bas_price = 5(1.5)
        total = (1 + self.tax) * self.qty * base_price
        #add on flat fee after total

        # 1 + 0.17
        if self.order_type == "international" and self.qty < 10:
            total = total + 3
        
        
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

class GovermentMelonOrder(AbstractMelonOrder):
    
    passed_inspection = False

    def __init__(self, passed, species, qty, country_code, shipped):
        self.passed = passed
        super().__init__(species, qty, country_code, shipped)

    def marked_inspection(self, passed):
        if self.passed_inspection != passed:
            passed_inspection = True
            return passed_inspection

# is_passed = GovermentMelonOrder(passed)
