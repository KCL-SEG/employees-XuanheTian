class Employee:

    def __init__(self, name, payment_method, commission_type=None):
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
        base_desc = f"{self.name} works on {self.payment_method.description()}"

        if self.commission_type:
            base_desc += f" and {self.commission_type.description()}"
        
        base_desc += f". Their total pay is {self.get_pay()}."
        return base_desc

class SalaryPay:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary
    
    def description(self):
        return f"a monthly salary of {self.monthly_salary}"


class HourlyPay:
    def __init__(self, hourly_wage, worked_hours):
        self.hourly_wage = hourly_wage
        self.worked_hours = worked_hours

    def get_pay(self):
        return self.hourly_wage * self.worked_hours
    
    def description(self):
        return f"a contract of {self.worked_hours} hours at {self.hourly_wage}/hour"


class BonusCommission:
    def __init__(self, fixed_bonus):
        self.fixed_bonus = fixed_bonus

    def get_commssion(self):
        return self.fixed_bonus
    
    def description(self):
        return f"receives a bonus commission of {self.fixed_bonus}"


class ContractCommission:
    def __init__(self, number_of_contract, contract_per_commission):
        self.number_of_contract = number_of_contract
        self.contract_per_commission = contract_per_commission

    def get_commssion(self):
        return self.number_of_contract * self.contract_per_commission
    
    def description(self):
        return f"receives a commission for {self.number_of_contract} contract(s) at {self.contract_per_commission}/contract"


billie = Employee('Billie', SalaryPay(4000))
charlie = Employee('Charlie', HourlyPay(25, 100))
renee = Employee('Renee', SalaryPay(3000), ContractCommission(4, 200))
jan = Employee('Jan', HourlyPay(25, 150), ContractCommission(3, 220))
robbie = Employee('Robbie', SalaryPay(2000), BonusCommission(1500))
ariel = Employee('Ariel', HourlyPay(30, 120), BonusCommission(600))