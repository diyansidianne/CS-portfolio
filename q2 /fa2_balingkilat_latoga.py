
class Patient:
    name = ""
    bill_amount = float(0)
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount
    def set_name(self, name):
        self._name = name
    def get_name(self):
        return f"Patient Name: {self._name}"
    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount
    def get_bill_amount(self):
        return f"Original Bill: ₱{self._bill_amount:,.2f}"
    def calculate_bill(self):
        return f"Final Bill: ₱{self._bill_amount:,.2f}"
class SeniorPatient(Patient):
    def calculate_bill(self):
        final_amount = self._bill_amount - (0.20 * self._bill_amount)
        return f"Final Bill: ₱{final_amount:,.2f}"

class PhilHealthPatient(Patient):
    def calculate_bill(self):
        final_amount = self._bill_amount - (0.15 * self._bill_amount)
        return f"Final Bill: ₱{final_amount:,.2f}"

p1 = Patient("Ismer Inghoi", 15000)
p2 = SeniorPatient("Liz Anya", 15000)
p3 = PhilHealthPatient("Princess Meiko", 15000)

print("Hospital Billing System")
print("-----------------------")
print(p1.get_name())
print(p1.get_bill_amount())
print(p1.calculate_bill())
print()
print(p2.get_name())
print(p2.get_bill_amount())
print(p2.calculate_bill())
print()
print(p3.get_name())
print(p3.get_bill_amount())
print(p3.calculate_bill())
