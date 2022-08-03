
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ''
        total = 0

        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']

        output = title + items + 'Total: ' + str(total)
        return output

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def deposit(self, amount, descr = ""):
        self.ledger.append({"amount": amount, "description": descr})

    def withdraw(self, amount, descr = ""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": descr}) 
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i['amount']

        return total
         
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

# def create_spend_chart(categories):
