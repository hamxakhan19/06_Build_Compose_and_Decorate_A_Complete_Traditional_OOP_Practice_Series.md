class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example
print(Bank.bank_name)
Bank.change_bank_name("XYZ Bank")
print(Bank.bank_name)
