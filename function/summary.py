class Summary():
    def __init__(self,months_transacctions, balance, credit, debit):
        self.months_transacctions = months_transacctions
        self.balance = balance
        self.credit = credit
        self.debit = debit

    def credit_average(self):
        return self.average(self.credit)
    
    def debit_average(self):
        return self.average(self.debit)

    def average(self,lst):
        return round(sum(lst) / len(lst),2)
