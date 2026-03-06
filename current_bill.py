"""
Program to calculate electricity/current bill
Includes tiered pricing, taxes, and charges
"""


class BillCalculator:
    """Class to handle electricity bill calculations"""
    
    def __init__(self, customer_name, meter_number):
        """Initialize bill calculator with customer details"""
        self.customer_name = customer_name
        self.meter_number = meter_number
        self.units_consumed = 0
        self.bill_amount = 0
        self.tax_percentage = 5  # 5% tax
        self.fixed_charge = 50   # Fixed monthly charge
    
    def set_tiered_rates(self):
        """Define tiered pricing rates per unit"""
        self.rates = {
            "0-50": 5.0,      # ₹5 per unit for first 50 units
            "51-100": 7.0,    # ₹7 per unit for 51-100 units
            "101-200": 9.0,   # ₹9 per unit for 101-200 units
            "200+": 11.0      # ₹11 per unit for 200+ units
        }
    
    def calculate_tiered_cost(self, units):
        """Calculate cost based on tiered pricing"""
        cost = 0
        
        if units <= 50:
            cost = units * self.rates["0-50"]
        elif units <= 100:
            cost = (50 * self.rates["0-50"]) + ((units - 50) * self.rates["51-100"])
        elif units <= 200:
            cost = (50 * self.rates["0-50"]) + (50 * self.rates["51-100"]) + \
                   ((units - 100) * self.rates["101-200"])
        else:
            cost = (50 * self.rates["0-50"]) + (50 * self.rates["51-100"]) + \
                   (100 * self.rates["101-200"]) + ((units - 200) * self.rates["200+"])
        
        return cost
    
    def calculate_bill(self, units):
        """Calculate total bill amount"""
        self.units_consumed = units
        self.set_tiered_rates()
        
        # Calculate cost based on units consumed
        unit_cost = self.calculate_tiered_cost(units)
        
        # Add fixed charge
        total_before_tax = unit_cost + self.fixed_charge
        
        # Calculate tax
        tax = (total_before_tax * self.tax_percentage) / 100
        
        # Final bill amount
        self.bill_amount = total_before_tax + tax
        
        return self.bill_amount
    
    def get_bill_breakdown(self, units):
        """Get detailed bill breakdown"""
        self.calculate_bill(units)
        self.set_tiered_rates()
        
        unit_cost = self.calculate_tiered_cost(units)
        total_before_tax = unit_cost + self.fixed_charge
        tax = (total_before_tax * self.tax_percentage) / 100
        
        breakdown = {
            "customer_name": self.customer_name,
            "meter_number": self.meter_number,
            "units_consumed": units,
            "unit_cost": unit_cost,
            "fixed_charge": self.fixed_charge,
            "subtotal": total_before_tax,
            "tax": tax,
            "total_bill": self.bill_amount
        }
        
        return breakdown
    
    def display_bill(self, units):
        """Display formatted bill"""
        breakdown = self.get_bill_breakdown(units)
        
        print("\n" + "="*50)
        print("           ELECTRICITY BILL")
        print("="*50)
        print(f"Customer Name    : {breakdown['customer_name']}")
        print(f"Meter Number     : {breakdown['meter_number']}")
        print(f"Units Consumed   : {breakdown['units_consumed']} kWh")
        print("-"*50)
        print(f"Unit Cost        : ₹{breakdown['unit_cost']:.2f}")
        print(f"Fixed Charge     : ₹{breakdown['fixed_charge']:.2f}")
        print(f"Subtotal         : ₹{breakdown['subtotal']:.2f}")
        print(f"Tax (5%)         : ₹{breakdown['tax']:.2f}")
        print("-"*50)
        print(f"TOTAL BILL       : ₹{breakdown['total_bill']:.2f}")
        print("="*50 + "\n")
    
    def calculate_multiple_bills(self, customers):
        """Calculate bills for multiple customers"""
        total_revenue = 0
        bills = []
        
        for customer_data in customers:
            name = customer_data['name']
            meter = customer_data['meter']
            units = customer_data['units']
            
            calculator = BillCalculator(name, meter)
            bill = calculator.calculate_bill(units)
            bills.append(calculator.get_bill_breakdown(units))
            total_revenue += bill
        
        return bills, total_revenue


# Example usage
if __name__ == "__main__":
    # Single customer bill
    print("--- SINGLE CUSTOMER BILL ---")
    calculator = BillCalculator("Raghu Vardhan", "MET001")
    calculator.display_bill(150)
    
    # Multiple customers
    print("\n--- MULTIPLE CUSTOMERS BILLS ---")
    customers = [
        {"name": "Raghu Vardhan", "meter": "MET001", "units": 120},
        {"name": "Suresh Kumar", "meter": "MET002", "units": 85},
        {"name": "Priya Sharma", "meter": "MET003", "units": 250}
    ]
    
    multi_calc = BillCalculator("Admin", "ADM001")
    bills, total_revenue = multi_calc.calculate_multiple_bills(customers)
    
    print("\nBill Details:")
    for bill in bills:
        print(f"\n{bill['customer_name']} (Meter: {bill['meter_number']})")
        print(f"  Units: {bill['units_consumed']} | Unit Cost: ₹{bill['unit_cost']:.2f} | Total: ₹{bill['total_bill']:.2f}")
    
    print(f"\nTotal Revenue: ₹{total_revenue:.2f}")
