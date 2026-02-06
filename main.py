import random
import math
import os



class LuhnFactory:
    """
    A utility class for validating and generating Luhn-compliant numbers.
    """
    @staticmethod
    def calculate_luhn_sum(number_str: str) -> int:
        """Calculates the Luhn checksum for a given string of digits."""
        digits = [int(d) for d in number_str]
        checksum = 0
        is_second = False

        # Iterate from right to left
        for i in range(len(digits) - 1, -1, -1):
            d = digits[i]
            if is_second:
                d = d * 2
                if d > 9:
                    d -= 9
            checksum += d
            is_second = not is_second
        
        return checksum

    @staticmethod
    def is_valid(number: str) -> bool:
        """Checks if the provided number string passes the Luhn algorithm."""
        if not number.isdigit():
            return False
        return LuhnFactory.calculate_luhn_sum(number) % 10 == 0

    @staticmethod
    def generate_valid_number(length: int) -> str:
        """
        Generates a valid Luhn number of a specific length using deterministic calculation.
        Strategy: Generate N-1 random digits, then calculate the required check digit.
        """
        if length <= 0:
            raise ValueError("Length must be positive")

        # 1. Generate the first N-1 digits randomly
        partial_number = "".join([str(random.randint(0, 9)) for _ in range(length - 1)])
        
        # 2. Calculate checksum of these digits (treating the missing digit as 0 temporarily)
        # Note: We need to account for the position. The check digit is at index -1.
        # So we append a '0', calculate the sum, and see what we need to add to reach mod 10.
        
        temp_full = partial_number + "0"
        current_sum = LuhnFactory.calculate_luhn_sum(temp_full)
        
        # 3. Calculate the check digit required to make sum % 10 == 0
        remainder = current_sum % 10
        check_digit = (10 - remainder) % 10
        
        return partial_number + str(check_digit)


MENU_OPTIONS = {
    "Financial": {
        1: ("Visa", 16),
        2: ("Visa (Old)", 13),
        3: ("MasterCard", 16),
        4: ("American Express", 15),
        5: ("Discover", 16),
        6: ("Diners Club", 14),
        7: ("Maestro", 19),
        8: ("JCB", 16),
    },
    "Telecom": {
        9: ("IMEI", 15),
        10: ("ICCID", 19),
        11: ("ICCID (Long)", 20),
    },
    "Government": {
        12: ("US NPI", 10),
        13: ("Canadian SIN", 9),
        14: ("South African ID", 13),
        15: ("Israeli ID", 9),
        16: ("Greek AMKA", 11),
        17: ("Swedish Personnummer", 10),
        18: ("Swedish Personnummer (Long)", 12),
    },
    "Other": {
        19: ("UPC (Barcode)", 12),
        20: ("USPS Tracking", 22),
    }
}

def clear_screen():
    return os.system("cls")


def display_menu():
    print("\n" + "="*40)
    print(f"{'LUHN GENERATOR TOOL':^40}")
    print("="*40)
    
    # Flatten the dict for display logic
    for category, items in MENU_OPTIONS.items():
        print(f"\n--- {category} ---")
        for key, (name, length) in items.items():
            print(f"[{key}] {name} ({length} digits)")
    print("\n[V] Validate a Number")
    print("[Q] Quit")

def main():
    # Flatten options for easier lookup: {1: ("Visa", 16), ...}
    flat_options = {}
    for group in MENU_OPTIONS.values():
        flat_options.update(group)

    while True:
        display_menu()
        choice = input("\nSelect an option: ").strip().lower()

        if choice == 'q':
            print("Exiting...")
            break

        if choice == 'v':
            number = input("\nEnter number to validate: ").strip()
            is_valid = LuhnFactory.is_valid(number)
            print("\n" + "-"*40)
            print(f"Number: {number}")
            print(f"Result: {'✅ VALID' if is_valid else '❌ INVALID'}")
            print("-"*40)
            input("Press Enter to continue...")
            clear_screen()
            continue

        if not choice.isdigit() or int(choice) not in flat_options:
            print("❌ Invalid selection. Please try again.")
            continue

        name, length = flat_options[int(choice)]
        
        count = input(f"\nHow many {name} numbers to generate? (default: 1): ").strip()
        count = int(count) if count.isdigit() and int(count) > 0 else 1
        
        print("\n" + "-"*40)
        print(f"✅ Generated {count} Valid {name} Number(s):")
        print("-"*40)
        
        for i in range(count):
            valid_number = LuhnFactory.generate_valid_number(length)
            is_valid = LuhnFactory.is_valid(valid_number)
            print(f"{i+1}. {valid_number} [{'PASS' if is_valid else 'FAIL'}]")
        
        print("-"*40)
        input("Press Enter to continue...")
        clear_screen()

if __name__ == "__main__":
    main()