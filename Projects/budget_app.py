import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        self.ledger.append({'amount': -amount, 'description': description})
        return self.check_funds(amount)

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return self.check_funds(amount)

    def check_funds(self, amount):
        return (self.get_balance() - amount) >= 0

    def __str__(self):
        title = self.name.center(30, "*")
        final = [title]

        for item in self.ledger:
            desc = item['description'][:23]
            amount = f"{item['amount']:.2f}"[:7]

            line = f"{desc:<23}{amount:>7}"
            final.append(line)

        final.append(f"Total: {self.get_balance():.2f}")

        return "\n".join(final)


def create_spend_chart(categories):
    categories_percentages = []
    total_withdrawals = sum(
        -item["amount"]
        for category in categories
        for item in category.ledger
        if item["amount"] < 0
    )
    if total_withdrawals == 0:
        total_withdrawals = 1

    for category in categories:
        spendings = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        percentage = math.floor(spendings * 100 / total_withdrawals)

        categories_percentages.append({'category': category, 'percentage': percentage})

    graph = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        graph += f"{i:>3}|"
        for category in categories_percentages:
            if category['percentage'] >= i:
                graph += ' o '
            else:
                graph += '   '
        graph += ' \n'

    graph += ("    " + "-" * (len(categories) * 3 + 1))

    max_length_name = max(len(category.name) for category in categories)

    for i in range(max_length_name):
        graph += "\n     "
        for category in categories:
            if len(category.name) >= i + 1:
                graph += f"{category.name[i]}  "
            else:
                graph += "   "

    return graph
