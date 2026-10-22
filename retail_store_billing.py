
class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = 0
        self.__quantity = 0

        self.set_price(price)
        self.set_quantity(quantity)

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    def set_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        self.__quantity = quantity

    def apply_discount(self):
        pass


class GroceryProduct(Product):
    def apply_discount(self):
        return 0.05  


class ElectronicsProduct(Product):
    def apply_discount(self):
        return 0.10  


class ClothingProduct(Product):
    def apply_discount(self):
        return 0.15  



class LoyaltyTier:
    def get_discount_rate(self):
        return 0.0


class RegularTier(LoyaltyTier):
    def get_discount_rate(self):
        return 0.0


class SilverTier(LoyaltyTier):
    def get_discount_rate(self):
        return 0.05


class GoldTier(LoyaltyTier):
    def get_discount_rate(self):
        return 0.10


class BillingEngine:
    def __init__(self, cart, loyalty_tier):
        self.cart = cart
        self.loyalty_tier = loyalty_tier

    def generate_bill(self):
        original_total = 0
        category_discount_total = 0

        print("\n" + "=" * 76)
        print("                    RETAIL STORE BILL")
        print("=" * 76)
        print(
            f"{'Product':<18}"
            f"{'Qty':>5}"
            f"{'Price':>12}"
            f"{'Subtotal':>12}"
            f"{'Discount':>12}"
            f"{'Final':>12}"
        )
        print("-" * 76)

        for product in self.cart:
            name = product.get_name()
            price = product.get_price()
            quantity = product.get_quantity()

            subtotal = price * quantity

            discount_rate = product.apply_discount()
            discount_amount = subtotal * discount_rate
            final_price = subtotal - discount_amount

            original_total += subtotal
            category_discount_total += discount_amount

            print(
                f"{name:<18}"
                f"{quantity:>5}"
                f"{price:>12.2f}"
                f"{subtotal:>12.2f}"
                f"{discount_amount:>12.2f}"
                f"{final_price:>12.2f}"
            )

        subtotal_after_discount = (
            original_total - category_discount_total
        )

        loyalty_rate = self.loyalty_tier.get_discount_rate()
        loyalty_discount = subtotal_after_discount * loyalty_rate

        grand_total = subtotal_after_discount - loyalty_discount

        print("-" * 76)
        print(f"{'Original Total:':<35} Rs. {original_total:>12.2f}")
        print(
            f"{'Category Discounts:':<35} "
            f"Rs. {category_discount_total:>12.2f}"
        )
        print(
            f"{'Subtotal After Discounts:':<35} "
            f"Rs. {subtotal_after_discount:>12.2f}"
        )
        print(
            f"{'Loyalty Tier:':<35} "
            f"{self.loyalty_tier.__class__.__name__:>15}"
        )
        print(
            f"{'Loyalty Discount:':<35} "
            f"Rs. {loyalty_discount:>12.2f}"
        )
        print("=" * 76)
        print(f"{'GRAND TOTAL:':<35} Rs. {grand_total:>12.2f}")
        print("=" * 76)

        return grand_total



cart = [
        GroceryProduct("Rice", 100, 2),
        ElectronicsProduct("Mobile", 20000, 1),
        ClothingProduct("T-Shirt", 500, 2)
    ]

print("Choose Customer Loyalty Tier")
print("1. Regular")
print("2. Silver")
print("3. Gold")

choice = input("Enter your choice (1-3): ")

loyalty_tiers = {
        "1": RegularTier,
        "2": SilverTier,
        "3": GoldTier
    }

if choice not in loyalty_tiers:
        print("Invalid loyalty tier selected.")
else:
        selected_tier = loyalty_tiers[choice]()
        billing_engine = BillingEngine(cart, selected_tier)
        billing_engine.generate_bill()
