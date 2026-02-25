# ********** Restaurant Management System (Advanced) ********** #

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class MenuItem:
    """Represents a single menu item with name, price, and category."""
    name: str
    price: float
    category: str


class Menu:
    """Manages the restaurant menu and lookups."""
    
    def __init__(self):
        self.items = [
            MenuItem("Pizza", 40, "Food"),
            MenuItem("Pasta", 50, "Food"),
            MenuItem("Burger", 60, "Food"),
            MenuItem("Salad", 70, "Food"),
            MenuItem("Coffee", 80, "Beverage"),
            MenuItem("Juice", 45, "Beverage"),
            MenuItem("Tea", 30, "Beverage"),
        ]
    
    def get_item(self, name: str) -> MenuItem | None:
        """Find menu item by name (case-insensitive)."""
        name_lower = name.strip().lower()
        return next((item for item in self.items if item.name.lower() == name_lower), None)
    
    def display(self, by_category: bool = True):
        """Display menu, optionally grouped by category."""
        print("\n" + "=" * 40)
        print("**** MENU ****")
        print("=" * 40)
        if by_category:
            categories = {}
            for item in self.items:
                categories.setdefault(item.category, []).append(item)
            for category, items in categories.items():
                print(f"\n  [{category}]")
                for item in items:
                    print(f"    {item.name}: Rs {item.price}")
        else:
            for item in self.items:
                print(f"  {item.name}: Rs {item.price}")
        print("=" * 40)


class Order:
    """Manages a customer's order (cart) with quantities."""
    
    def __init__(self):
        self.items: dict[str, int] = {}  # item_name -> quantity
        self.tax_rate = 0.05  # 5% tax
        self.menu = Menu()
    
    def add_item(self, name: str, quantity: int = 1) -> bool:
        """Add item to order. Returns True if successful."""
        item = self.menu.get_item(name)
        if not item:
            return False
        self.items[item.name] = self.items.get(item.name, 0) + quantity
        return True
    
    def remove_item(self, name: str) -> bool:
        """Remove item from order. Returns True if successful."""
        item = self.menu.get_item(name)
        if not item or item.name not in self.items:
            return False
        del self.items[item.name]
        return True
    
    def update_quantity(self, name: str, quantity: int) -> bool:
        """Update quantity of an item. Remove if quantity <= 0."""
        item = self.menu.get_item(name)
        if not item or item.name not in self.items:
            return False
        if quantity <= 0:
            del self.items[item.name]
        else:
            self.items[item.name] = quantity
        return True
    
    def subtotal(self) -> float:
        """Calculate subtotal before tax."""
        total = 0
        for name, qty in self.items.items():
            item = self.menu.get_item(name)
            if item:
                total += item.price * qty
        return total
    
    def tax_amount(self) -> float:
        """Calculate tax amount."""
        return round(self.subtotal() * self.tax_rate, 2)
    
    def grand_total(self) -> float:
        """Calculate total including tax."""
        return round(self.subtotal() + self.tax_amount(), 2)
    
    def display_cart(self):
        """Display current cart with itemized prices."""
        if not self.items:
            print("\n  Your cart is empty.")
            return
        print("\n" + "-" * 40)
        print("**** YOUR CART ****")
        print("-" * 40)
        for name, qty in self.items.items():
            item = self.menu.get_item(name)
            if item:
                line_total = item.price * qty
                print(f"  {name} x{qty} = Rs {line_total}")
        print("-" * 40)
        print(f"  Subtotal: Rs {self.subtotal()}")
        print(f"  Tax (5%): Rs {self.tax_amount()}")
        print(f"  GRAND TOTAL: Rs {self.grand_total()}")
        print("-" * 40)
    
    def generate_receipt(self) -> str:
        """Generate formatted receipt string."""
        lines = [
            "\n" + "=" * 44,
            "       PYTHON RESTAURANT - RECEIPT",
            "=" * 44,
            f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "-" * 44,
        ]
        for name, qty in self.items.items():
            item = self.menu.get_item(name)
            if item:
                lines.append(f"  {name} x{qty} @ Rs {item.price} = Rs {item.price * qty}")
        lines.extend([
            "-" * 44,
            f"  Subtotal:     Rs {self.subtotal()}",
            f"  Tax (5%):     Rs {self.tax_amount()}",
            f"  GRAND TOTAL:  Rs {self.grand_total()}",
            "=" * 44,
            "       Thank you for your order!",
            "=" * 44 + "\n",
        ])
        return "\n".join(lines)


def get_positive_int(prompt: str, default: int = 1) -> int:
    """Get a positive integer from user input."""
    while True:
        try:
            val = input(prompt).strip() or str(default)
            num = int(val)
            if num > 0:
                return num
            print("  Please enter a positive number.")
        except ValueError:
            print("  Invalid input. Enter a number.")


def main():
    order = Order()
    
    print("\n********** Welcome to Python Restaurant **********")
    order.menu.display()
    
    while True:
        print("\n[1] Add item  [2] Remove item  [3] View cart  [4] Checkout")
        choice = input("Choice: ").strip()
        
        if choice == "1":
            item_name = input("Enter item name: ").strip()
            quantity = get_positive_int("Quantity (default 1): ", 1)
            if order.add_item(item_name, quantity):
                item = order.menu.get_item(item_name)
                print(f"  Added {quantity}x {item.name} to your order.")
            else:
                print("  Item not found. Order from the menu.")
                order.menu.display()
        
        elif choice == "2":
            if not order.items:
                print("  Your cart is empty.")
            else:
                item_name = input("Enter item to remove: ").strip()
                if order.remove_item(item_name):
                    print("  Item removed.")
                else:
                    print("  Item not in cart.")
        
        elif choice == "3":
            order.display_cart()
        
        elif choice == "4":
            if not order.items:
                print("  Your cart is empty. Add items before checkout.")
            else:
                order.display_cart()
                confirm = input("\nProceed to payment? (y/n): ").strip().upper()
                if confirm == "Y":
                    receipt = order.generate_receipt()
                    print(receipt)
                    # Save receipt to file
                    filename = "receipt.txt"
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(receipt)
                    print(f"  Receipt saved to {filename}")
                    break
                else:
                    print("  Checkout cancelled.")
        
        else:
            print("  Invalid choice. Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
