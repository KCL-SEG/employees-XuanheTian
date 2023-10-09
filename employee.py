"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:

    def __init__(self, name, payment_method, commission_type = None):
        self.name = name
        self.payment_method = payment_method
        self.commission_type = commission_type
    def get_pay(self):
        base_payment = self.payment_method.get_pay()
        commission = 0
        if self.commission_type:
            commission = self.commission_type.get_commssion()
        return base_payment + commission

    
    def __str__(self):
        return (f"{self.name} works on a {self.payment_method } of {self.base_payment}. Their total pay is {self.get_pay()}.")


class salary_pay :
    def __init__ (self, monthly_salary):
        self.monthly_salary = monthly_salary
    def get_pay(self):
        return self.monthly_salary


class Hourly_pay :
    def __init__ (self, hourly_wage , worked_hours):
        self.hourly_wage = hourly_wage
        self.worked_hours = worked_hours
    def get_pay(self):
        return self.hourly_wage * worked_hours

class bonus_commission:
    def __init__(self, fixed_bonus):
        self.fixed_bonus = fixed_bonus
    def get_commssion(self):
        return self.fixed_bonus

class contract_commission:
    def __init__(self, number_of_contract, contract_per_commission ):
        self.number_of_contract = number_of_contract
        self.contract_per_commission = contract_per_commission
    def get_commssion(self):
        return self.number_of_contract * contract_per_commission
    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryPay(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
