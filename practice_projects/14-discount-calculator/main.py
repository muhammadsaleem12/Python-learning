from abc import ABC, abstractmethod


# Represents a product with a name and price
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'


# Abstract base class for all discount strategies
class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass


# Applies a percentage-based discount
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)


# Applies a fixed amount discount
class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount


# Applies a special discount to premium users
class PremiumUserDiscount(DiscountStrategy):
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8


# Calculates the lowest available price from all applicable strategies
class DiscountEngine:
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)


# Creates the product, discount strategies, and calculates the best price
if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'
    
    product2 = Product('Mechanical Keyboard', 120.0)
    user_tier2 = 'Normal'

    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)
    best_price2 = engine.calculate_best_price(product2, user_tier)

    print(f'Best price for {product.name} for {user_tier} user: ${best_price:.2f}')
    print(f'Best price for {product2.name} for {user_tier2} user: ${best_price2:.2f}')