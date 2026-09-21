class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True

        return False

    def get_balance(self):
        total = 0

        for transaction in self.ledger:
            total += transaction['amount']

        return total

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, another):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {another.name}')
            another.deposit(amount, f'Transfer from {self.name}')
            return True

        return False

    def __str__(self):
        output = f'{self.name:*^30}\n'

        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = f"{transaction['amount']:.2f}"

            output += f'{description:<23}{amount:>7}\n'

        output += f'Total: {self.get_balance():.2f}'

        return output




def create_spend_chart(categories):
    # Find total spending across all categories
    total_spending = 0

    for category in categories:
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total_spending += -transaction['amount']

    # Calculate spending percentage for each category
    percentages = []

    for category in categories:
        category_spending = 0

        for transaction in category.ledger:
            if transaction['amount'] < 0:
                category_spending += -transaction['amount']

        percentage = int((category_spending / total_spending) * 100)
        percentage = (percentage // 10) * 10

        percentages.append(percentage)

    # Chart title
    output = "Percentage spent by category\n"

    # Bars: 100 down to 0
    for level in range(100, -1, -10):
        output += f"{level:>3}| "

        for percentage in percentages:
            if percentage >= level:
                output += "o  "
            else:
                output += "   "

        output += "\n"

    # Horizontal line
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        output += "     "

        for category in categories:
            if i < len(category.name):
                output += category.name[i]
            else:
                output += " "

            output += "  "

        if i < max_length - 1:
            output += "\n"

    return output


# Testing the Code
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant")

clothing = Category("Clothing")
clothing.deposit(500, "salary")
food.transfer(50, clothing)

print(food)
print()
print(clothing)
print()

print(create_spend_chart([food, clothing]))